# -*- coding: UTF-8 -*-

from selenium import webdriver
from PyQt4 import QtCore, QtGui
import ui
import sys, os
import time
import sktb
import review
import user
import debug
import thread

class window(QtGui.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = ui.Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.initTable()
        self.ui.initOrderTable()
        self.ui.initGiftTable()
        
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.tableNumber = 0
        self.tableNumber1 = 0
        self.tableorder = 0
        self.initButton()
        self.initDriver()
        # self.AUTOLogin = False
        # self.ui.TaobaoUserName.setText(u'tb22765774:毛毛') 
        # self.ui.ShikeeUserName.setText('18814726078')
        self.ui.InvalidOrders.setText('')
        self.ui.AverageTime.setText('')
        self.ui.Total.setText('')
        self.ui.TrialsNumber.setText('')
        self.ui.AbandonNumber.setText('')
        self.ui.Number.setText('')
        self.ui.ViolationsNumber.setText('')
        
        # now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.fromString(now_time, 'yyyy-MM-dd hh:mm:ss'))
        # print str(self.ui.dateTimeEdit.dateTime())
        
        self.ui.Browser.insertItem(0, 'chrome')
        self.ui.Browser.insertItem(1, 'firefox')
        # self.ui.Browser.insertItem(2, 'ie')
        self.initAccount()
    
    def closeEvent(self, event):
        event.accept()

    def initButton(self):
        self.ui.AddActivity.clicked.connect(self.addActive)
        self.ui.GetShikeeData.clicked.connect(self.getShikeeData)
        self.ui.resetActivity.clicked.connect(self.clearActive)
        self.ui.ExecuteActivity.clicked.connect(self.executeActivity)
        self.ui.clearLink.clicked.connect(self.deleteTryList)
        self.ui.addGift.clicked.connect(self.addGift)
        self.ui.resetGift.clicked.connect(self.clearGift)
        self.ui.executeRemarks.clicked.connect(self.executeRemarks)
        self.ui.autoLogin.clicked.connect(self.autoLogin)
        self.ui.rectifyRemarks.clicked.connect(self.rectifyRemarks)
        self.ui.addOrder.clicked.connect(self.addOrder)
        self.ui.resetOrder.clicked.connect(self.clearOrder)
        self.ui.Execute0.clicked.connect(self.artificial)
        self.ui.openBrowser.clicked.connect(self.openBrowser)
        self.ui.closeBrowser.clicked.connect(self.closeBrowser)
    
    
    def account_cmp(self, a, b):
        return cmp(a['tbusername'], b['tbusername']) * -1
    def initAccount(self):
        temp = user.listAccount()
        self.account = sorted(temp, cmp=self.account_cmp)
        for account in self.account:
            self.ui.Account.addItem(account['tbusername'])
    
    def getAccount(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        for account in self.account:
            if name == account['tbusername']:
                user = account
                break
        return user
    
    def initDriver(self):
        self.orders = []
        self.taskList = []
        self.giftList = []
        self.try_list = []
        #self.driver = []
        self.driverCount = 0 
        
    def openBrowser(self):
        # thread.start_new_thread(test, ())  
        browser = str(self.ui.Browser.currentText())
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
            #self.driver.append(driver)
            self.driverCount = self.driverCount + 1
            self.ui.BrowserNumber.addItem(str(self.driverCount))
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
            #self.driver.append(driver)
            self.driverCount = self.driverCount + 1
            self.ui.BrowserNumber.addItem(str(self.driverCount))
        elif browser == 'ie':
            self.driver = webdriver.Ie()
            #self.driver.append(driver)
            self.driverCount = self.driverCount + 1
            self.ui.BrowserNumber.addItem(str(self.driverCount))
    def closeBrowser(self):
        index = self.ui.BrowserNumber.currentIndex()
        browser = int(str(self.ui.BrowserNumber.currentText()))
        #self.driver[browser - 1].close()
        #self.ui.BrowserNumber.removeItem(index)
            
    def addOrder(self):
        order = self.ui.orderLine.text()
        self.orders.append(unicode(order.toUtf8(), 'utf-8', 'ignore'))
        self.ui.orderModel.setItem(self.tableorder, 0, QtGui.QStandardItem(order))
        self.ui.orderTable.setModel(self.ui.orderModel)
        self.tableorder = self.tableorder + 1
    def clearOrder(self):
        self.tableorder = 0
        self.orders = []
        self.ui.orderModel.removeRows(0, self.ui.orderModel.rowCount())
        self.ui.orderTable.setModel(self.ui.orderModel)
        self.ui.initOrderTable()
        
    def autoLogin(self):
        #browser = int(str(self.ui.BrowserNumber.currentText()))
        #driver = self.driver[browser - 1]
        # tname = unicode(self.ui.TaobaoUserName.text().toUtf8(), 'utf-8', 'ignore')
        # sname = unicode(self.ui.ShikeeUserName.text().toUtf8(), 'utf-8', 'ignore')
        # obj = {'su':sname, 'tu':tname}
        # account = user.getAccount(obj)
        
        self.Account = self.getAccount()
        if user.autoLogin(self.driver, self.Account):
            QtGui.QMessageBox.information(self, u'登录提示', u'登录成功')
        else:
            QtGui.QMessageBox.critical(self, u'登录提示', u'登录失败 ')
        # self.AUTOLogin = True
        


    def addActive(self):
        a = self.ui.ActivityNumber.text()
        b = self.ui.PeopleNumber.text()
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.ui.model.setItem(self.tableNumber, 0,
                              QtGui.QStandardItem(ui._fromUtf8(a)))
        self.ui.model.setItem(self.tableNumber, 1,
                              QtGui.QStandardItem(ui._fromUtf8(b)))
        self.ui.model.setItem(self.tableNumber, 2, QtGui.QStandardItem(t))
        self.tableNumber = self.tableNumber + 1
        self.ui.tableView.setModel(self.ui.model)
        self.taskList.append(
            {'name': str(a).upper(), 'num': int(b), 'time': t})

    def clearActive(self):
        self.taskList = []
        self.tableNumber = 0
        self.ui.model.removeRows(0, self.ui.model.rowCount())
        self.ui.tableView.setModel(self.ui.model)
        self.ui.initTable()

    def getShikeeData(self):
        #browser = int(str(self.ui.BrowserNumber.currentText()))
        #driver = self.driver[browser - 1]
        self.try_list 
        res = sktb.saveActiveList(self.driver)
        if res[1]:
            self.try_list = res[0]
            self.try_list.sort(key=lambda obj: obj.get('time'), reverse=True)    
            QtGui.QMessageBox.information(self, u'获取试客活动数据提示', u'获取数据成功')
        else:
            QtGui.QMessageBox.critical(self, u'获取试客活动数据提示', u'获取数据失败')

    def deleteTryList(self):
        url = str(self.ui.Link.text())
        for t in self.try_list:
            if t['link'] in url:
                self.try_list.remove(t)
                break

    def addGift(self):
        gift = self.ui.Gift.text()
        
        self.giftList.append(unicode(gift.toUtf8(), 'utf-8', 'ignore'))
        self.ui.giftmodel.setItem(self.tableNumber1, 0,
                              QtGui.QStandardItem(unicode(gift.toUtf8(), 'utf-8', 'ignore')))
        self.tableNumber1 = self.tableNumber1 + 1
    def clearGift(self):
        self.giftList = []
        self.tableNumber1 = 0
        self.ui.giftmodel.removeRows(0, self.ui.model.rowCount())
        self.ui.GiftTable.setModel(self.ui.giftmodel)
        self.ui.initGiftTable()

    
    def executeActivity(self):
        #browser = int(str(self.ui.BrowserNumber.currentText()))
        #driver = self.driver[browser - 1]
        trialsNumber = self.ui.TrialsNumber.text()  # 近30日获得试用次数
        number = self.ui.Number.text()  # 近30天下单次数
        
        invalidOrders = self.ui.InvalidOrders.text()  # 无效订单次数
        averageTime = self.ui.AverageTime.text()  # 填写订单号平均时长
        total = self.ui.Total.text()  # 参与试用总次数
        
        abandonNumber = self.ui.AbandonNumber.text()  # 放弃试用次数
        
        violationsNumber = self.ui.ViolationsNumber.text()  # 违规次数
        days = self.ui.Days.text()
        bilv = self.ui.Days_2.text()
        # account = self.ui.ShikeeUserName.text()
        # name = self.ui.TaobaoUserName.text()
        # if self.AUTOLogin:
        res = {'bilv':str(bilv), 'invalidOrders': str(invalidOrders), 'averageTime': str(averageTime), 'total': str(total), 'trialsNumber': str(trialsNumber), 'abandonNumber': str(abandonNumber), 'number': str(number), 'violationsNumber': str(violationsNumber), 'days': str(days), 'account':self.Account['skusername'], 'tbuser':self.Account['tbusername']}
        
        if sktb.executeActivity(self.driver, self.try_list, self.taskList, res):
            QtGui.QMessageBox.information(self, u'通过结果提示', u'通过完成')
        else:
            QtGui.QMessageBox.critical(self, u'通过结果提示', u'过程出错')
    
    def executeRemarks(self):
        #browser = int(str(self.ui.BrowserNumber.currentText()))
        #driver = self.driver[browser - 1]
        # account = self.ui.ShikeeUserName.text()
        # name = self.ui.TaobaoUserName.text()
        # if self.AUTOLogin:
        color = {'list':self.giftList, 'account':self.Account['skusername'], 'tbuser':self.Account['tbusername']}
        
        if review.addRemarks(self.driver, self.try_list, color):
            QtGui.QMessageBox.information(self, u'备注结果提示', u'备注完成')
        else:
            QtGui.QMessageBox.critical(self, u'备注结果提示', u'过程出错')
        
    def rectifyRemarks(self):
        #browser = int(str(self.ui.BrowserNumber.currentText()))
        #driver = self.driver[browser - 1]
        try:
            color = {'list':self.giftList, 'account':self.Account['skusername'], 'tbuser':self.Account['tbusername']}
            if self.ui.allData.isChecked():
                if review.correct(self.driver, color, True):
                    QtGui.QMessageBox.information(self, u'纠正全部备注提示', u'纠正完成')
                else:
                    QtGui.QMessageBox.critical(self, u'纠正全部备注提示', u'过程出错')
            elif self.ui.partData.isChecked():
                if review.correct(self.driver, color, False):
                    QtGui.QMessageBox.information(self, u'纠正部分备注提示', u'纠正完成')
                else:
                    QtGui.QMessageBox.critical(self, u'纠正部分备注提示', u'过程出错')
        except Exception, e:
            info = sys.exc_info()
            debug.log(str(sys.exc_info()[2].tb_lineno), e.message, info[1], os.path.basename(__file__))
            
    def artificial(self):
        #browser = int(str(self.ui.BrowserNumber.currentText()))
        #driver = self.driver[browser - 1]
        # account = self.ui.ShikeeUserName.text()
        # name = self.ui.TaobaoUserName.text()
        # if self.AUTOLogin:
        color = {'list':self.giftList, 'account':self.Account['skusername'], 'tbuser':self.Account['tbusername']}
        
        if review.artificial(self.driver, self.orders, color):
            QtGui.QMessageBox.information(self, u'手动添加订单备注提示', u'备注完成')
        else:
            QtGui.QMessageBox.critical(self, u'手动添加订单备注提示', u'过程出错')
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())
