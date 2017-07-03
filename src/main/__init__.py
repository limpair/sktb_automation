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
    
    def closeEvent(self, event):
        self.driver.close()
        event.accept()
    
    def initButton(self):
        self.ui.AddActivity.clicked.connect(self.addActive)
        self.ui.loginTaobao.clicked.connect(self.loginTaobao)
        self.ui.loginShikee.clicked.connect(self.loginShikee)
        self.ui.GetShikeeData.clicked.connect(self.getShikeeData)
    
    def initDriver(self):
        self.driver = webdriver.Chrome()
    
    def addActive(self):
        a = self.ui.ActivityNumber.text()
        b = self.ui.PeopleNumber.text()
        self.ui.model.setItem(self.tableNumber, 0, QtGui.QStandardItem(ui._fromUtf8(a)))
        self.ui.model.setItem(self.tableNumber, 1, QtGui.QStandardItem(ui._fromUtf8(b)))
        self.ui.model.setItem(self.tableNumber, 2, QtGui.QStandardItem(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        self.tableNumber = self.tableNumber + 1
        self.ui.tableView.setModel(self.ui.model)
        
    def loginTaobao(self):
        name = self.ui.TaobaoUserName.text()
        pswd = self.ui.TaobaoPassword.text()
        sktb.loginTaobao(self.driver, unicode(name.toUtf8(), 'utf-8', 'ignore'), str(pswd))
    
    def loginShikee(self):
        name = self.ui.ShikeeUserName.text()
        pswd = self.ui.ShikeePassword.text()
        sktb.loginShikee(self.driver, unicode(name.toUtf8(), 'utf-8', 'ignore'), str(pswd))
    
    def getShikeeData(self):
        a = time.time()
        try_list = sktb.saveActiveList(self.driver)
        self.try_list = sktb.saveTryList(self.driver, try_list)
        print self.try_list
        b = time.time()
        print round(b - a, 2)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)     
    window = window()     
    window.show()     
    sys.exit(app.exec_())
