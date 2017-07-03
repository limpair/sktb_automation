# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import time, math, re
import datetime

driver = webdriver.Chrome('../driver/chromedriver.exe')
driver.get('http://login.shikee.com/')
driver.find_element_by_xpath('//i[@class="iconimg pc"]').click()
driver.find_element_by_xpath('//input[@id="J_userName"]').send_keys('13794728078')
driver.find_element_by_xpath('//input[@id="J_pwd"]').send_keys('kyd0920')
time.sleep(1)
driver.find_element_by_xpath('//input[@id="J_submit"]').click()

time.sleep(1)
driver.get('http://user.shikee.com/seller/tryings/try_list/0/?key=&search_type=try_name&state[]=3&state[]=4&is_block=&check_fail=&wait_check_out=')

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
		num = int(re.sub("\D", "", t[4].text)) 
		link = t[6].find_all('a')[0].attrs['href'].split('?')[0]
		li[link] = {'title':title, 'num':num, 'link':link}
		

	loadlist = {}
	driver.get('http://user.shikee.com' + link)
	time.sleep(1)
	looktotal = int(driver.find_element_by_id('total').text)
	lookn = int(math.ceil(total / 10.0))
	for a in range(0, lookn):
		driver.get('http://user.shikee.com' + link + str(a * 20))
		time.sleep(1)
		soupp = BeautifulSoup(driver.page_source).find_all(id='load-buyer-list')[0].find_all('tr')
		kk = len(soupp)
		for b in range(1, kk):
			time.sleep(1.5)
			rows = soupp[b].attrs['id'].split('_')[1]
			driver.find_element_by_xpath("//div[@data-uid='" + rows + "']").click()
		time.sleep(1.5)
		soupp = BeautifulSoup(driver.page_source).find_all(id='load-buyer-list')[0].find_all('tr')
		
		for b in range(1, kk):
			rows = soupp[b].attrs['id'].split('_')[1]
			t = soupp[b].find_all('td')
			sp = t[3].find_all('span')
			SP = {}
			for x in sp:
				temp = re.findall(r'(\w*[0-9]+)\w*', x.text)
				ss = x.text.split('(')[0]
				print ss
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
			loadlist['id'] = int(rows)
			loadlist['sys'] = SP
			loadlist['name'] = t[1].find_all('span')[0].attrs['title']
			loadlist['time'] = t[2].text
	
		# li[link] = {'title':title, 'num':num, 'link':link, 'user':loadlist}
print li
