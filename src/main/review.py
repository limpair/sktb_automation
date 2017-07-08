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
    print u'开始获取订单:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    a = time.time()
    result = []
    count = 0
    for tr in trs:
        link = tr['link'].replace('look_wait_join_list', 'look_pass_join_list')
        driver.get(skhost + link + '/0' + state)
        if sktb.is_element_exist(driver, '#total'):
            total = int(driver.find_element_by_id('total').text)
            n = int(math.ceil(total / 10.0))
        else:
            n = 1
        aaa = BeautifulSoup(driver.page_source).find_all(id='load_list')[0].find_all('tr')
        if len(aaa) == 2:
            continue
        order = []
        for i in range(0, n):
            driver.get(skhost + link + '/' + str(i * 10) + state)
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source).find_all(id='load_list')[0].find_all('tr')
            Len = len(soup)
            if Len > 2:
                for j in range(1, Len - 1):
                    count = count + 1
                    order.append(''.join(soup[j].find_all(class_='trade_number')[0].text.split()))
        tr['passlink'] = link
        tr['order'] = order
        result.append(tr)
    b = time.time()
    print u'结束获取订单:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print u'获取所有任务需要审核的订单的时间为：', b - a
    print u'一共：', count
    return result

def verify(driver, url, order, flag):
    try:
        driver.get(url)
        time.sleep(1)
        driver.find_element_by_id('orderNumber').send_keys(order)
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="key_from"]/input[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="load_list"]/table/tbody/tr[2]/td[5]/a[2]').click()
        time.sleep(1)
        if flag:
            driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[2]/td[3]/input[2]').click()
        else:
            driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[2]/td[3]/input[3]').click()
        time.sleep(0.5)
        driver.find_element_by_id('sub_trade_number').click()
    except:
        return False
    return True

def addRemarks(driver, trs, color):
    
    if sktb.exists(color['tbuser']):
        out = open(color['tbuser'] + u'/error.txt', 'a')
        out1 = open(color['tbuser'] + u'/remark.txt', 'a')
        out2 = open(color['tbuser'] + u'/flag.txt', 'a')
        out3 = open(color['tbuser'] + u'/count.txt', 'a')
        out4 = open(color['tbuser'] + u'/loaddata_time.txt', 'a')
        # out2 = open(color['account']+'/error_order.txt')
    else:
        out = open(color['tbuser'] + u'_error.txt', 'a')
        out1 = open(color['tbuser'] + u'_remark.txt', 'a')
        out2 = open(color['tbuser'] + u'_flag.txt', 'a')
        out3 = open(color['tbuser'] + u'_count.txt', 'a')
        out4 = open(color['tbuser'] + u'_loaddata_time.txt', 'a')
        # out2 = open(color['account']+'_error_order.txt')
    out4.write('开始获取订单:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    trs = getOrderNumber(driver, trs)
    out4.write('结束获取订单:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    out4.close()
    count = {}
    countSum = {}
    
    everyDay = {}
    
    colorCount = {}
    
    for cc in color['list']:
        colorCount[cc] = 0
    
    for tr in trs:
        title = ''.join(tr['title'][0:3].split())
        if len(title) == 2:
            title = title[0] + '0' + title[1]
        countSum[title] = 0
    
    for tr in trs:
        title = ''.join(tr['title'][0:3].split())
        if len(title) == 2:
            title = title[0] + '0' + title[1]
        count[title + tr['passlink']] = 0
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
            di1 = page.find_all(class_='item-mod__trade-order___2LnGB')
            orderTime = di1[0].find_all('label')[0].find_all('span')[5].text
            if orderTime[0:10] not in everyDay.keys():
                everyDay[orderTime[0:10]] = {'sum':{}, 'order':[], 'count':{}}
            llen = len(div)
            if llen > 0:
                td = div[0].find_all('td')
                status = td[5].text
                if ''.join(td[3].text.split()) != '':
                    if u'买家已付款' in status:
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'] + '已付款订单号:' + i + '\n')
                    elif u'卖家已发货' in status:
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'] + '已发货订单号:' + i + '\n')
                    elif u'交易成功' in status:
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'] + '已完成订单号:' + i + '\n')
                    elif u'资金保护中' in status:
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'] + '资金保订单号:' + i + '\n')
                else:
                    driver.find_element_by_id('flag')
                    href = page.find_all(id='flag')[0].get('href')
                    driver.get(tb + href)
                    time.sleep(1)
                    if u'买家已付款' in status:    
                        driver.find_element_by_id('flag1').click()
                        time.sleep(0.5)
                        for cc in color['list']:
                            if cc.encode('utf-8') in tr['title']:
                                colorCount[cc] = colorCount[cc] + 1
                                driver.find_element_by_id('memo').send_keys(u'送' + cc)
                                break
                        time.sleep(0.5)
                        driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
                        time.sleep(0.5)
                        driver.switch_to_alert().accept()
                        time.sleep(0.5)
                        if verify(driver, skhost + tr['passlink'], i, True):
                            count[title + tr['passlink']] = count[title + tr['passlink']] + 1
                            countSum[title] = countSum[title] + 1
                            
                            if title not in everyDay[orderTime[0:10]]['sum'].keys():
                                everyDay[orderTime[0:10]]['sum'][title] = 0
                                everyDay[orderTime[0:10]]['count'][title + tr['passlink']] = 0
                            
                            everyDay[orderTime[0:10]]['sum'][title] = everyDay[orderTime[0:10]]['sum'][title] + 1
                            everyDay[orderTime[0:10]]['count'][title + tr['passlink']] = everyDay[orderTime[0:10]]['count'][title + tr['passlink']] + 1
                            everyDay[orderTime[0:10]]['order'].append('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '订单号：' + i.encode('utf-8'))   
                            out1.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '订单号：' + i.encode('utf-8') + '\n')
                        
                    if u'等待买家付款' in status:
                        driver.find_element_by_id('flag1').click()
                        time.sleep(0.5)
                        driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
                        time.sleep(0.5)
                        driver.switch_to_alert().accept()
                        time.sleep(0.5)
                    out2.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '订单号：' + i.encode('utf-8') + '\n')
            else:
                if verify(driver, skhost + tr['passlink'], i, True):
                    print u'订单错误'
    
    for i in count:
        if  count[i] > 0:
            out1.write(i.encode('utf-8') + ':' + str(count[i]).encode('utf-8') + '\n')
    for i in countSum:
        if  countSum[i] > 0:
            out1.write(i.encode('utf-8') + ':' + str(countSum[i]).encode('utf-8') + '\n')
    out3.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
    for i in everyDay:
        out3.write(i.encode('utf-8') + '\n')
        for j in everyDay[i]['order']:
            out3.write(j + '\n')
        
        for k in everyDay[i]['count']:
            if everyDay[i]['count'][k] > 0:
                out3.write(k.encode('utf-8') + ':' + str(everyDay[i]['count'][k]) + '\n')
        
        for l in everyDay[i]['sum']:
            if everyDay[i]['sum'][l] > 0:
                out3.write(l.encode('utf-8') + ':' + str(everyDay[i]['sum'][l]) + '\n')
    
    out3.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
            
    out.close()
    out1.close()
    out2.close()    
    out3.close()
    
