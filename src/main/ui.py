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
        self.shikeeLabel = QtGui.QLabel(self.centralwidget)
        self.shikeeLabel.setGeometry(QtCore.QRect(330, 10, 61, 21))
        self.shikeeLabel.setObjectName(_fromUtf8("shikeeLabel"))
        self.shikeeUsernameLabel = QtGui.QLabel(self.centralwidget)
        self.shikeeUsernameLabel.setGeometry(QtCore.QRect(330, 40, 31, 21))
        self.shikeeUsernameLabel.setObjectName(_fromUtf8("shikeeUsernameLabel"))
        self.shikeePasswordLabel = QtGui.QLabel(self.centralwidget)
        self.shikeePasswordLabel.setGeometry(QtCore.QRect(330, 70, 31, 21))
        self.shikeePasswordLabel.setObjectName(_fromUtf8("shikeePasswordLabel"))
        self.taobaoLabel = QtGui.QLabel(self.centralwidget)
        self.taobaoLabel.setGeometry(QtCore.QRect(330, 130, 61, 21))
        self.taobaoLabel.setObjectName(_fromUtf8("taobaoLabel"))
        self.taobaoUsernameLabel = QtGui.QLabel(self.centralwidget)
        self.taobaoUsernameLabel.setGeometry(QtCore.QRect(330, 160, 31, 21))
        self.taobaoUsernameLabel.setObjectName(_fromUtf8("taobaoUsernameLabel"))
        self.taobaoPasswordLabel = QtGui.QLabel(self.centralwidget)
        self.taobaoPasswordLabel.setGeometry(QtCore.QRect(330, 190, 31, 21))
        self.taobaoPasswordLabel.setObjectName(_fromUtf8("taobaoPasswordLabel"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(310, 100, 331, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.ShikeeUserName = QtGui.QLineEdit(self.centralwidget)
        self.ShikeeUserName.setGeometry(QtCore.QRect(380, 40, 171, 20))
        self.ShikeeUserName.setObjectName(_fromUtf8("ShikeeUserName"))
        self.ShikeePassword = QtGui.QLineEdit(self.centralwidget)
        self.ShikeePassword.setEchoMode(QtGui.QLineEdit.Password)
        self.ShikeePassword.setGeometry(QtCore.QRect(380, 70, 171, 20))
        self.ShikeePassword.setObjectName(_fromUtf8("ShikeePassword"))
        self.TaobaoUserName = QtGui.QLineEdit(self.centralwidget)
        self.TaobaoUserName.setGeometry(QtCore.QRect(380, 160, 171, 20))
        self.TaobaoUserName.setObjectName(_fromUtf8("TaobaoUserName"))
        self.TaobaoPassword = QtGui.QLineEdit(self.centralwidget)
        self.TaobaoPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.TaobaoPassword.setGeometry(QtCore.QRect(380, 190, 171, 20))
        self.TaobaoPassword.setObjectName(_fromUtf8("TaobaoPassword"))
        self.loginShikee = QtGui.QPushButton(self.centralwidget)
        self.loginShikee.setGeometry(QtCore.QRect(560, 40, 75, 51))
        self.loginShikee.setObjectName(_fromUtf8("loginShikee"))
        self.loginTaobao = QtGui.QPushButton(self.centralwidget)
        self.loginTaobao.setGeometry(QtCore.QRect(560, 160, 75, 51))
        self.loginTaobao.setObjectName(_fromUtf8("loginTaobao"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 230, 650, 250))
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
        self.Days = QtGui.QLineEdit(self.tab)
        self.Days.setGeometry(QtCore.QRect(120, 190, 51, 20))
        self.Days.setObjectName(_fromUtf8("Days"))
        self.DayLabel = QtGui.QLabel(self.tab)
        self.DayLabel.setGeometry(QtCore.QRect(180, 190, 21, 21))
        self.DayLabel.setObjectName(_fromUtf8("DayLabel"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
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
        self.shikeeLabel.raise_()
        self.shikeeUsernameLabel.raise_()
        self.shikeePasswordLabel.raise_()
        self.taobaoLabel.raise_()
        self.taobaoUsernameLabel.raise_()
        self.taobaoPasswordLabel.raise_()
        self.line_3.raise_()
        self.ShikeeUserName.raise_()
        self.ShikeePassword.raise_()
        self.TaobaoUserName.raise_()
        self.TaobaoPassword.raise_()
        self.loginShikee.raise_()
        self.loginTaobao.raise_()
        self.tabWidget.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "自动化工具 V1.0", None))
        self.violationLabel.setText(_translate("mainWindow", "违规次数", None))
        self.placeAnOrderLabel.setText(_translate("mainWindow", "近30日下单次数", None))
        self.abandonLabel.setText(_translate("mainWindow", "试客放弃试用次数", None))
        self.getLabel.setText(_translate("mainWindow", "近30日获得试用次数", None))
        self.totalLabel.setText(_translate("mainWindow", "试客总参与试用次数", None))
        self.invalidLabel.setText(_translate("mainWindow", "试客提交无效订单号次数", None))
        self.timeLabel.setText(_translate("mainWindow", "近30内填写订单号的平均时长", None))
        self.shikeeLabel.setText(_translate("mainWindow", "试客联盟", None))
        self.shikeeUsernameLabel.setText(_translate("mainWindow", "账号", None))
        self.shikeePasswordLabel.setText(_translate("mainWindow", "密码", None))
        self.taobaoLabel.setText(_translate("mainWindow", "淘宝", None))
        self.taobaoUsernameLabel.setText(_translate("mainWindow", "账号", None))
        self.taobaoPasswordLabel.setText(_translate("mainWindow", "密码", None))
        self.loginShikee.setText(_translate("mainWindow", "登陆", None))
        self.loginTaobao.setText(_translate("mainWindow", "登陆", None))
        self.GetShikeeData.setText(_translate("mainWindow", "获取试客数据", None))
        self.AddActivity.setText(_translate("mainWindow", "添加任务", None))
        self.ActivityNumberLabel.setText(_translate("mainWindow", "活动编号", None))
        self.PeopleNumberLabel.setText(_translate("mainWindow", "通过人数", None))
        self.ExecuteActivity.setText(_translate("mainWindow", "执行任务", None))
        self.resetActivity.setText(_translate("mainWindow", "重置任务", None))
        self.clearLink.setText(_translate("mainWindow", "清除无效链接", None))
        self.DayLabel.setText(_translate("mainWindow", "天", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "任务", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "备注", None))


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
