# coding=utf-8
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
import time
import math
import os, sys
import datetime
import sktb, sqlite


skhost = 'http://user.shikee.com'
state = '?state[]=&state[]=&state[]=&report_state[]=&trade_state[]=2&key=&trade_no='
tbhost = 'https://trade.taobao.com/trade/itemlist/list_sold_items.htm'
tb = 'https://trade.taobao.com'

style = 'height:17px;width:1px;padding-left:17px;overflow:hidden;vertical-align:middle;font-size:0px;display:inline-block;visibility:visible;background:url(//img.alicdn.com/tps/i1/TB1heyGFVXXXXXpXXXXR3Ey7pXX-550-260.png) no-repeat -100px -207px;'

def getOrderNumber(driver, trs, account):
    cont = sqlite.DataBaseControl()
    outx = open(account + u'/order_data.txt', 'a')
    outx.write('开始获取订单:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    print u'开始获取订单:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    a = time.time()
    result = []
    count = 0
    for tr in trs:
        link = tr['link'].replace('look_wait_join_list', 'look_pass_join_list')
        driver.get(skhost + link + '/0' + state)
        time.sleep(0.1)
        source = BeautifulSoup(driver.page_source)
        if sktb.is_element_exist(driver, '#total'):
            total = int(driver.find_element_by_id('total').text)
            n = int(math.ceil(total / 10.0))
        else:
            n = 1
        if len(source.find_all(id='load_list')) == 0:
            continue
        aaa = source.find_all(id='load_list')[0].find_all('tr')
        if len(aaa) == 2:
            continue
        order = []
        for i in range(0, n):
            driver.get(skhost + link + '/' + str(i * 10) + state)
            time.sleep(0.5)
            soup = BeautifulSoup(driver.page_source).find_all(id='load_list')[0].find_all('tr')
            Len = len(soup)
            if Len > 2:
                for j in range(1, Len - 1):
                    count = count + 1
                    order_num = ''.join(soup[j].find_all(class_='trade_number')[0].text.split())
                    order.append(order_num)
                    obj = {'title':tr['title'], 'link':link.encode('utf-8'), 'order_num':order_num.encode('utf-8'), 'time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'account':account.encode('utf-8')}
                    dborder = cont.getOrder(account.encode('utf-8'), order_num.encode('utf-8'))
                    if len(dborder) == 1:
                        obj['id'] = dborder[0]['id']
                        cont.saveOrder(obj, 1)
                    else:
                        cont.saveOrder(obj, 0)
        tr['passlink'] = link
        tr['order'] = order
        result.append(tr)
    cont.close()
    b = time.time()
    
    outx.write('一共 ' + str(count) + '订单\n')
    for i in result:
        outx.write(str(i['order']).encode('utf-8') + '\n')
    print u'结束获取订单:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print u'获取所有任务需要审核的订单的时间为：', b - a
    print u'一共：', count
    outx.write('结束获取订单:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    outx.close()
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
        time.sleep(1)
    except:
        return False
    return True

def addRemarks(driver, trs, color):
    if len(color['list']) == 0:
        return False
    
    conn = sqlite.DataBaseControl()
    if not os.path.exists(color['account']):
        os.makedirs(color['account'])
        fp = open(color['account'] + '/' + color['tbuser'].replace(u':', u'：'), 'w')
        fp.write('1')
        fp.close()
    
    process = open(color['account'] + u'/process_error.txt', 'a')
    out = open(color['account'] + u'/error.txt', 'a')
    out1 = open(color['account'] + u'/remark.txt', 'a')
    out2 = open(color['account'] + u'/flag.txt', 'a')
    out3 = open(color['account'] + u'/count.txt', 'a')
    out4 = open(color['account'] + u'/loaddata_time.txt', 'a')
    text = '开始获取订单:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
    out4.write('开始获取订单:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    trs = getOrderNumber(driver, trs, color['account'])
    text = text + '结束获取订单:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
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
    process.write('-----' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    orderlen = 0
    for tr in trs:
        orderlen = orderlen + len(tr['order'])
        title = ''.join(tr['title'][0:3].split())
        if len(title) == 2:
            title = title[0] + '0' + title[1]
        count[title + tr['passlink']] = 0
        for i in tr['order']:
            try:
                driver.get(tbhost)
            except:
                print u'打开淘宝搜索订单存在问题，尝试第二次打开'
                time.sleep(2)
                driver.get(tbhost)
            time.sleep(2)
            error_count = 0
            try:
                driver.find_element_by_id('bizOrderId').send_keys(i)
                time.sleep(1.5)
                driver.find_element_by_xpath('//*[@id="sold_container"]/div/div[1]/div[1]/form/div[7]/div/div/button[1]').click()
                time.sleep(1.5)
            except:
                error_count = error_count + 1
            if error_count == 1:
                try:
                    driver.find_element_by_id('bizOrderId')
                    time.sleep(1)
                    driver.find_element_by_css_selector('button.button-mod__button___2JAs3.button-mod__primary___3N5o1').click()
                except:
                    process.write('136-139行错误，跳过了订单：' + i.encode('utf-8') + '\n')
                    continue
            soup = BeautifulSoup(driver.page_source)
            page = soup.find_all(attrs={"data-reactid": ".0.5"})[0]
            div = page.find_all(class_='suborder-mod__order-table___2SEhF')
            llen = len(div)
            if llen > 0:
                di1 = page.find_all(class_='item-mod__trade-order___2LnGB')
                orderTime = di1[0].find_all('label')[0].find_all('span')[5].text
                if orderTime[0:10] not in everyDay.keys():
                    everyDay[orderTime[0:10]] = {'sum':{}, 'order':[], 'count':{}}
                td = div[0].find_all('td')
                status = td[5].text
                caveat = ''.join(td[3].text.split())
                if caveat != '' and caveat != u'退款关闭':
                    if u'买家已付款' in status:
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '已付款订单号:' + i + '\n')
                    elif u'卖家已发货' in status:
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '已发货订单号:' + i + '\n')
                    elif u'交易成功' in status:
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '已完成订单号:' + i + '\n')
                    elif u'资金保护中' in status:
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '资金保订单号:' + i + '\n')
                    elif u'交易关闭' in status:
                        if verify(driver, skhost + tr['passlink'], i, False):
                            print 'error-----------'
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '退款成功且交易关闭单号:' + i + '\n')
                else:
                    href = page.find_all(id='flag')[0].get('href')
                    driver.get(tb + href)
                    time.sleep(2)
                    if u'买家已付款' in status:                        
                        obj = {'taskId':title, 'title':tr['title'], 'link':tr['passlink'], 'order_num':i, 'time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'account':color['account'], 'tbuser':color['tbuser']}   
                        driver.find_element_by_id('flag1').click()
                        time.sleep(1)
                        driver.find_element_by_id('flag1').click()
                        FLAG = False
                        for cc in color['list']:
                            if cc.encode('utf-8').upper() in tr['title'].upper():
                                colorCount[cc] = colorCount[cc] + 1
                                driver.find_element_by_id('memo').clear()
                                driver.find_element_by_id('memo').send_keys(u'送' + cc)
                                FLAG = True
                                break
                        time.sleep(1)
                        try:
                            driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
                        except:
                            process.write('190行错误，跳过了订单：' + i.encode('utf-8') + '\n')
                            continue
                        time.sleep(1)
                        driver.switch_to_alert().accept()
                        time.sleep(1)
                        conn.saveRemark(obj, 0)
                        if verify(driver, skhost + tr['passlink'], i, True):
                            conn.saveRemark(obj, 1)
                            count[title + tr['passlink']] = count[title + tr['passlink']] + 1
                            countSum[title] = countSum[title] + 1
                            if title not in everyDay[orderTime[0:10]]['sum'].keys():
                                everyDay[orderTime[0:10]]['sum'][title] = 0
                            if (title + tr['passlink']) not in everyDay[orderTime[0:10]]['count']:
                                everyDay[orderTime[0:10]]['count'][title + tr['passlink']] = 0
                            everyDay[orderTime[0:10]]['sum'][title] = everyDay[orderTime[0:10]]['sum'][title] + 1
                            everyDay[orderTime[0:10]]['count'][title + tr['passlink']] = everyDay[orderTime[0:10]]['count'][title + tr['passlink']] + 1
                            everyDay[orderTime[0:10]]['order'].append('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '订单号：' + i.encode('utf-8'))   
                            out1.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '订单号：' + i.encode('utf-8') + '\n')
                            if not FLAG:
                                out1.write('订单号：' + i.encode('utf-8') + '审核过了但没备注\n')
                    if u'等待买家付款' in status:
                        try:
                            driver.find_element_by_id('flag1').click()
                            time.sleep(1)
                            driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
                            time.sleep(1)
                            driver.switch_to_alert().accept()
                            time.sleep(1)
                        except:
                            continue
                    if u'交易关闭' in status:
                        if verify(driver, skhost + tr['passlink'], i, False):
                            print u'订单错误'
                        out.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '交易关闭单号:' + i + '\n')
                    out2.write('活动 ' + title + ' 链接：' + tr['passlink'].encode('utf-8') + '订单号：' + i.encode('utf-8') + '\n')
            else:
                if verify(driver, skhost + tr['passlink'], i, False):
                    print u'订单错误'
    conn.close()
    process.write('-----' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    process.close()
    for i in count:
        if  count[i] > 0:
            out1.write(i.encode('utf-8') + ':' + str(count[i]).encode('utf-8') + '\n')
    for i in countSum:
        if  countSum[i] > 0:
            out1.write(i.encode('utf-8') + ':' + str(countSum[i]).encode('utf-8') + '\n')
    out3.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
    out3.write(text)
    out3.write('一共获取了：' + str(orderlen) + '订单\n')
    for i in everyDay:
        out3.write(i.encode('utf-8') + '\n')
        for j in everyDay[i]['order']:
            out3.write(j + '\n')
        kk = sorted(everyDay[i]['count'].keys())
        for k in kk:
            if everyDay[i]['count'][k] > 0:
                out3.write(k.encode('utf-8') + ':' + str(everyDay[i]['count'][k]) + '\n')
        ll = sorted(everyDay[i]['sum'].keys())
        for l in ll:
            if everyDay[i]['sum'][l] > 0:
                out3.write(l.encode('utf-8') + ':' + str(everyDay[i]['sum'][l]) + '\n')
    
    out3.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
            
    out.close()
    out1.close()
    out2.close()    
    out3.close()

def correct_verify(driver, url, order, flag):
    try:
        driver.get(url)
        time.sleep(1)
        driver.find_element_by_id('orderNumber').send_keys(order)
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="key_from"]/input[3]').click()
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source)
        text = soup.find_all(class_='trade_state_msg')[0].text
        if u'订单号正确' in text:
            return False
        driver.find_element_by_xpath('//*[@id="load_list"]/table/tbody/tr[2]/td[5]/a[2]').click()
        time.sleep(1)
        if flag:
            driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[2]/td[3]/input[2]').click()
        else:
            driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[2]/td[3]/input[3]').click()
        time.sleep(0.5)
        driver.find_element_by_id('sub_trade_number').click()
        time.sleep(1)
    except:
        return False
    return True

