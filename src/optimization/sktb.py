# coding=utf-8

from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sqlite
import time
import math
import re
import datetime
import os
import debug
import sys

host = 'http://user.shikee.com'


def toInt(s):
    return s == '' and -1 or int(s)


def is_element_exist(driver, css):
    # driver.implicitly_wait(10)
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        # print "Not find the element: %s" % css
        return False
    elif len(s) == 1:
        return True
        # print "Find the element: %s" % css
    else:
        # print "Find %s element: %s" % (len(s), css)
        return False


def exists(Path):
    if os.path.exists(Path):
        return True
    else:
        os.makedirs(Path)
        if os.path.exists(Path):
            return True
    return False


def loginTaobao(driver, username, password):
    result = True
    try:
        driver.implicitly_wait(10)
        driver.get('https://login.taobao.com/member/login.jhtml')
        time.sleep(1.5)
        if is_element_exist(driver, '.module-quick'):
            J_Quick2Static = WebDriverWait(driver, 10, 0.5).until(
                EC.presence_of_element_located((By.ID, 'J_Quick2Static')))
            J_Quick2Static.click()

        TPL_username_1 = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'TPL_username_1')))
        TPL_username_1.send_keys(username)

        TPL_password_1 = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'TPL_password_1')))
        TPL_password_1.send_keys(password)

        if is_element_exist(driver, '#nc_1_n1z'):
            debug.message('存在滑块等待8s：', os.path.basename(__file__))
            time.sleep(8)
        J_SubmitStatic = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'J_SubmitStatic')))
        J_SubmitStatic.click()
        time.sleep(5)
    except Exception, e:
        result = False
        info = sys.exc_info()
        debug.log(str(sys.exc_info()[2].tb_lineno),
                  e.message, info[1], os.path.basename(__file__))
    return result


def loginShikee(driver, username, password):
    result = True
    try:
        driver.implicitly_wait(10)
        driver.get('http://login.shikee.com/')
        iconimg = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="iconimg pc"]')))
        iconimg.click()
        J_userName = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'J_userName')))
        J_userName.send_keys(username)
        J_pwd = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'J_pwd')))
        J_pwd.send_keys(password)
        J_submit = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'J_submit')))
        J_submit.click()
        time.sleep(5)
    except Exception, e:
        result = False
        info = sys.exc_info()
        debug.log(str(sys.exc_info()[2].tb_lineno),
                  e.message, info[1], os.path.basename(__file__))
    return result


def saveActiveList(driver):
    result = True
    try:
        driver.implicitly_wait(10)
        li = []
        listUrl = 'http://user.shikee.com/seller/tryings/try_list/'
        search = '?key=&search_type=try_name&state[]=3&state[]=4&is_block=&check_fail=&wait_check_out='
        driver.get(listUrl + str(0) + search)
        # time.sleep(2)
        if is_element_exist(driver, '#total'):
            total = WebDriverWait(driver, 10, 0.5).until(
                EC.presence_of_element_located((By.ID, 'total')))
            total = int(total.text)
            n = int(math.ceil(total / 10.0))
        else:
            n = 1
        for i in range(0, n):
            driver.get(listUrl + str(i * 10) + search)
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source).find_all(id='load_list')[0].find_all('tr')
            k = len(soup)
            for i in range(1, k - 1):
                t = soup[i].find_all('td')
                # 0,4,6
                title = t[0].find_all('img')[0].attrs['art'].encode('utf-8')
                if u'已经屏蔽' in t[2].text:
                    continue
                ttt = time.mktime(time.strptime(
                    t[0].find_all('p')[0].text, '%Y-%m-%d %H:%M:%S'))
                num = int(re.sub("\D", "", t[4].text))
                link = t[6].find_all('a')[0].attrs['href'].split('?')[0]
                li.append({'title': title, 'num': num, 'link': link, 'time': ttt})
    except Exception, e:
        result = False
        info = sys.exc_info()
        debug.log(str(sys.exc_info()[2].tb_lineno),
                  e.message, info[1], os.path.basename(__file__))
    return li, result

# {'title': title, 'num': num, 'link': link, 'time': ttt}
# invalidOrders    # 无效订单次数
# averageTime      # 填写订单号平均时长
# total            # 参与试用总次数
# trialsNumber     # 近30日获得试用次数
# abandonNumber    # 放弃试用次数
# number           # 近30天下单次数
# violationsNumber # 违规次数


def judgeSys(c, a, b):
    if a >= 0:
        if a >= b:
            c = c + 1
    else:
        c = c + 1
    return c


