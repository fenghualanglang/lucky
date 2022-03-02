# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("打开网页")
        MainWindow.resize(1640, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 630, 30))

        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(690, 10, 90, 30))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## 创建web窗体
        self.qwebengine = QtWebEngineWidgets.QWebEngineView(MainWindow)
        self.qwebengine.setGeometry(20, 50, 1600, 600)

        ## 创建连接
        self.pushButton.clicked.connect(self.open_url)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "打开网页"))
        self.lineEdit.setText(_translate("MainWindow", "http://www.baidu.com"))
        self.pushButton.setText(_translate("MainWindow", "打开"))

    def open_url(self):
        url=self.lineEdit.text()
        self.qwebengine.load(QtCore.QUrl(url))



import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()                   # 创建窗体对象
    ui = Ui_MainWindow()                                   # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)                                 # 调用窗体的方法对对象进行初始化设置
    MainWindow.show()                                      # 显示窗体
    sys.exit(app.exec_())                                  # 程序关闭时退出进程