# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(643, 501)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("main.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.violationLabel = QtGui.QLabel(self.centralwidget)
        self.violationLabel.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.violationLabel.setObjectName(_fromUtf8("violationLabel"))
        self.placeAnOrderLabel = QtGui.QLabel(self.centralwidget)
        self.placeAnOrderLabel.setGeometry(QtCore.QRect(10, 40, 161, 21))
        self.placeAnOrderLabel.setObjectName(_fromUtf8("placeAnOrderLabel"))
        self.abandonLabel = QtGui.QLabel(self.centralwidget)
        self.abandonLabel.setGeometry(QtCore.QRect(10, 70, 161, 21))
        self.abandonLabel.setObjectName(_fromUtf8("abandonLabel"))
        self.getLabel = QtGui.QLabel(self.centralwidget)
        self.getLabel.setGeometry(QtCore.QRect(10, 100, 161, 21))
        self.getLabel.setObjectName(_fromUtf8("getLabel"))
        self.totalLabel = QtGui.QLabel(self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(10, 130, 161, 21))
        self.totalLabel.setObjectName(_fromUtf8("totalLabel"))
        self.invalidLabel = QtGui.QLabel(self.centralwidget)
        self.invalidLabel.setGeometry(QtCore.QRect(10, 160, 161, 21))
        self.invalidLabel.setObjectName(_fromUtf8("invalidLabel"))
        self.timeLabel = QtGui.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(10, 190, 161, 21))
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.AverageTime = QtGui.QLineEdit(self.centralwidget)
        self.AverageTime.setGeometry(QtCore.QRect(180, 190, 113, 20))
        self.AverageTime.setObjectName(_fromUtf8("AverageTime"))
        self.InvalidOrders = QtGui.QLineEdit(self.centralwidget)
        self.InvalidOrders.setGeometry(QtCore.QRect(180, 160, 113, 20))
        self.InvalidOrders.setObjectName(_fromUtf8("InvalidOrders"))
        self.Total = QtGui.QLineEdit(self.centralwidget)
        self.Total.setGeometry(QtCore.QRect(180, 130, 113, 20))
        self.Total.setObjectName(_fromUtf8("Total"))
        self.TrialsNumber = QtGui.QLineEdit(self.centralwidget)
        self.TrialsNumber.setGeometry(QtCore.QRect(180, 100, 113, 20))
        self.TrialsNumber.setObjectName(_fromUtf8("TrialsNumber"))
        self.AbandonNumber = QtGui.QLineEdit(self.centralwidget)
        self.AbandonNumber.setGeometry(QtCore.QRect(180, 70, 113, 20))
        self.AbandonNumber.setObjectName(_fromUtf8("AbandonNumber"))
        self.Number = QtGui.QLineEdit(self.centralwidget)
        self.Number.setGeometry(QtCore.QRect(180, 40, 113, 20))
        self.Number.setObjectName(_fromUtf8("Number"))
        self.ViolationsNumber = QtGui.QLineEdit(self.centralwidget)
        self.ViolationsNumber.setGeometry(QtCore.QRect(180, 10, 113, 20))
        self.ViolationsNumber.setObjectName(_fromUtf8("ViolationsNumber"))
        self.line_1 = QtGui.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(0, 210, 641, 41))
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(300, -10, 20, 241))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.shikeeUsernameLabel = QtGui.QLabel(self.centralwidget)
        self.shikeeUsernameLabel.setGeometry(QtCore.QRect(330, 45, 32, 20))
        self.shikeeUsernameLabel.setObjectName(_fromUtf8("shikeeUsernameLabel"))
        
        self.autoLogin = QtGui.QPushButton(self.centralwidget)
        self.autoLogin.setGeometry(QtCore.QRect(560, 45, 80, 25))
        self.autoLogin.setObjectName(_fromUtf8("autoLogin"))
        
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 230, 643, 241))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.GetShikeeData = QtGui.QPushButton(self.tab)
        self.GetShikeeData.setGeometry(QtCore.QRect(10, 110, 81, 31))
        self.GetShikeeData.setObjectName(_fromUtf8("GetShikeeData"))
        self.AddActivity = QtGui.QPushButton(self.tab)
        self.AddActivity.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.AddActivity.setObjectName(_fromUtf8("AddActivity"))
        self.ActivityNumberLabel = QtGui.QLabel(self.tab)
        self.ActivityNumberLabel.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.ActivityNumberLabel.setObjectName(_fromUtf8("ActivityNumberLabel"))
        self.PeopleNumberLabel = QtGui.QLabel(self.tab)
        self.PeopleNumberLabel.setGeometry(QtCore.QRect(10, 40, 51, 21))
        self.PeopleNumberLabel.setObjectName(_fromUtf8("PeopleNumberLabel"))
        self.ActivityNumber = QtGui.QLineEdit(self.tab)
        self.ActivityNumber.setGeometry(QtCore.QRect(80, 10, 113, 20))
        self.ActivityNumber.setObjectName(_fromUtf8("ActivityNumber"))
        self.PeopleNumber = QtGui.QLineEdit(self.tab)
        self.PeopleNumber.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.PeopleNumber.setObjectName(_fromUtf8("PeopleNumber"))
        self.tableView = QtGui.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(205, 10, 431, 201))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.ExecuteActivity = QtGui.QPushButton(self.tab)
        self.ExecuteActivity.setGeometry(QtCore.QRect(110, 110, 81, 31))
        self.ExecuteActivity.setObjectName(_fromUtf8("ExecuteActivity"))
        self.resetActivity = QtGui.QPushButton(self.tab)
        self.resetActivity.setGeometry(QtCore.QRect(110, 70, 81, 31))
        self.resetActivity.setObjectName(_fromUtf8("resetActivity"))
        self.Link = QtGui.QLineEdit(self.tab)
        self.Link.setGeometry(QtCore.QRect(10, 150, 181, 20))
        self.Link.setObjectName(_fromUtf8("Link"))
        self.clearLink = QtGui.QPushButton(self.tab)
        self.clearLink.setGeometry(QtCore.QRect(10, 180, 81, 31))
        self.clearLink.setObjectName(_fromUtf8("clearLink"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(310, 30, 331, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.DayLabel = QtGui.QLabel(self.centralwidget)
        self.DayLabel.setGeometry(QtCore.QRect(330, 10, 21, 21))
        self.DayLabel.setObjectName(_fromUtf8("DayLabel"))
        self.Days = QtGui.QLineEdit(self.centralwidget)
        self.Days.setGeometry(QtCore.QRect(360, 10, 51, 20))
        self.Days.setObjectName(_fromUtf8("Days"))
        self.DayLabel_2 = QtGui.QLabel(self.centralwidget)
        self.DayLabel_2.setGeometry(QtCore.QRect(460, 10, 101, 21))
        self.DayLabel_2.setObjectName(_fromUtf8("DayLabel_2"))
        self.Days_2 = QtGui.QLineEdit(self.centralwidget)
        self.Days_2.setGeometry(QtCore.QRect(580, 10, 51, 20))
        self.Days_2.setText(_fromUtf8(""))
        self.Days_2.setObjectName(_fromUtf8("Days_2"))
        
        self.executeRemarks = QtGui.QPushButton(self.tab_2)
        self.executeRemarks.setGeometry(QtCore.QRect(410, 40, 75, 24))
        self.executeRemarks.setObjectName(_fromUtf8("executeRemarks"))
        
        self.rectifyRemarks = QtGui.QPushButton(self.tab_2)
        self.rectifyRemarks.setGeometry(QtCore.QRect(410, 70, 75, 24))
        self.rectifyRemarks.setObjectName(_fromUtf8("rectifyRemarks"))
        
        self.addGift = QtGui.QPushButton(self.tab_2)
        self.addGift.setGeometry(QtCore.QRect(410, 10, 75, 24))
        self.addGift.setObjectName(_fromUtf8("addGift"))
        
        self.resetGift = QtGui.QPushButton(self.tab_2)
        self.resetGift.setGeometry(QtCore.QRect(410, 100, 75, 24))
        self.resetGift.setObjectName(_fromUtf8("resetGift"))
        
        
        self.allData = QtGui.QRadioButton(self.tab_2)
        self.allData.setGeometry(QtCore.QRect(400, 130, 50, 24))
        self.allData.setObjectName(_fromUtf8("allData"))
        self.partData = QtGui.QRadioButton(self.tab_2)
        self.partData.setGeometry(QtCore.QRect(450, 130, 75, 24))
        self.partData.setObjectName(_fromUtf8("partData"))
        
        
        self.GiftTable = QtGui.QTableView(self.tab_2)
        self.GiftTable.setGeometry(QtCore.QRect(300, 40, 100, 170))
        self.GiftTable.setObjectName(_fromUtf8("GiftTable"))
        self.Gift = QtGui.QLineEdit(self.tab_2)
        self.Gift.setGeometry(QtCore.QRect(300, 10, 100, 24))
        self.Gift.setObjectName(_fromUtf8("Gift"))
        
        self.orderTable = QtGui.QTableView(self.tab_2)
        self.orderTable.setGeometry(QtCore.QRect(0, 40, 290, 170))
        self.orderTable.setObjectName(_fromUtf8("orderTable"))
        self.addOrder = QtGui.QPushButton(self.tab_2)
        self.addOrder.setGeometry(QtCore.QRect(180, 10, 41, 24))
        self.addOrder.setObjectName(_fromUtf8("addOrder"))
        self.orderLine = QtGui.QLineEdit(self.tab_2)
        self.orderLine.setGeometry(QtCore.QRect(0, 10, 180, 24))
        self.orderLine.setObjectName(_fromUtf8("orderLine"))
        self.Execute0 = QtGui.QPushButton(self.tab_2)
        self.Execute0.setGeometry(QtCore.QRect(220, 10, 41, 24))
        self.Execute0.setObjectName(_fromUtf8("Execute0"))
        
        self.resetOrder = QtGui.QPushButton(self.tab_2)
        self.resetOrder.setGeometry(QtCore.QRect(260, 10, 41, 24))
        self.resetOrder.setObjectName(_fromUtf8("resetOrder"))
        
        self.openBrowser = QtGui.QPushButton(self.centralwidget)
        self.openBrowser.setGeometry(QtCore.QRect(560, 80, 80, 24))
        self.openBrowser.setObjectName(_fromUtf8("openBrowser"))
        self.Browser = QtGui.QComboBox(self.centralwidget)
        self.Browser.setGeometry(QtCore.QRect(490, 80, 65, 24))
        self.Browser.setObjectName(_fromUtf8("Browser"))
        
        self.BrowserNumber = QtGui.QComboBox(self.centralwidget)
        self.BrowserNumber.setGeometry(QtCore.QRect(320, 80, 65, 24))
        self.BrowserNumber.setObjectName(_fromUtf8("BrowserNumber"))
        
        self.closeBrowser = QtGui.QPushButton(self.centralwidget)
        self.closeBrowser.setGeometry(QtCore.QRect(390, 80, 75, 24))
        self.closeBrowser.setObjectName(_fromUtf8("openBrowser"))
        
        self.Account = QtGui.QComboBox(self.centralwidget)
        self.Account.setGeometry(QtCore.QRect(370, 45, 180, 24))
        self.Account.setObjectName(_fromUtf8("Account"))
        
        self.violationLabel.raise_()
        self.placeAnOrderLabel.raise_()
        self.abandonLabel.raise_()
        self.getLabel.raise_()
        self.totalLabel.raise_()
        self.invalidLabel.raise_()
        self.timeLabel.raise_()
        self.AverageTime.raise_()
        self.InvalidOrders.raise_()
        self.Total.raise_()
        self.TrialsNumber.raise_()
        self.AbandonNumber.raise_()
        self.Number.raise_()
        self.ViolationsNumber.raise_()
        self.line_2.raise_()
        self.line_1.raise_()
        self.shikeeUsernameLabel.raise_()
        self.tabWidget.raise_()
        self.Days.raise_()
        self.line_4.raise_()
        self.DayLabel.raise_()
        self.Days.raise_()
        self.DayLabel_2.raise_()
        self.Days_2.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "自动化多线程 Beta V1.0.0", None))
        self.violationLabel.setText(_translate("mainWindow", "违规次数", None))
        self.placeAnOrderLabel.setText(_translate("mainWindow", "近30日下单次数", None))
        self.abandonLabel.setText(_translate("mainWindow", "试客放弃试用次数", None))
        self.getLabel.setText(_translate("mainWindow", "近30日获得试用次数", None))
        self.totalLabel.setText(_translate("mainWindow", "试客总参与试用次数", None))
        self.invalidLabel.setText(_translate("mainWindow", "试客提交无效订单号次数", None))
        self.timeLabel.setText(_translate("mainWindow", "近30内填写订单号的平均时长", None))
        self.shikeeUsernameLabel.setText(_translate("mainWindow", "账号", None))

        self.autoLogin.setText(_translate("mainWindow", "自动登陆登陆", None))

        self.GetShikeeData.setText(_translate("mainWindow", "获取试客数据", None))
        self.AddActivity.setText(_translate("mainWindow", "添加任务", None))
        self.ActivityNumberLabel.setText(_translate("mainWindow", "活动编号", None))
        self.PeopleNumberLabel.setText(_translate("mainWindow", "通过人数", None))
        self.ExecuteActivity.setText(_translate("mainWindow", "执行任务", None))
        self.resetActivity.setText(_translate("mainWindow", "重置任务", None))
        self.clearLink.setText(_translate("mainWindow", "清除无效链接", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "任务", None))
        self.executeRemarks.setText(_translate("mainWindow", "执行", None))
        self.rectifyRemarks.setText(_translate("mainWindow", "纠正", None))
        self.addGift.setText(_translate("mainWindow", "添加送啥", None))
        self.resetGift.setText(_translate("mainWindow", "不送了", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "备注", None))
        self.DayLabel.setText(_translate("mainWindow", "天", None))
        self.DayLabel_2.setText(_translate("mainWindow", "下单/获得（比率）", None))
        self.addOrder.setText(_translate("mainWindow", "添加", None))
        self.Execute0.setText(_translate("mainWindow", "执行", None))
        self.resetOrder.setText(_translate("mainWindow", "重置", None))
        self.allData.setText(_translate("mainWindow", "全部", None))
        self.partData.setText(_translate("mainWindow", "部分", None))
        
        self.openBrowser.setText(_translate("mainWindow", "启动浏览器", None))
        self.closeBrowser.setText(_translate("mainWindow", "关闭浏览器", None))
        
        self.partData.click()
        
    def initTable(self):
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.model.setRowCount(10)    
        self.model.setColumnCount(3) 
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, _fromUtf8("活动编号"))
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, _fromUtf8("通过人数"))
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, _fromUtf8("添加时间"))
        
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter) 
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setColumnWidth(0, 120) 
        self.tableView.setColumnWidth(1, 120) 
        self.tableView.setColumnWidth(2, 150)
    def initGiftTable(self):
        self.giftmodel = QtGui.QStandardItemModel(self.GiftTable)
        
        self.giftmodel.setRowCount(10)    
        self.giftmodel.setColumnCount(1)
        self.giftmodel.setHeaderData(0, QtCore.Qt.Horizontal, _fromUtf8("啥"))
        
        self.GiftTable.setModel(self.giftmodel)
        self.GiftTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter) 
        self.GiftTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        
        self.GiftTable.setColumnWidth(0, 80)
    def initOrderTable(self):
        self.orderModel = QtGui.QStandardItemModel(self.orderTable)
        
        self.orderModel.setRowCount(10)    
        self.orderModel.setColumnCount(1)
        self.orderModel.setHeaderData(0, QtCore.Qt.Horizontal, _fromUtf8("订单编号"))
        
        self.orderTable.setModel(self.orderModel)
        self.orderTable.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter) 
        self.orderTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        
        self.orderTable.setColumnWidth(0, 250)
        
        
        
        