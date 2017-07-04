# -*- coding: UTF-8 -*-

from selenium import webdriver
from PyQt4 import QtCore, QtGui
import ui, sktb, sys, time

class window(QtGui.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = ui.Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.initTable()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.tableNumber = 0
        self.initButton()
        self.initDriver()
        
        self.ui.TaobaoUserName.setText(u'starry_sky品牌企业店:盘满钵满')
        self.ui.TaobaoPassword.setText('qqh983468869')
        
        self.ui.ShikeeUserName.setText('13794728078')
        self.ui.ShikeePassword.setText('kyd0920')
        
        self.ui.InvalidOrders.setText('1')
        self.ui.AverageTime.setText('2')
        self.ui.Total.setText('3')
        self.ui.TrialsNumber.setText('4')
        self.ui.AbandonNumber.setText('5')
        self.ui.Number.setText('6')
        self.ui.ViolationsNumber.setText('7')
        
        
    def closeEvent(self, event):
        self.driver.close()
        event.accept()
    
    def initButton(self):
        self.ui.AddActivity.clicked.connect(self.addActive)
        self.ui.loginTaobao.clicked.connect(self.loginTaobao)
        self.ui.loginShikee.clicked.connect(self.loginShikee)
        self.ui.GetShikeeData.clicked.connect(self.getShikeeData)
        self.ui.ClearActivity.clicked.connect(self.clearActive)
        self.ui.ExecuteActivity.clicked.connect(self.executeActivity)
        
    
    def initDriver(self):
        self.taskList = []
        self.driver = webdriver.Chrome('E:\sktb_automation\src\driver\chromedriver.exe')
    
    def addActive(self):
        a = self.ui.ActivityNumber.text()
        b = self.ui.PeopleNumber.text()
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.ui.model.setItem(self.tableNumber, 0, QtGui.QStandardItem(ui._fromUtf8(a)))
        self.ui.model.setItem(self.tableNumber, 1, QtGui.QStandardItem(ui._fromUtf8(b)))
        self.ui.model.setItem(self.tableNumber, 2, QtGui.QStandardItem(t))
        self.tableNumber = self.tableNumber + 1
        self.ui.tableView.setModel(self.ui.model)
        self.taskList.append({'name':str(a).upper(), 'num':int(b), 'time':t})
        
    def clearActive(self):
        print self.taskList
        self.taskList = []
        self.tableNumber = 0
        self.ui.model.removeRows(0, self.ui.model.rowCount())
        self.ui.tableView.setModel(self.ui.model)
        self.ui.initTable()
        
    def loginTaobao(self):
        name = self.ui.TaobaoUserName.text()
        pswd = self.ui.TaobaoPassword.text()
        sktb.loginTaobao(self.driver, unicode(name.toUtf8(), 'utf-8', 'ignore'), str(pswd))
    
    def loginShikee(self):
        name = self.ui.ShikeeUserName.text()
        pswd = self.ui.ShikeePassword.text()
        sktb.loginShikee(self.driver, unicode(name.toUtf8(), 'utf-8', 'ignore'), str(pswd))
    
    def getShikeeData(self):
        #a = time.time()
        self.try_list = sktb.saveActiveList(self.driver)
        self.try_list.sort(key=lambda obj:obj.get('time'),reverse=True)
        #self.try_list = sktb.saveTryList(self.driver, try_list)
        #print self.try_list
        #b = time.time()
        #print round(b - a, 2)
    
    def deleteTryList(self):
        url=''
        for t in self.try_list:
            if t['link'] in url:
                self.try_list.remove(t)
                break
    
    def executeActivity(self):
        invalidOrders = self.ui.InvalidOrders.text()#无效订单次数
        averageTime=self.ui.AverageTime.text()#填写订单号平均时长
        total=self.ui.Total.text()#参与试用总次数
        trialsNumber=self.ui.TrialsNumber.text()#近30日获得试用次数
        abandonNumber=self.ui.AbandonNumber.text()#放弃试用次数
        number=self.ui.Number.text()#近30天下单次数
        violationsNumber=self.ui.ViolationsNumber.text()#违规次数 
        res={'invalidOrders':str(invalidOrders),'averageTime':str(averageTime),'total':str(total),'trialsNumber':str(trialsNumber),'abandonNumber':str(abandonNumber),'number':str(number),'violationsNumber':str(violationsNumber)}
        print res
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())