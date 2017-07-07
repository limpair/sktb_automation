# coding=utf-8
from bs4 import BeautifulSoup
import time
import math
import re
import datetime
import sktb

skhost = 'http://user.shikee.com'
state = '?state[]=&state[]=&state[]=&report_state[]=&trade_state[]=2&key=&trade_no='
tbhost = 'https://trade.taobao.com/trade/itemlist/list_sold_items.htm'
tb = 'https://trade.taobao.com'

def getOrderNumber(driver, trs):
    result = []
    for tr in trs:
        link = tr['link'].replace('look_wait_join_list', 'look_pass_join_list')
        driver.get(skhost + link + '/0' + state)
        if sktb.is_element_exist(driver, '#total'):
            total = int(driver.find_element_by_id('total').text)
            n = int(math.ceil(total / 10.0))
        else:
            n = 1
        order = []
        for i in range(0, n):
            driver.get(skhost + link + str(i * 10) + state)
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source).find_all(id='load_list')[0].find_all('tr')
            Len = len(soup)
            if Len > 2:
                for j in range(1, Len - 1):
                    order.append(''.join(soup[j].find_all(class_='trade_number').text.split()))
        tr['passlink'] = link
        tr['order'] = order
        result.append(tr)
    return result

def verify(driver,url,order,flag):
    driver.get(url)
    driver.find_element_by_id('orderNumber').send_keys(order)
    driver.find_element_by_xpath('//*[@id="key_from"]/input[3]').click()
    driver.find_element_by_xpath('//*[@id="load_list"]/table/tbody/tr[2]/td[5]/a[2]').click()
    
    if flag:
        driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[2]/td[3]/input[2]').click()
    else:
        driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[2]/td[3]/input[3]').click()
    
    driver.find_element_by_id('sub_trade_number').click()

def addRemarks(driver, trs, color):
    trs = getOrderNumber(driver, trs)
    for tr in trs:
        for i in tr['order']:
            driver.get(tbhost)
            time.sleep(1)
            driver.find_element_by_id('bizOrderId').send_keys(i)
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="sold_container"]/div/div[1]/div[1]/form/div[7]/div/div/button[1]').click()
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source)
            page = soup.find_all(attrs={"data-reactid": ".0.5"})[0]
            div = page.find_all(class_='suborder-mod__order-table___2SEhF')
            llen = len(div)
            if llen > 0:
                td = div[0].find_all('td')
                status = td[5].text
                if ''.join(td[3].text.split()) == '':
                    if u'买家已付款' in status:
                        pass
                    elif u'卖家已发货' in status:
                        pass
                    elif u'交易成功' in status:
                        pass
                    elif u'资金保护中' in status:
                        pass
                else:
                    driver.find_element_by_id('flag')
                    href = page.find_all(id='flag')[0].get('href')
                    driver.get(tb + href)
                    time.sleep(1)
                    if u'买家已付款' in status:    
                        driver.find_element_by_id('flag1').click()
                        time.sleep(0.5)
                        for cc in color:
                            if cc in tr['title']:
                                driver.find_element_by_id('memo').send_keys(cc)
                                break
                        time.sleep(0.5)
                        driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
                        time.sleep(1)
                        verify(driver,skhost+tr['passlink'],i,True)
                        
                    if u'等待买家付款' in status:
                        driver.find_element_by_id('flag1').click()
                        time.sleep(0.5)
                        driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
                        time.sleep(1)
            else:
                verify(driver,skhost+tr['passlink'],i,False)
    
    