def correct(driver, color):
    conn = sqlite.DataBaseControl()
    orders = conn.getRemarks(color['account'])
    conn.close()
    driver.get(tbhost)
    if not os.path.exists(color['account']):
        os.makedirs(color['account'])
        fp = open(color['account'] + '/' + color['tbuser'].replace(u':', u'：'), 'w')
        fp.write('1')
        fp.close()
    
    out = open(color['account'] + u'/rectify_order.txt', 'a')
    out.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
    for order in orders:
        driver.find_element_by_id('bizOrderId').clear()
        driver.find_element_by_id('bizOrderId').send_keys(order['order'])
        time.sleep(1.5)
        driver.find_element_by_css_selector('button.button-mod__button___2JAs3.button-mod__primary___3N5o1').click()
        time.sleep(1.5)
        soup = BeautifulSoup(driver.page_source)
        page = soup.find_all(attrs={"data-reactid": ".0.5"})[0]
        div = page.find_all(class_='suborder-mod__order-table___2SEhF')
        if len(div) == 0:
            continue
        i = page.find_all(id='flag')[0].find_all(attrs={"style": style})
        if len(i) == 0:
            out.write('重新备注订单：' + order['order'].encode('utf-8') + '\n')
            td = div[0].find_all('td')
            status = td[5].text
            href = page.find_all(id='flag')[0].get('href')
            driver.get(tb + href)
            time.sleep(1.5)
            driver.find_element_by_id('flag1').click()
            time.sleep(1)
            driver.find_element_by_id('flag1').click()
            if u'买家已付款' in status:
                for cc in color['list']:
                    if cc.upper() in order['title'].upper():
                        driver.find_element_by_id('memo').clear()
                        driver.find_element_by_id('memo').send_keys(u'送' + cc)
                        break
                time.sleep(0.5)
            try:
                driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
            except:
                continue
            time.sleep(1)
            driver.switch_to_alert().accept()
            if u'买家已付款' in status:
                correct_verify(driver, skhost + order['link'], order['order'], True)
            driver.get(tbhost)
            time.sleep(0.5)
    out.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
    out.close()


