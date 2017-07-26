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
import threading

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
        self.ui.InvalidOrders.setText('')
        self.ui.AverageTime.setText('')
        self.ui.Total.setText('')
        self.ui.TrialsNumber.setText('')
        self.ui.AbandonNumber.setText('')
        self.ui.Number.setText('')
        self.ui.ViolationsNumber.setText('')
        self.ui.Browser.insertItem(0, 'chrome')
        self.ui.Browser.insertItem(1, 'firefox')
        self.initAccount()
        self.ids = []
    
    def closeEvent(self, event):
        event.accept()

    def initButton(self):
        self.ui.AddActivity.clicked.connect(self.addActive)
        self.ui.resetActivity.clicked.connect(self.clearActive)
        self.ui.clearLink.clicked.connect(self.deleteTryList)
        self.ui.addGift.clicked.connect(self.addGift)
        self.ui.resetGift.clicked.connect(self.clearGift)
        self.ui.addOrder.clicked.connect(self.addOrder)
        self.ui.resetOrder.clicked.connect(self.clearOrder)
        self.ui.openBrowser.clicked.connect(self.openBrowser)
        self.ui.closeBrowser.clicked.connect(self.closeBrowser)
        
        self.ui.autoLogin.clicked.connect(self.autoLogin)
        self.ui.GetShikeeData.clicked.connect(self.getShikeeData)
        self.ui.ExecuteActivity.clicked.connect(self.executeActivity)
        self.ui.executeRemarks.clicked.connect(self.executeRemarks)
        self.ui.rectifyRemarks.clicked.connect(self.rectifyRemarks)
        self.ui.Execute0.clicked.connect(self.artificial)
        self.ui.BrowserNumber.activated.connect(self.change)
        self.ui.approvedTimer.clicked.connect(self.approvedTimer)
        
        
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
    
    def getId(self):
        Id = {}
        n = int(str(self.ui.BrowserNumber.currentText()))
        for i in self.ids:
            if i['id'] == n:
                Id = i
                break
        return Id
    def setId(self, Id):
        idsLen = len(self.ids)
        for i in range(0, idsLen):
            if self.ids[i]['id'] == Id['id']:
                self.ids[i] = Id
                break
    
    def change(self):
        # index = self.ui.BrowserNumber.currentIndex()
        Id = {}
        n = int(str(self.ui.BrowserNumber.currentText()))
        for i in self.ids:
            if i['id'] == n:
                Id = i
                break
        if Id['browser'] == 'chrome':
            self.ui.Browser.setCurrentIndex(0)
        elif Id['browser'] == 'firefox':
            self.ui.Browser.setCurrentIndex(1)
        accountLen = len(self.account)
        
        for i in range(0, accountLen):
            if Id['account']['tbusername'] == self.account[i]['tbusername']:
                self.ui.Account.setCurrentIndex(i)
                break
        
        self.ui.initTable()
        self.ui.initGiftTable()
        self.ui.initOrderTable()
        
        tableLen = len(Id['tasks'])
        giftLen = len(Id['gifts'])
        ordersLen = len(Id['orders'])
        
        for i in range(0, tableLen):
            self.ui.model.setItem(i, 0, QtGui.QStandardItem(Id['tasks'][i]['name']))
            self.ui.model.setItem(i, 1, QtGui.QStandardItem(str(Id['tasks'][i]['num'])))
            self.ui.model.setItem(i, 2, QtGui.QStandardItem(Id['tasks'][i]['time']))
        
        for i in range(0, ordersLen):
            self.ui.orderModel.setItem(i, 0, QtGui.QStandardItem(Id['orders'][i]))
        
        for i in range(0, giftLen):
            self.ui.giftmodel.setItem(i, 0, QtGui.QStandardItem(Id['gifts'][i]))
        self.ui.orderTable.setModel(self.ui.orderModel)
        self.ui.tableView.setModel(self.ui.model)
        self.tableNumber = 0
        # self.giftList.append(unicode(gift.toUtf8(), 'utf-8', 'ignore'))
        # self.ui.giftmodel.setItem(self.tableNumber1, 0, QtGui.QStandardItem(unicode(gift.toUtf8(), 'utf-8', 'ignore')))
        
        
    def data(self):
        self.ids = []
        self.id = {'id':1, 'browser':'chrome', 'skdata':'list', 'tasks':'tasks', 'orders':'orders', 'gifts':'gift', 'account':'account'}
    def initDriver(self):
        self.orders = []
        self.taskList = []
        self.giftList = []
        self.try_list = []
        self.driver = []
        self.driverCount = 0 
        
    def openBrowser(self):
        # thread.start_new_thread(test, ())  
        browser = str(self.ui.Browser.currentText())
        if browser == 'chrome':
            driver = webdriver.Chrome()
            self.driver.append(driver)
            self.driverCount = self.driverCount + 1
            self.ui.BrowserNumber.addItem(str(self.driverCount))
            self.ids.append({'id':self.driverCount, 'driver':driver, 'browser':'chrome', 'skdata':[], 'tasks':[], 'orders':[], 'gifts':[], 'account':{'tbusername':''}})
        elif browser == 'firefox':
            driver = webdriver.Firefox()
            self.driver.append(driver)
            self.driverCount = self.driverCount + 1
            self.ui.BrowserNumber.addItem(str(self.driverCount))
            self.ids.append({'id':self.driverCount, 'driver':driver, 'browser':'firefox', 'skdata':[], 'tasks':[], 'orders':[], 'gifts':[], 'account':{'tbusername':''}})
        elif browser == 'ie':
            driver = webdriver.Ie()
            self.driver.append(driver)
            self.driverCount = self.driverCount + 1
            self.ui.BrowserNumber.addItem(str(self.driverCount))
    def closeBrowser(self):
        index = self.ui.BrowserNumber.currentIndex()
        browser = int(str(self.ui.BrowserNumber.currentText()))
        self.driver[browser - 1].close()
        self.ui.BrowserNumber.removeItem(index)
            
    def addOrder(self):
        Id = self.getId()
        order = self.ui.orderLine.text()
        self.orders.append(unicode(order.toUtf8(), 'utf-8', 'ignore'))
        self.ui.orderModel.setItem(self.tableorder, 0, QtGui.QStandardItem(order))
        self.ui.orderTable.setModel(self.ui.orderModel)
        self.tableorder = self.tableorder + 1
        Id['orders'].append(unicode(order.toUtf8(), 'utf-8', 'ignore'))
        self.setId(Id)
    def clearOrder(self):
        self.tableorder = 0
        self.orders = []
        self.ui.orderModel.removeRows(0, self.ui.orderModel.rowCount())
        self.ui.orderTable.setModel(self.ui.orderModel)
        self.ui.initOrderTable()
        Id = self.getId()
        Id['orders'] = []
        self.setId(Id)
    def addActive(self):
        
        Id = self.getId()
        
        a = self.ui.ActivityNumber.text()
        b = self.ui.PeopleNumber.text()
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        self.ui.model.setItem(self.tableNumber, 0, QtGui.QStandardItem(ui._fromUtf8(a)))
        self.ui.model.setItem(self.tableNumber, 1, QtGui.QStandardItem(ui._fromUtf8(b)))
        self.ui.model.setItem(self.tableNumber, 2, QtGui.QStandardItem(t))
        self.tableNumber = self.tableNumber + 1
        self.ui.tableView.setModel(self.ui.model)
        self.taskList.append({'name': str(a).upper(), 'num': int(b), 'time': t})
        Id['tasks'].append({'name': str(a).upper(), 'num': int(b), 'time': t})
        self.setId(Id)
    def clearActive(self):
        self.taskList = []
        self.tableNumber = 0
        self.ui.model.removeRows(0, self.ui.model.rowCount())
        self.ui.tableView.setModel(self.ui.model)
        self.ui.initTable()
        
        Id = self.getId()
        Id['tasks'] = []
        self.setId(Id)
        
    def deleteTryList(self):
        Id = self.getId()
        url = str(self.ui.Link.text())
        for t in Id['skdata']:
            if t['link'] in url:
                Id['skdata'].remove(t)
                break
        self.setId(Id)

    def addGift(self):
        gift = self.ui.Gift.text()
        self.giftList.append(unicode(gift.toUtf8(), 'utf-8', 'ignore'))
        self.ui.giftmodel.setItem(self.tableNumber1, 0, QtGui.QStandardItem(unicode(gift.toUtf8(), 'utf-8', 'ignore')))
        self.tableNumber1 = self.tableNumber1 + 1 
        Id = self.getId()
        Id['gifts'].append(unicode(gift.toUtf8(), 'utf-8', 'ignore'))
        self.setId(Id)
    def clearGift(self):
        self.giftList = []
        self.tableNumber1 = 0
        self.ui.giftmodel.removeRows(0, self.ui.model.rowCount())
        self.ui.GiftTable.setModel(self.ui.giftmodel)
        self.ui.initGiftTable()
        Id = self.getId()
        Id['gifts'] = []
        self.setId(Id)
    def login(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        account = self.getAccount()
        Id['account'] = account
        if user.autoLogin(Id['driver'], account):
            print name + u'登录成功'
            # QtGui.QMessageBox.information(self, u'登录提示', name + u'登录成功')
        else:
            print name + u'登录失败'
            # QtGui.QMessageBox.critical(self, u'登录提示', name + u'登录失败 ')
    
    def autoLogin(self):
        thread.start_new_thread(self.login, ())
    
    def getskData(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        res = sktb.saveActiveList(Id['driver'])
        if res[1]:
            Id['skdata'] = res[0]
            Id['skdata'].sort(key=lambda obj: obj.get('time'), reverse=True) 
            # QtGui.QMessageBox.information(self, u'获取试客活动数据提示', name + u'获取数据成功')
            print name + u'试客活动获取数据成功'
        else:
            print name + u'试客活动获取数据失败'
            # QtGui.QMessageBox.critical(self, u'获取试客活动数据提示', name + u'获取数据失败')
        self.setId(Id)
    def getShikeeData(self):
        thread.start_new_thread(self.getskData, ())
    
    
    def execActivity(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        trialsNumber = self.ui.TrialsNumber.text()  # 近30日获得试用次数
        number = self.ui.Number.text()  # 近30天下单次数
        
        invalidOrders = self.ui.InvalidOrders.text()  # 无效订单次数
        averageTime = self.ui.AverageTime.text()  # 填写订单号平均时长
        total = self.ui.Total.text()  # 参与试用总次数
        
        abandonNumber = self.ui.AbandonNumber.text()  # 放弃试用次数
        
        violationsNumber = self.ui.ViolationsNumber.text()  # 违规次数
        days = self.ui.Days.text()
        bilv = self.ui.Days_2.text()
        res = {'bilv':str(bilv), 'invalidOrders': str(invalidOrders), 'averageTime': str(averageTime), 'total': str(total), 'trialsNumber': str(trialsNumber), 'abandonNumber': str(abandonNumber), 'number': str(number), 'violationsNumber': str(violationsNumber), 'days': str(days), 'account':Id['account']['skusername'], 'tbuser':Id['account']['tbusername']}
        
        if sktb.executeActivity(Id['driver'], Id['skdata'], Id['tasks'], res):
            # QtGui.QMessageBox.information(self, u'通过结果提示', name + u'通过完成')
            print name + u'通过完成'
        else:
            print name + u'过程出错'
            # QtGui.QMessageBox.critical(self, u'通过结果提示', name + u'过程出错')
    def executeActivity(self):
        thread.start_new_thread(self.execActivity, ())
    
    def execRemarks(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        color = {'list':Id['gifts'], 'account':Id['account']['skusername'], 'tbuser':Id['account']['tbusername']}
        
        if review.addRemarks(Id['driver'], Id['skdata'], color):
            # QtGui.QMessageBox.information(self, u'备注结果提示', name + u'备注完成')
            print name + u'备注完成'
        else:
            print name + u'过程出错'
            # QtGui.QMessageBox.critical(self, u'备注结果提示', name + u'过程出错')
    
    def executeRemarks(self):
        thread.start_new_thread(self.execRemarks, ())
    
    def rtfRemarks(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        try:
            color = {'list':Id['gifts'], 'account':Id['account']['skusername'], 'tbuser':Id['account']['tbusername']}
            if self.ui.allData.isChecked():
                if review.correct(Id['driver'], color, True):
                    print name + u'纠正完成'
                    # QtGui.QMessageBox.information(self, u'纠正全部备注提示', name + u'纠正完成')
                else:
                    print name + u'过程出错'
                    # QtGui.QMessageBox.critical(self, u'纠正全部备注提示', name + u'过程出错')
            elif self.ui.partData.isChecked():
                if review.correct(Id['driver'], color, False):
                    print name + u'纠正完成'
                    # QtGui.QMessageBox.information(self, u'纠正部分备注提示', name + u'纠正完成')
                else:
                    print name + u'过程出错'
                    # QtGui.QMessageBox.critical(self, u'纠正部分备注提示', name + u'过程出错')
        except Exception, e:
            info = sys.exc_info()
            debug.log(str(sys.exc_info()[2].tb_lineno), e.message, info[1], os.path.basename(__file__))
    def rectifyRemarks(self):
        thread.start_new_thread(self.rtfRemarks, ())
    def atf(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        
        color = {'list':Id['gifts'], 'account':Id['account']['skusername'], 'tbuser':Id['account']['tbusername']}
        
        if review.artificial(Id['driver'], self.orders, color):
            print name + u'备注完成'
            QtGui.QMessageBox.information(self, u'手动添加订单备注提示', name + u'备注完成')
        else:
            print name + u'过程出错'
            QtGui.QMessageBox.critical(self, u'手动添加订单备注提示', name + u'过程出错')
    def artificial(self):
        thread.start_new_thread(self.atf, ())
        
    def approved(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        if user.autoLogin(Id['driver'], Id['account']):
            print name + u'登录成功'
            res = sktb.saveActiveList(Id['driver'])
            if res[1]:
                Id['skdata'] = res[0]
                Id['skdata'].sort(key=lambda obj: obj.get('time'), reverse=True) 
                # QtGui.QMessageBox.information(self, u'获取试客活动数据提示', name + u'获取数据成功')
                print name + u'试客活动获取数据成功'
                # self.setId(Id)
                trialsNumber = self.ui.TrialsNumber.text()  # 近30日获得试用次数
                number = self.ui.Number.text()  # 近30天下单次数
                
                invalidOrders = self.ui.InvalidOrders.text()  # 无效订单次数
                averageTime = self.ui.AverageTime.text()  # 填写订单号平均时长
                total = self.ui.Total.text()  # 参与试用总次数
                
                abandonNumber = self.ui.AbandonNumber.text()  # 放弃试用次数
                
                violationsNumber = self.ui.ViolationsNumber.text()  # 违规次数
                days = self.ui.Days.text()
                bilv = self.ui.Days_2.text()
                res = {'bilv':str(bilv), 'invalidOrders': str(invalidOrders), 'averageTime': str(averageTime), 'total': str(total), 'trialsNumber': str(trialsNumber), 'abandonNumber': str(abandonNumber), 'number': str(number), 'violationsNumber': str(violationsNumber), 'days': str(days), 'account':Id['account']['skusername'], 'tbuser':Id['account']['tbusername']}
                
                if sktb.executeActivity(Id['driver'], Id['skdata'], Id['tasks'], res):
                    # QtGui.QMessageBox.information(self, u'通过结果提示', name + u'通过完成')
                    print name + u'通过完成'
                else:
                    print name + u'过程出错'
            else:
                print name + u'试客活动获取数据失败'
            # QtGui.QMessageBox.information(self, u'登录提示', name + u'登录成功')
        else:
            print name + u'登录失败'
        
    def approvedTimer(self):
        second_1 = int(self.ui.second_1.text())
        threading.Timer(second_1 * 1.0, self.approved).start()
        
    def remarks(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        if user.autoLogin(Id['driver'], Id['account']):
            print name + u'登录成功'
            res = sktb.saveActiveList(Id['driver'])
            if res[1]:
                Id['skdata'] = res[0]
                Id['skdata'].sort(key=lambda obj: obj.get('time'), reverse=True) 
                # QtGui.QMessageBox.information(self, u'获取试客活动数据提示', name + u'获取数据成功')
                print name + u'试客活动获取数据成功'
                # self.setId(Id)
                color = {'list':Id['gifts'], 'account':Id['account']['skusername'], 'tbuser':Id['account']['tbusername']}
        
                if review.addRemarks(Id['driver'], Id['skdata'], color):
                    # QtGui.QMessageBox.information(self, u'备注结果提示', name + u'备注完成')
                    print name + u'备注完成'
                else:
                    print name + u'过程出错'
                    # QtGui.QMessageBox.critical(self, u'备注结果提示', name + u'过程出错')
            else:
                print name + u'试客活动获取数据失败'
            # QtGui.QMessageBox.information(self, u'登录提示', name + u'登录成功')
        else:
            print name + u'登录失败'
    def remarksTimer(self):
        second_2 = int(self.ui.second_2.text())
        threading.Timer(second_2 * 1.0, self.remarks).start()
    
    def task(self):
        name = unicode(self.ui.Account.currentText().toUtf8(), 'utf-8', 'ignore')
        Id = self.getId()
        if user.autoLogin(Id['driver'], Id['account']):
            print name + u'登录成功'
            res = sktb.saveActiveList(Id['driver'])
            if res[1]:
                Id['skdata'] = res[0]
                Id['skdata'].sort(key=lambda obj: obj.get('time'), reverse=True) 
                # QtGui.QMessageBox.information(self, u'获取试客活动数据提示', name + u'获取数据成功')
                print name + u'试客活动获取数据成功'
                # self.setId(Id)
                color = {'list':Id['gifts'], 'account':Id['account']['skusername'], 'tbuser':Id['account']['tbusername']}
        
                if review.addRemarks(Id['driver'], Id['skdata'], color):
                    # QtGui.QMessageBox.information(self, u'备注结果提示', name + u'备注完成')
                    print name + u'备注完成'
                    trialsNumber = self.ui.TrialsNumber.text()  # 近30日获得试用次数
                    number = self.ui.Number.text()  # 近30天下单次数
                    
                    invalidOrders = self.ui.InvalidOrders.text()  # 无效订单次数
                    averageTime = self.ui.AverageTime.text()  # 填写订单号平均时长
                    total = self.ui.Total.text()  # 参与试用总次数
                    
                    abandonNumber = self.ui.AbandonNumber.text()  # 放弃试用次数
                    
                    violationsNumber = self.ui.ViolationsNumber.text()  # 违规次数
                    days = self.ui.Days.text()
                    bilv = self.ui.Days_2.text()
                    res = {'bilv':str(bilv), 'invalidOrders': str(invalidOrders), 'averageTime': str(averageTime), 'total': str(total), 'trialsNumber': str(trialsNumber), 'abandonNumber': str(abandonNumber), 'number': str(number), 'violationsNumber': str(violationsNumber), 'days': str(days), 'account':Id['account']['skusername'], 'tbuser':Id['account']['tbusername']}
                    
                    if sktb.executeActivity(Id['driver'], Id['skdata'], Id['tasks'], res):
                        # QtGui.QMessageBox.information(self, u'通过结果提示', name + u'通过完成')
                        print name + u'通过完成'
                    else:
                        print name + u'过程出错'
                else:
                    print name + u'过程出错'
                    # QtGui.QMessageBox.critical(self, u'备注结果提示', name + u'过程出错')
            else:
                print name + u'试客活动获取数据失败'
            # QtGui.QMessageBox.information(self, u'登录提示', name + u'登录成功')
        else:
            print name + u'登录失败'    
    def taskTimer(self):
        second_3 = int(self.ui.second_3.text())
        threading.Timer(second_3 * 1.0, self.task).start()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())
