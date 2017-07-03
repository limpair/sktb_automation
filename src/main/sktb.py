# coding=utf-8

from bs4 import BeautifulSoup
import time, math, re

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
    if is_element_exist(driver, '.module-quick'):
        driver.find_element_by_id('J_Quick2Static').click()
    time.sleep(4)
    driver.find_element_by_id('TPL_username_1').send_keys(username)
    time.sleep(4)
    driver.find_element_by_id('TPL_password_1').send_keys(password)

    if is_element_exist(driver, '#nc_1_n1z'):
        print "huakuai"
        # actions = ActionChains(driver)
        huakuai = driver.find_element_by_id('nc_1_n1z')
        loc = huakuai.location
        print loc
        time.sleep(5)
        # ActionChains(driver).drag_and_drop_by_offset(huakuai,258,0).perform()
        print "wait"
        time.sleep(5)
        print driver.find_element_by_id('nc_1_n1z').location
    driver.find_element_by_id('J_SubmitStatic').click()
    time.sleep(10)
def loginShikee(driver, username, password):
    driver.get('http://login.shikee.com/')
    time.sleep(10)
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
        soup = BeautifulSoup(driver.page_source).find_all(id='load_list')[0].find_all('tr')
        k = len(soup)
        for i in range(1, k - 1):
            t = soup[i].find_all('td')
            # 0,4,6
            title = t[0].find_all('img')[0].attrs['art'].encode('utf-8')
            num = re.sub("\D", "", t[4].text)
            link = t[6].find_all('a')[0].attrs['href'].split('?')[0]
            li.append({'title':title, 'num':num, 'link':link})
    return li

def saveTryList(driver, try_list):
    li = []
    host = 'http://user.shikee.com'
    for u in try_list:
        url = host + u['link']
        driver.get(url + '/0')
        time.sleep(2)
        if is_element_exist(driver, '#total'):
            total = int(driver.find_element_by_id('total').text)
            n = int(math.ceil(total / 20.0))
        else:
            n = 1
        user = []
        for i in range(0, n):
            driver.get(url + '/' + str(i * 20))
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source).find_all(id='load-buyer-list')[0].find_all('tr')
            k = len(soup)
            J = 0
            for j in range(1, k):
                time.sleep(1.8)
                rows = soup[j].attrs['id'].split('_')[1]
                try:
                    driver.find_element_by_xpath("//div[@data-uid='" + rows + "']").click()
                except:
                    j = j - 1
                    if J - j >= 3:
                        continue
                    else:
                        J = J + 1
                
            time.sleep(1.5)
            soup = BeautifulSoup(driver.page_source).find_all(id='load-buyer-list')[0].find_all('tr')
            
            for l in range(1, k):
                rows = soup[l].attrs['id'].split('_')[1]
                t = soup[l].find_all('td')
                sp = t[3].find_all('span')
                SP = {}
                for x in sp:
                    temp = re.findall(r'(\w*[0-9]+)\w*', x.text)
                    ss = x.text.split('(')[0]
                    if u'近30内填写订单号的平均时长' == ss:
                        SP['AverageTime'] = int(temp[len(temp) - 1]);
                    elif u'违规次数' == ss:
                        SP['ViolationNumber'] = int(temp[len(temp) - 1]);
                    elif u'近30日下单次数' == ss:
                        SP['OrderNumber'] = int(temp[len(temp) - 1]);
                    elif u'近30日获得试用次数' == ss:
                        SP['TryNumber'] = int(temp[len(temp) - 1]);
                    elif u'试客放弃试用次数' == ss:
                        SP['AbandonNumber'] = int(temp[len(temp) - 1]);
                    elif u'试客提交无效订单号次数' == ss:
                        SP['InvalidNumber'] = int(temp[len(temp) - 1]);
                    elif u'试客总参与试用次数' == ss:
                        SP['TrySum'] = int(temp[len(temp) - 1]);
                print SP
                user.append({'id':int(rows), 'sys':SP, 'name':t[1].find_all('span')[0].attrs['title'], 'time':t[2].text})
        u['user'] = user       
        li.append(u)
    return li
    
