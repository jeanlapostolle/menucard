# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 611, 741))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.b_newTable = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_newTable.setMinimumSize(QtCore.QSize(150, 75))
        self.b_newTable.setObjectName("b_newTable")
        self.verticalLayout_2.addWidget(self.b_newTable)
        self.b_send = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_send.setMinimumSize(QtCore.QSize(150, 75))
        self.b_send.setObjectName("b_send")
        self.verticalLayout_2.addWidget(self.b_send)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tb_recap = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.tb_recap.setObjectName("tb_recap")
        self.horizontalLayout.addWidget(self.tb_recap)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tab_select = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tab_select.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_select.setIconSize(QtCore.QSize(16, 16))
        self.tab_select.setObjectName("tab_select")
        self.tab_entree = QtWidgets.QWidget()
        self.tab_entree.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_entree.setObjectName("tab_entree")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_entree)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 601, 331))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.entreeLayout = QtWidgets.QVBoxLayout()
        self.entreeLayout.setObjectName("entreeLayout")
        self.horizontalLayout_2.addLayout(self.entreeLayout)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.recapentreeLayout = QtWidgets.QVBoxLayout()
        self.recapentreeLayout.setObjectName("recapentreeLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recapentreeLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.recapentreeLayout)
        self.tab_select.addTab(self.tab_entree, "")
        self.tab_plat = QtWidgets.QWidget()
        self.tab_plat.setObjectName("tab_plat")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_plat)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 601, 331))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.platLayout = QtWidgets.QVBoxLayout()
        self.platLayout.setObjectName("platLayout")
        self.horizontalLayout_3.addLayout(self.platLayout)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.recaplatlayout = QtWidgets.QVBoxLayout()
        self.recaplatlayout.setObjectName("recaplatlayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recaplatlayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.recaplatlayout)
        self.tab_select.addTab(self.tab_plat, "")
        self.tab_dessert = QtWidgets.QWidget()
        self.tab_dessert.setObjectName("tab_dessert")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_dessert)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 601, 331))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dessertlayout = QtWidgets.QVBoxLayout()
        self.dessertlayout.setObjectName("dessertlayout")
        self.horizontalLayout_6.addLayout(self.dessertlayout)
        self.line_5 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_6.addWidget(self.line_5)
        self.recapdessertLayout = QtWidgets.QVBoxLayout()
        self.recapdessertLayout.setObjectName("recapdessertLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recapdessertLayout.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.recapdessertLayout)
        self.tab_select.addTab(self.tab_dessert, "")
        self.tab_boisson = QtWidgets.QWidget()
        self.tab_boisson.setObjectName("tab_boisson")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_boisson)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 601, 331))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.boissonLayout = QtWidgets.QVBoxLayout()
        self.boissonLayout.setObjectName("boissonLayout")
        self.horizontalLayout_8.addLayout(self.boissonLayout)
        self.line_7 = QtWidgets.QFrame(self.horizontalLayoutWidget_5)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_8.addWidget(self.line_7)
        self.recapboissonLayout = QtWidgets.QVBoxLayout()
        self.recapboissonLayout.setObjectName("recapboissonLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recapboissonLayout.addItem(spacerItem4)
        self.horizontalLayout_8.addLayout(self.recapboissonLayout)
        self.tab_select.addTab(self.tab_boisson, "")
        self.verticalLayout.addWidget(self.tab_select)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_select.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_newTable.setText(_translate("MainWindow", "Table"))
        self.b_send.setText(_translate("MainWindow", "Envoyer"))
        self.tb_recap.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Table n° <span style=\" font-weight:600;\">_ </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Total:    €                  </span></p></body></html>"))
        self.tab_select.setTabText(self.tab_select.indexOf(self.tab_entree), _translate("MainWindow", "Entrée"))
        self.tab_select.setTabText(self.tab_select.indexOf(self.tab_plat), _translate("MainWindow", "Plat"))
        self.tab_select.setTabText(self.tab_select.indexOf(self.tab_dessert), _translate("MainWindow", "Dessert"))
        self.tab_select.setTabText(self.tab_select.indexOf(self.tab_boisson), _translate("MainWindow", "Boisson"))
