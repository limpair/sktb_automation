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
    li = {}
    total = int(driver.find_element_by_id('total').text)
    n = int(math.ceil(total / 10.0))
    listUrl = 'http://user.shikee.com/seller/tryings/try_list/'
    search = '?key=&search_type=try_name&state[]=3&state[]=4&is_block=&check_fail=&wait_check_out='
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
            li[link] = {'title':title, 'num':num, 'link':link}
    return li

def saveTryList(driver, url):
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_id('chebox3').click()
    driver.find_element_by_id('chebox4').click()
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source)
    total = int(soup.find_all(id='total')[0].text)