def judgeSysData(t, sys):
    total = toInt(t['total'])
    trials = toInt(t['trialsNumber'])
    number = toInt(t['number'])
    count = 0
    count = judgeSys(count, total, sys['TrySum'])
    count = judgeSys(count, trials, sys['TryNumber'])
    count = judgeSys(count, number, sys['OrderNumber'])
    try:
        if t['bilv'] != '' and sys['TryNumber'] != 0 and (sys['OrderNumber'] * 1.0 / sys['TryNumber'] * 1.0) > float(t['bilv']):
            count = count + 1
        elif t['bilv'] == '':
            count = count + 1
    except Exception, e:
        info = sys.exc_info()
        debug.log(str(sys.exc_info()[2].tb_lineno),
                  e.message, info[1], os.path.basename(__file__))
        debug.message('判断账号能否通过存在问题，调过此账号：', os.path.basename(__file__))
    if count == 4:
        return True
    else:
        return False


def judgeTaobao(driver, name, day):
    try:
        driver.implicitly_wait(10)
        driver.get('https://trade.taobao.com/trade/itemlist/list_sold_items.htm')
        # time.sleep(1.5)
        buyerNick = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'buyerNick')))
        buyerNick.send_keys(name)
        search_btn = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sold_container"]/div/div[1]/div[1]/form/div[7]/div/div/button[1]')))
        search_btn.click()
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source)
        page = soup.find_all(attrs={"data-reactid": ".0.5"})[0]
        if day == '':
            if u'没有符合条件的宝贝，请尝试其他搜索条件' in page.text:
                return True
            if (u'买家已付款' in page.text) or (u'卖家已发货' in page.text) or (u'交易成功' in page.text) or (u'资金保护中' in page.text):
                return False
            else:
                return True
        else:
            if u'没有符合条件的宝贝，请尝试其他搜索条件' in page.text:
                return True
            divs = page.find_all(class_='item-mod__trade-order___2LnGB')
            for div in divs:
                if (u'买家已付款' in div.text) or (u'卖家已发货' in div.text) or (u'交易成功' in div.text) or (u'资金保护中' in div.text):
                    tt = div.find_all('label')[0].find_all('span')[5].text
                    old = time.mktime(time.strptime(tt, '%Y-%m-%d %H:%M:%S'))
                    now = time.time()
                    if round((now - old) / 86400.0, 4) - float(day) > 0:
                        return True
            return False
    except Exception, e:
        info = sys.exc_info()
        debug.log(str(sys.exc_info()[2].tb_lineno),
                  e.message, info[1], os.path.basename(__file__))
        return False


def passUser(driver, link, name):
    try:
        driver.implicitly_wait(10)
        driver.get(link)
        time.sleep(2)
        page = BeautifulSoup(driver.page_source)
        bs = page.find_all(class_='ParList_top')[0].find_all('b')
        l = len(bs)
        if int(''.join(bs[l - 1].text.split())) == 0:
            return False
        key = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'key')))
        key.send_keys(name)
        submit = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
        submit.click()
        search = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="load-buyer-list"]/tbody/tr[2]/td[5]/a[1]')))
        search.click()
        passbtn = WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div/p[2]/input[1]')))
        passbtn.click()
        time.sleep(0.5)
    except Exception, e:
        info = sys.exc_info()
        debug.log(str(sys.exc_info()[2].tb_lineno),
                  e.message, info[1], os.path.basename(__file__))
        return False
    return True

def cmp_sort(a, b):
    x1 = a['sys']['OrderNumber']
    y1 = a['sys']['TryNumber']
    x2 = b['sys']['OrderNumber']
    y2 = b['sys']['TryNumber']
    if y1 == 0 or y2 == 0:
        return -1
    x = int((x1 * 1.0) / (y1 * 1.0) * 10000)
    y = int((x2 * 1.0) / (y2 * 1.0) * 10000)
    return y - x
def judgeNum(driver):
    driver.implicitly_wait(10)
    page = BeautifulSoup(driver.page_source)
    bs = page.find_all(class_='ParList_top')[0].find_all('b')
    l = len(bs)
    if int(''.join(bs[l - 1].text.split())) == 0:
        return True
    return False