def artificial_verify(driver, order, FLAG):
    try:
        driver.get('http://user.shikee.com/seller/tryings/try_list/')
        time.sleep(0.5)
        select = Select(driver.find_element_by_name('search_type'))
        select.select_by_value('order_id')
        time.sleep(0.5)
        driver.find_element_by_id('key').clear()
        driver.find_element_by_id('key').send_keys(order)
        time.sleep(0.5)
        driver.find_element_by_id('go_search').click()
        time.sleep(0.5)
        
        page = BeautifulSoup(driver.page_source)
        table = page.find_all(id='search_order')[0]
        trs = table.find_all('tr')
        td = trs[1].find_all('td')
        title = td[0].text                
        driver.find_element_by_id('J_checkno').click()
        time.sleep(0.5)
        if FLAG:      
            driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[2]/td[3]/input[2]').click()
        else:            
            driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/form/table/tbody/tr[2]/td[3]/input[3]').click()            
        time.sleep(0.5)
        driver.find_element_by_id('asub_trade_number').click()
        time.sleep(1)
    except:
        return ''
    return title
    

def artificial(driver, orders, color):
    if not os.path.exists(color['account']):
        os.makedirs(color['account'])
        fp = open(color['account'] + '/' + color['tbuser'].replace(u':', u'：'), 'w')
        fp.write('1')
        fp.close()
    
    out = open(color['account'] + u'/artificial_order.txt', 'a')
    error = open(color['account'] + u'/artificial_error.txt', 'a')
    out.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
    error.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
    try:
        count = {}
        skcount = {}
        for order in orders:
            driver.get(tbhost)
            driver.find_element_by_id('bizOrderId').clear()
            driver.find_element_by_id('bizOrderId').send_keys(order)
            time.sleep(1.5)
            driver.find_element_by_css_selector('button.button-mod__button___2JAs3.button-mod__primary___3N5o1').click()
            time.sleep(1.5)
            soup = BeautifulSoup(driver.page_source)
            page = soup.find_all(attrs={"data-reactid": ".0.5"})[0]
            div = page.find_all(class_='suborder-mod__order-table___2SEhF')
            llen = len(div)
            if llen > 0:
                td = div[0].find_all('td')
                status = td[5].text
                caveat = ''.join(td[3].text.split())
                if caveat != '' and caveat != u'退款关闭':
                    if u'买家已付款' in status:
                        out.write(caveat.encode('utf-8') + '已付款订单号:' + order + '\n')
                    elif u'卖家已发货' in status:
                        out.write(caveat.encode('utf-8') + '已发货订单号:' + order + '\n')
                    elif u'交易成功' in status:
                        out.write(caveat.encode('utf-8') + '已完成订单号:' + order + '\n')
                    elif u'资金保护中' in status:
                        out.write(caveat.encode('utf-8') + '资金保订单号:' + order + '\n')
                    elif u'交易关闭' in status:
                        if verify(driver, skhost + tr['passlink'], order, False):
                            print 'error-----------'
                        out.write(caveat.encode('utf-8') + '退款成功且交易关闭单号:' + order + '\n')
                else:
                    href = page.find_all(id='flag')[0].get('href')
                    if u'买家已付款' in status:
                        title = artificial_verify(driver, order, True)
                        if title == '':
                            out.write('427行错误，跳过了订单：' + order.encode('utf-8') + '\n\n')
                            continue
                        
                        title_text = ''.join(title[0:3].split())
                        if len(title_text) == 2:
                            title_text = title_text[0] + '0' + title_text[1]
                        count[title_text] = 0
                        skcount[title_text] = 0
                        
                        out.write('活动标题：' + title.encode('utf-8') + '，订单号：' + order.encode('utf-8') + '\n')
                        
                        out.write('联盟通过了\n')
                        skcount[title_text] = skcount[title_text] + 1
                        driver.get(tb + href)
                        time.sleep(1)
                        driver.find_element_by_id('flag1').click()
                        time.sleep(1)
                        driver.find_element_by_id('flag1').click()
                        FLAG = False
                        for cc in color['list']:
                            if cc.upper() in title.upper():
                                driver.find_element_by_id('memo').clear()
                                driver.find_element_by_id('memo').send_keys(u'送' + cc)
                                FLAG = True
                                break
                        time.sleep(1)
                        try:
                            driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
                        except:
                            out.write('445行错误，跳过了订单：' + order.encode('utf-8') + '\n\n')
                            continue
                        time.sleep(1)
                        driver.switch_to_alert().accept()
                        time.sleep(1)
                        if FLAG:
                            out.write('淘宝备注了订单\n\n')
                        else:
                            out.write('淘宝插旗了订单\n\n')
                        count[title_text] = count[title_text] + 1
                    if u'等待买家付款' in status:
                        try:
                            driver.find_element_by_id('flag1').click()
                            time.sleep(1)
                            driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[3]/td/div/button').click()
                            time.sleep(1)
                            driver.switch_to_alert().accept()
                            time.sleep(1)
                            out.write('等待买家付款的单号:' + order.encode('utf-8') + '\n\n')
                        except:
                            continue
                    if u'交易关闭' in status:
                        title = artificial_verify(driver, order, False)
                        out.write('交易关闭单号:' + order.encode('utf-8') + '\n\n')
            else:
                title = artificial_verify(driver, order, False)
                out.write('淘宝没找到单号:' + order.encode('utf-8') + '\n\n')
        out.write('联盟审核统计\n')
        cc = sorted(skcount.keys())
        for i in cc:
            out.write(i.encode('utf-8') + '：' + str(skcount[i]) + '\n')
        out.write('淘宝备注统计\n')    
        cc = sorted(count.keys())
        for i in cc:
            out.write(i.encode('utf-8') + '：' + str(count[i]) + '\n')
        
    
    except Exception, e:
        error.write(str(sys.exc_info()[2].tb_lineno) + e.message + '\n')
    out.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
    error.write('--------------' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '--------------\n')
    out.close()
    error.close()
