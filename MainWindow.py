import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from ui_mainwindow import Ui_MainWindow
from menu import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.resize(640, 820)
        self.setWindowTitle("MenuAPPS")
        self.setWindowIcon(QIcon("./ressource/images/frites.svg"))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tab_select.setStyleSheet(
            "QTabBar::tab { min-height: 50px; width: 150%}")
        self.pBentree = []
        self.pBplat = []
        self.pBdessert = []
        self.pBboisson = []
        spacerItem1 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        for i in range(len(entrees)):
            self.pBentree.append(QPushButton(self.ui.horizontalLayoutWidget_2))
            self.pBentree[i].setMinimumSize(QSize(200, 50))
            self.pBentree[i].setObjectName(entrees[i])
            self.pBentree[i].setText(entrees[i])
            self.ui.entreeLayout.addWidget(self.pBentree[i])

        self.ui.entreeLayout.addItem(spacerItem1)

        for i in range(len(plats)):
            self.pBplat.append(QPushButton(self.ui.horizontalLayoutWidget_2))
            self.pBplat[i].setMinimumSize(QSize(200, 50))
            self.pBplat[i].setObjectName(plats[i])
            self.pBplat[i].setText(plats[i])
            self.ui.platLayout.addWidget(self.pBplat[i])

        self.ui.platLayout.addItem(spacerItem1)

        for i in range(len(desserts)):
            self.pBdessert.append(QPushButton(
                self.ui.horizontalLayoutWidget_2))
            self.pBdessert[i].setMinimumSize(QSize(200, 50))
            self.pBdessert[i].setObjectName(desserts[i])
            self.pBdessert[i].setText(desserts[i])
            self.ui.dessertlayout.addWidget(self.pBdessert[i])

        self.ui.dessertlayout.addItem(spacerItem1)

        for i in range(len(boissons)):
            self.pBboisson.append(QPushButton(
                self.ui.horizontalLayoutWidget_2))
            self.pBboisson[i].setMinimumSize(QSize(200, 50))
            self.pBboisson[i].setObjectName(boissons[i])
            self.pBboisson[i].setText(boissons[i])
            self.ui.boissonLayout.addWidget(self.pBboisson[i])

        self.ui.boissonLayout.addItem(spacerItem1)


        # for plat in plats:
        # self.ui.verticalLayout_3.addItem()
        # uic.loadUi('ui/mainwindow.ui', self)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()
