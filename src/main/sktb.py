# coding=utf-8

from bs4 import BeautifulSoup
import sqlite
import time
import math
import re
import datetime

host = 'http://user.shikee.com'


def toInt(s):
    return s == '' and -1 or int(s)


def is_element_exist(driver, css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print "Not find the element: %s" % css
        return False
    elif len(s) == 1:
        return True
        print "Find the element: %s" % css
    else:
        print "Find %s element: %s" % (len(s), css)
        return False


def loginTaobao(driver, username, password):
    print username + '\n' + password
    driver.get('https://login.taobao.com/member/login.jhtml')
    time.sleep(1.5)
    if is_element_exist(driver, '.module-quick'):
        driver.find_element_by_id('J_Quick2Static').click()
    time.sleep(3)
    driver.find_element_by_id('TPL_username_1').send_keys(username)
    time.sleep(3)
    driver.find_element_by_id('TPL_password_1').send_keys(password)

    if is_element_exist(driver, '#nc_1_n1z'):
        print u'滑块验证中'
        time.sleep(8)
    driver.find_element_by_id('J_SubmitStatic').click()
    time.sleep(5)

def loginShikee(driver, username, password):
    driver.get('http://login.shikee.com/')
    time.sleep(5)
    driver.find_element_by_xpath('//i[@class="iconimg pc"]').click()
    driver.find_element_by_id('J_userName').send_keys(username)
    driver.find_element_by_id('J_pwd').send_keys(password)
    time.sleep(2)
    driver.find_element_by_id('J_submit').click()
    time.sleep(5)


def saveActiveList(driver):
    li = []
    listUrl = 'http://user.shikee.com/seller/tryings/try_list/'
    search = '?key=&search_type=try_name&state[]=3&state[]=4&is_block=&check_fail=&wait_check_out='
    driver.get(listUrl + str(0) + search)
    time.sleep(2)
    if is_element_exist(driver, '#total'):
        total = int(driver.find_element_by_id('total').text)
        n = int(math.ceil(total / 10.0))
    else:
        n = 1
    for i in range(0, n):
        driver.get(listUrl + str(i * 10) + search)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source).find_all(
            id='load_list')[0].find_all('tr')
        k = len(soup)
        for i in range(1, k - 1):
            t = soup[i].find_all('td')
            # 0,4,6
            title = t[0].find_all('img')[0].attrs['art'].encode('utf-8')

            ttt = time.mktime(time.strptime(
                t[0].find_all('p')[0].text, '%Y-%m-%d %H:%M:%S'))
            num = int(re.sub("\D", "", t[4].text))
            link = t[6].find_all('a')[0].attrs['href'].split('?')[0]
            li.append({'title': title, 'num': num, 'link': link, 'time': ttt})
    return li

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
    if t['bilv'] != '' and sys['TryNumber'] != 0 and (sys['OrderNumber'] * 1.0 / sys['TryNumber'] * 1.0) > float(t['bilv']):
        count = count + 1
    elif t['bilv'] == '':
        count = count + 1
    if count == 4:
        return True
    else:
        return False

def judgeTaobao(driver, name, day):
    driver.get('https://trade.taobao.com/trade/itemlist/list_sold_items.htm')
    time.sleep(1)
    driver.find_element_by_id('buyerNick').send_keys(name)
    driver.find_element_by_xpath('//*[@id="sold_container"]/div/div[1]/div[1]/form/div[7]/div/div/button[1]').click()
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
    

def passUser(driver, link, name):
    driver.get(link)
    time.sleep(2)
    driver.find_element_by_id('key').send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath('//input[@type="submit"]').click()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="load-buyer-list"]/tbody/tr[2]/td[5]/a[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div/p[2]/input[1]').click()
    return True
    
def executeActivity(driver, try_list, tasks, tri):
    conn = sqlite.DataBaseControl()
    for task in tasks:
        count = 0
        name = task['name']
        num = task['num']
        out = open(tri['account'] + '.txt', 'a')
        a = time.time()
        for tr in try_list:
            if name.upper() in tr['title'].upper():
                driver.get(host + tr['link'] + '/0')
                time.sleep(2)
                
                if is_element_exist(driver, '#total'):
                    total = int(driver.find_element_by_id('total').text)
                    n = int(math.ceil(total / 20.0))
                else:
                    n = 1
                users = []
                for i in range(0, n):
                    driver.get(host + tr['link'] + '/' + str(i * 20) + '?sysarrs%5B%5D=order_count&sysarrs%5B%5D=join_count&sysarrs%5B%5D=completion_count')
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
                                SP['AverageTime'] = int(temp[len(temp) - 1])
                            elif u'违规次数' == ss:
                                SP['ViolationNumber'] = int(temp[len(temp) - 1])
                            elif u'近30日下单次数' == ss:
                                SP['OrderNumber'] = int(temp[len(temp) - 1])
                            elif u'近30日获得试用次数' == ss:
                                SP['TryNumber'] = int(temp[len(temp) - 1])
                            elif u'试客放弃试用次数' == ss:
                                SP['AbandonNumber'] = int(temp[len(temp) - 1])
                            elif u'试客提交无效订单号次数' == ss:
                                SP['InvalidNumber'] = int(temp[len(temp) - 1])
                            elif u'试客总参与试用次数' == ss:
                                SP['TrySum'] = int(temp[len(temp) - 1])
                        
                        users.append({'id': int(rows), 'sys': SP, 'name': t[1].find_all(
                            'span')[0].attrs['title'], 'time': t[2].text, 'skname':t[1].find_all('img')[0].attrs['art']})

                for user in users:
                    dbUsers = conn.getByName(user['name'], tri['account'])
                    user['account'] = tri['account']
                    user['activity'] = name
                    if judgeSysData(tri, user['sys']) == False:
                        continue
                    if len(dbUsers) > 0:
                        if dbUsers[0]['name'] == user['name']:
                            nowtime = round((time.time() - dbUsers[0]['mktime']) / 86400.0, 4)
                            if nowtime >= 3.0:
                                if judgeTaobao(driver, user['name'], ''.join(tri['days'].split())):
                                    if passUser(driver, host + tr['link'], user['skname']):
                                        count = count + 1
                                        user['passtime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                        conn.save(user)
                                continue
                    elif judgeTaobao(driver, user['name'], ''.join(tri['days'].split())):
                        if passUser(driver, host + tr['link'], user['skname']):
                            count = count + 1
                            user['passtime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            conn.save(user)
                    
                    if count == tr['num'] or count == num:
                        break
                
            if count == num:
                break
        b = time.time()
        out.write('活动' + name + '，预计通过 ' + str(num) + ' 人，已通过 ' + str(count) + ' 人，用时 ' + str(round(b - a, 2)) + '。' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print u'活动' + name + u'通过 ' + str(count) + u' 人，用时' + str(round(b - a, 2)) + u'，' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
