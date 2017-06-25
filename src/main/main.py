# coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
Tusername = u'starry_sky品牌企业店:盘满钵满'
Tpassword = 'qqh983468869'
Susername = '13794728078'
Spassword = 'kyd0920'
# driver=webdriver.PhantomJS(executable_path='phantomjs.exe')
TUrl = 'https://trade.taobao.com/trade/itemlist/list_sold_items.htm?spm=a313o.7775905.a1zvx.d28.IiB2I1&mytmenu=ymbb'
SUrl = 'http://user.shikee.com/seller/tryings/try_list/'
driver = webdriver.Chrome()

def page(n):
	if n % 10 == 0:
		return n / 10
	else:
		return n / 10 + 1

def is_element_exist(css):
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

def loginTaobao():
	driver.get('https://login.taobao.com/member/login.jhtml')
	if is_element_exist('.module-quick'):
		driver.find_element_by_id('J_Quick2Static').click()
	time.sleep(4)
	driver.find_element_by_id('TPL_username_1').send_keys(Tusername)
	time.sleep(4)
	driver.find_element_by_id('TPL_password_1').send_keys(Tpassword)

	if is_element_exist('#nc_1_n1z'):
		print "huakuai"
		actions = ActionChains(driver)
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
def loginShikee():
	driver.get('http://login.shikee.com/')
	time.sleep(5)
	driver.find_element_by_xpath('//i[@class="iconimg pc"]').click()
	driver.find_element_by_xpath('//input[@id="J_userName"]').send_keys(Susername)
	driver.find_element_by_xpath('//input[@id="J_pwd"]').send_keys(Spassword)
	time.sleep(2)
	driver.find_element_by_xpath('//input[@id="J_submit"]').click()
	time.sleep(5)
def saveTryList():
	driver.get(SUrl)
	time.sleep(5)
	driver.find_element_by_id('chebox3').click()
	driver.find_element_by_id('chebox4').click()
	time.sleep(3)
	soup = BeautifulSoup(driver.page_source)
	total = int(soup.find_all(id='total')[0].text)

if __name__ == '__main__':
	total = 97;
	print page(total)
