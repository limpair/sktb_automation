#coding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime

driver=webdriver.PhantomJS(executable_path='C:\Users\Administrator\Desktop\phantomjs.exe')
driver.get('http://login.shikee.com/')
driver.find_element_by_xpath('//i[@class="iconimg pc"]').click()
driver.find_element_by_xpath('//input[@id="J_userName"]').send_keys('13794728078')
driver.find_element_by_xpath('//input[@id="J_pwd"]').send_keys('kyd0920')
time.sleep(1)
driver.find_element_by_xpath('//input[@id="J_submit"]').click()

time.sleep(1)
driver.get('http://user.shikee.com/seller/tryings/try_list/')

li={}

total=int(driver.find_element_by_id('total').text)
n=int(math.ceil(total/10.0))
listUrl='http://user.shikee.com/seller/tryings/try_list/'
search='?key=&search_type=try_name&state[]=3&state[]=4&is_block=&check_fail=&wait_check_out='
for i in range(0,n):
	driver.get(listUrl+str(i*10)+search)	
	time.sleep(2)
	soup = BeautifulSoup(driver.page_source).find_all(id='load_list')[0].find_all('tr')
	k=len(soup)
	for i in range(1,k-1):
		t=soup[i].find_all('td')
		#0,4,6
		title = t[0].find_all('img')[0].attrs['art'].encode('utf-8')
		num = re.sub("\D", "", t[4].text)
		link = t[6].find_all('a')[0].attrs['href'].split('?')[0]
		li[link] = {'title':title,'num':num,'link':link}

soup = BeautifulSoup(driver.page_source).find_all(id='load-buyer-list')[0].find_all('tr')
k=len(soup)
for i in range(1,k):
	time.sleep(1.5)
	rows=soup[i].attrs['id'].split('_')[1]
	driver.find_element_by_xpath("//div[@data-uid='"+rows+"']").click()
soup = BeautifulSoup(driver.page_source).find_all(id='load-buyer-list')[0].find_all('tr')
for i in range(1,k):
	rows=soup[i].attrs['id'].split('_')[1]
	t=soup[i].find_all('td')
	print t[0].find_all('span')[0].attrs['title']
	print t[3].find_all('span')