def executeActivity(driver, try_list, tasks, tri):
    driver.implicitly_wait(10)
    result = True
    conn = sqlite.DataBaseControl()
    for task in tasks:
        try:
            count = 0
            name = task['name']
            num = task['num']
            tbname = tri['tbuser'].replace(u':', u'：')
            if not os.path.exists(tbname):
                os.makedirs(tbname)
                # fp = open(tri['account'] + '/' + tri['tbuser'].replace(u':', u'：'), 'w')
                # fp.write('1')
                # fp.close()
            out = open(tbname + u'/10.审批会员统计.txt', 'a')
            a = time.time()
            for tr in try_list:
                if tr['num'] <= 0:
                    continue
                if count >= num:
                    break
                title = ''.join(tr['title'][0:3].split())
                if name.upper() == title.upper():
                    driver.get(host + tr['link'] + '/0')
                    time.sleep(2)
                    if judgeNum(driver):
                        continue
                    if is_element_exist(driver, '#total'):
                        total = int(driver.find_element_by_id('total').text)
                        n = int(math.ceil(total / 20.0))
                    else:
                        n = 1
                    users = []
                    for i in range(0, n):
                        driver.get(host + tr['link'] + '/' + str(
                            i * 20) + '?sysarrs%5B%5D=order_count&sysarrs%5B%5D=join_count&sysarrs%5B%5D=completion_count')
                        time.sleep(2)
                        soup = BeautifulSoup(driver.page_source).find_all(
                            id='load-buyer-list')[0].find_all('tr')
                        k = len(soup)

                        for l in range(1, k):
                            rows = soup[l].attrs['id'].split('_')[1]
                            t = soup[l].find_all('td')
                            sp = t[3].find_all('span')
                            SP = {}
                            for x in sp:
                                temp = re.findall(r'(\w*[0-9]+)\w*', x.text)
                                ss = x.text.split('(')[0]
                                if u'近30内填写订单号的平均时长' == ss:
                                    SP['AverageTime'] = int(
                                        temp[len(temp) - 1])
                                elif u'违规次数' == ss:
                                    SP['ViolationNumber'] = int(
                                        temp[len(temp) - 1])
                                elif u'近30日下单次数' == ss:
                                    SP['OrderNumber'] = int(
                                        temp[len(temp) - 1])
                                elif u'近30日获得试用次数' == ss:
                                    SP['TryNumber'] = int(temp[len(temp) - 1])
                                elif u'试客放弃试用次数' == ss:
                                    SP['AbandonNumber'] = int(
                                        temp[len(temp) - 1])
                                elif u'试客提交无效订单号次数' == ss:
                                    SP['InvalidNumber'] = int(
                                        temp[len(temp) - 1])
                                elif u'试客总参与试用次数' == ss:
                                    SP['TrySum'] = int(temp[len(temp) - 1])
                            try:
                                users.append({'id': int(rows), 'sys': SP, 'name': t[1].find_all('span')[0].attrs['title'], 'time': t[2].text, 'skname':t[1].find_all('img')[0].attrs['art']})
                            except Exception, e:
                                info = sys.exc_info()
                                debug.log(str(sys.exc_info()[2].tb_lineno), e.message, info[1], os.path.basename(__file__))
                                continue
                    bilv = ''.join(tri['bilv'].split())
                    if bilv != '':
                        users = sorted(users, cmp=cmp_sort)
                    for user in users:
                        username = ''.join(user['name'].split())
                        user['name'] = username
                        if tr['num'] <= 0 or count >= num:
                            break
                        try:
                            dbUsers = conn.getByName(username, tri['account'])
                        except Exception, e:
                            info = sys.exc_info()
                            debug.log(
                                str(sys.exc_info()[2].tb_lineno), e.message, info[1], os.path.basename(__file__))
                            continue
                        user['account'] = tri['account']
                        user['activity'] = name
                        if judgeSysData(tri, user['sys']) == False:
                            continue
                        if len(dbUsers) > 0:
                            dbname = ''.join(dbUsers[0]['name'].split())
                            if dbname == username:
                                nowtime = round((time.time() - dbUsers[0]['mktime']) / 86400.0, 4)
                                if nowtime >= 3.0:
                                    if judgeTaobao(driver, username, ''.join(tri['days'].split())):
                                        driver.get(host + tr['link'])
                                        time.sleep(0.2)
                                        if judgeNum(driver):
                                            break
                                        if passUser(driver, host + tr['link'], user['skname']):
                                            user['id'] = dbUsers[0]['id']
                                            tr['num'] = tr['num'] - 1
                                            count = count + 1
                                            user['passtime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                            conn.save(user)
                                    continue
                        elif judgeTaobao(driver, username, ''.join(tri['days'].split())):
                            driver.get(host + tr['link'])
                            time.sleep(0.2)
                            if judgeNum(driver):
                                break
                            if passUser(driver, host + tr['link'], user['skname']):
                                tr['num'] = tr['num'] - 1
                                count = count + 1
                                user['passtime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                conn.save(user)
        except Exception, e:
            result = False
            info = sys.exc_info()
            debug.log(str(sys.exc_info()[2].tb_lineno),
                      e.message, info[1], os.path.basename(__file__))
        b = time.time()
        out.write('活动' + name + '，预计通过 ' + str(num) + ' 人，已通过 ' + str(count) + ' 人，用时 ' + str(
            round(b - a, 2)) + '。' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        debug.message('活动' + name + '，预计通过 ' + str(num) + ' 人，已通过 ' + str(count) + ' 人，用时 ' + str(round(b - a, 2)
                                                                                                  ) + '。' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), os.path.basename(__file__))
        # print u'活动' + name + u'通过 ' + str(count) + u' 人，用时' + str(round(b - a, 2)) + u'，' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn.close()
    return result
