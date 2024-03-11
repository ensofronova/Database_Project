# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(183, 187, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:0;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane{\n"
"border:1 px;\n"
"background:none;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"background: rgb(170, 170, 255);\n"
"min-width: 30ex;\n"
"min-height: 9ex;\n"
"margin-left: 2px;\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"background: rgb(229, 231, 255);\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"}\n"
"\n"
"QTabBar::tab:hover{\n"
"background: rgb(210, 213, 255);\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"}")
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.BusinessTab = QtWidgets.QWidget()
        self.BusinessTab.setAutoFillBackground(False)
        self.BusinessTab.setStyleSheet("QWidget:pane { border: 0; }")
        self.BusinessTab.setObjectName("BusinessTab")
        self.BusinessTable = QtWidgets.QTableWidget(self.BusinessTab)
        self.BusinessTable.setGeometry(QtCore.QRect(40, 105, 920, 371))
        self.BusinessTable.setStyleSheet("QTableWidget {\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"}\n"
"\n"
"QTableWidget:section{\n"
"background-color: rgb(170, 170, 255);\n"
"color: black;\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"}\n"
"\n"
"QTableWidget:item{\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"color:black;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"color: black;\n"
"background-color: white;\n"
"}")
        self.BusinessTable.setObjectName("BusinessTable")
        self.BusinessTable.setColumnCount(0)
        self.BusinessTable.setRowCount(0)
        self.businessNameText = QtWidgets.QLineEdit(self.BusinessTab)
        self.businessNameText.setGeometry(QtCore.QRect(570, 60, 211, 30))
        self.businessNameText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.businessNameText.setText("")
        self.businessNameText.setAlignment(QtCore.Qt.AlignCenter)
        self.businessNameText.setObjectName("businessNameText")
        self.addButton = QtWidgets.QPushButton(self.BusinessTab)
        self.addButton.setGeometry(QtCore.QRect(800, 20, 71, 30))
        self.addButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/add_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton")
        self.clearButton = QtWidgets.QPushButton(self.BusinessTab)
        self.clearButton.setGeometry(QtCore.QRect(889, 20, 71, 30))
        self.clearButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/close_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setObjectName("clearButton")
        self.searchButton = QtWidgets.QPushButton(self.BusinessTab)
        self.searchButton.setGeometry(QtCore.QRect(800, 60, 71, 30))
        self.searchButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/search_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon2)
        self.searchButton.setObjectName("searchButton")
        self.deleteButton = QtWidgets.QPushButton(self.BusinessTab)
        self.deleteButton.setGeometry(QtCore.QRect(889, 60, 71, 30))
        self.deleteButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/delete_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon3)
        self.deleteButton.setObjectName("deleteButton")
        self.addressText = QtWidgets.QLineEdit(self.BusinessTab)
        self.addressText.setGeometry(QtCore.QRect(40, 60, 361, 30))
        self.addressText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.addressText.setAlignment(QtCore.Qt.AlignCenter)
        self.addressText.setObjectName("addressText")
        self.supplierText = QtWidgets.QLineEdit(self.BusinessTab)
        self.supplierText.setGeometry(QtCore.QRect(320, 20, 301, 30))
        self.supplierText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.supplierText.setAlignment(QtCore.Qt.AlignCenter)
        self.supplierText.setObjectName("supplierText")
        self.ownerNameText_2 = QtWidgets.QLineEdit(self.BusinessTab)
        self.ownerNameText_2.setGeometry(QtCore.QRect(40, 20, 251, 30))
        self.ownerNameText_2.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.ownerNameText_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ownerNameText_2.setObjectName("ownerNameText_2")
        self.featureText = QtWidgets.QLineEdit(self.BusinessTab)
        self.featureText.setGeometry(QtCore.QRect(650, 20, 131, 30))
        self.featureText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"\n"
"")
        self.featureText.setText("")
        self.featureText.setAlignment(QtCore.Qt.AlignCenter)
        self.featureText.setObjectName("featureText")
        self.label = QtWidgets.QLabel(self.BusinessTab)
        self.label.setGeometry(QtCore.QRect(420, 70, 131, 16))
        self.label.setStyleSheet("border: none;\n"
"background-color: none")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.BusinessTab, "")
        self.OwnersTab = QtWidgets.QWidget()
        self.OwnersTab.setObjectName("OwnersTab")
        self.ownerNameText = QtWidgets.QLineEdit(self.OwnersTab)
        self.ownerNameText.setGeometry(QtCore.QRect(40, 20, 321, 30))
        self.ownerNameText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.ownerNameText.setAlignment(QtCore.Qt.AlignCenter)
        self.ownerNameText.setObjectName("ownerNameText")
        self.addOwnersButton = QtWidgets.QPushButton(self.OwnersTab)
        self.addOwnersButton.setGeometry(QtCore.QRect(700, 20, 120, 30))
        self.addOwnersButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.addOwnersButton.setIcon(icon)
        self.addOwnersButton.setObjectName("addOwnersButton")
        self.deleteOwnersButton = QtWidgets.QPushButton(self.OwnersTab)
        self.deleteOwnersButton.setGeometry(QtCore.QRect(840, 60, 120, 30))
        self.deleteOwnersButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.deleteOwnersButton.setIcon(icon3)
        self.deleteOwnersButton.setObjectName("deleteOwnersButton")
        self.searchOwnersButton = QtWidgets.QPushButton(self.OwnersTab)
        self.searchOwnersButton.setGeometry(QtCore.QRect(700, 60, 120, 30))
        self.searchOwnersButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.searchOwnersButton.setIcon(icon2)
        self.searchOwnersButton.setObjectName("searchOwnersButton")
        self.clearOwnersButton = QtWidgets.QPushButton(self.OwnersTab)
        self.clearOwnersButton.setGeometry(QtCore.QRect(840, 20, 120, 30))
        self.clearOwnersButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.clearOwnersButton.setIcon(icon1)
        self.clearOwnersButton.setObjectName("clearOwnersButton")
        self.emailText = QtWidgets.QLineEdit(self.OwnersTab)
        self.emailText.setGeometry(QtCore.QRect(400, 60, 281, 30))
        self.emailText.setStyleSheet("\n"
"\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"\n"
"")
        self.emailText.setText("")
        self.emailText.setAlignment(QtCore.Qt.AlignCenter)
        self.emailText.setObjectName("emailText")
        self.ownersTable = QtWidgets.QTableWidget(self.OwnersTab)
        self.ownersTable.setGeometry(QtCore.QRect(40, 105, 920, 371))
        self.ownersTable.setStyleSheet("QTableWidget {\n"
"background-color: white;\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"}\n"
"\n"
"QTableWidget:section{\n"
"background-color: rgb(170, 170, 255);\n"
"color: black;\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"}\n"
"\n"
"QTableWidget:item{\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"color:black;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"color: white;\n"
"background-color: rgb(170, 170, 255);\n"
"}")
        self.ownersTable.setObjectName("ownersTable")
        self.ownersTable.setColumnCount(0)
        self.ownersTable.setRowCount(0)
        self.foundationDate = QtWidgets.QDateEdit(self.OwnersTab)
        self.foundationDate.setGeometry(QtCore.QRect(520, 20, 161, 31))
        self.foundationDate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.foundationDate.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.foundationDate.setAlignment(QtCore.Qt.AlignCenter)
        self.foundationDate.setDate(QtCore.QDate(2021, 12, 17))
        self.foundationDate.setObjectName("foundationDate")
        self.label_2 = QtWidgets.QLabel(self.OwnersTab)
        self.label_2.setGeometry(QtCore.QRect(400, 30, 111, 16))
        self.label_2.setStyleSheet("border: none;\n"
"background-color: none")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.OwnersTab)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 171, 16))
        self.label_3.setStyleSheet("border: none;\n"
"background-color: none")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.OwnersTab, "")
        self.SuppliersTab = QtWidgets.QWidget()
        self.SuppliersTab.setObjectName("SuppliersTab")
        self.volumePurchaseText = QtWidgets.QLineEdit(self.SuppliersTab)
        self.volumePurchaseText.setGeometry(QtCore.QRect(470, 20, 181, 30))
        self.volumePurchaseText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.volumePurchaseText.setAlignment(QtCore.Qt.AlignCenter)
        self.volumePurchaseText.setObjectName("volumePurchaseText")
        self.suppliersTable = QtWidgets.QTableWidget(self.SuppliersTab)
        self.suppliersTable.setGeometry(QtCore.QRect(30, 110, 920, 361))
        self.suppliersTable.setStyleSheet("QTableView {\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"}\n"
"\n"
"QTableView:section{\n"
"background-color: rgb(170, 170, 255);\n"
"color: black;\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"}\n"
"\n"
"QTableView:item{\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"color:black;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"color: white;\n"
"background-color: rgb(170, 170, 255);\n"
"}")
        self.suppliersTable.setObjectName("suppliersTable")
        self.suppliersTable.setColumnCount(1)
        self.suppliersTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.suppliersTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.suppliersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.suppliersTable.setItem(0, 0, item)
        self.label_7 = QtWidgets.QLabel(self.SuppliersTab)
        self.label_7.setGeometry(QtCore.QRect(100, 70, 221, 20))
        self.label_7.setStyleSheet("border: none;\n"
"background-color: none")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.addSuppliersButton = QtWidgets.QPushButton(self.SuppliersTab)
        self.addSuppliersButton.setGeometry(QtCore.QRect(710, 20, 105, 22))
        self.addSuppliersButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.addSuppliersButton.setIcon(icon)
        self.addSuppliersButton.setObjectName("addSuppliersButton")
        self.searchSuppliersButton = QtWidgets.QPushButton(self.SuppliersTab)
        self.searchSuppliersButton.setGeometry(QtCore.QRect(710, 60, 105, 22))
        self.searchSuppliersButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.searchSuppliersButton.setIcon(icon2)
        self.searchSuppliersButton.setObjectName("searchSuppliersButton")
        self.clearSuppliersButton = QtWidgets.QPushButton(self.SuppliersTab)
        self.clearSuppliersButton.setGeometry(QtCore.QRect(850, 9, 111, 31))
        self.clearSuppliersButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.clearSuppliersButton.setIcon(icon1)
        self.clearSuppliersButton.setObjectName("clearSuppliersButton")
        self.deleteSuppliersButton = QtWidgets.QPushButton(self.SuppliersTab)
        self.deleteSuppliersButton.setGeometry(QtCore.QRect(850, 50, 101, 31))
        self.deleteSuppliersButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.deleteSuppliersButton.setIcon(icon3)
        self.deleteSuppliersButton.setObjectName("deleteSuppliersButton")
        self.organisationText = QtWidgets.QLineEdit(self.SuppliersTab)
        self.organisationText.setGeometry(QtCore.QRect(40, 20, 401, 30))
        self.organisationText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.organisationText.setAlignment(QtCore.Qt.AlignCenter)
        self.organisationText.setObjectName("organisationText")
        self.phoneNumberText = QtWidgets.QLineEdit(self.SuppliersTab)
        self.phoneNumberText.setGeometry(QtCore.QRect(370, 60, 141, 31))
        self.phoneNumberText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.phoneNumberText.setText("")
        self.phoneNumberText.setAlignment(QtCore.Qt.AlignCenter)
        self.phoneNumberText.setObjectName("phoneNumberText")
        self.tabWidget.addTab(self.SuppliersTab, "")
        self.RatingsTab = QtWidgets.QWidget()
        self.RatingsTab.setObjectName("RatingsTab")
        self.ratingsTable = QtWidgets.QTableWidget(self.RatingsTab)
        self.ratingsTable.setGeometry(QtCore.QRect(40, 105, 920, 371))
        self.ratingsTable.setStyleSheet("QTableWidget {\n"
"background-color: white;\n"
"color: black;\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"selection-color:black;\n"
"selection-background-color:rgb(210, 213, 255);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"gridline:black;\n"
"background-color:rgb(170, 170, 255);\n"
"selection-background-color:rgb(229, 231, 255);\n"
"}")
        self.ratingsTable.setObjectName("ratingsTable")
        self.ratingsTable.setColumnCount(3)
        self.ratingsTable.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ratingsTable.setItem(0, 0, item)
        self.feedbackText = QtWidgets.QLineEdit(self.RatingsTab)
        self.feedbackText.setGeometry(QtCore.QRect(480, 20, 481, 61))
        self.feedbackText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.feedbackText.setAlignment(QtCore.Qt.AlignCenter)
        self.feedbackText.setObjectName("feedbackText")
        self.addRatingsButton = QtWidgets.QPushButton(self.RatingsTab)
        self.addRatingsButton.setGeometry(QtCore.QRect(30, 60, 93, 29))
        self.addRatingsButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.addRatingsButton.setIcon(icon2)
        self.addRatingsButton.setObjectName("addRatingsButton")
        self.gradeText = QtWidgets.QLineEdit(self.RatingsTab)
        self.gradeText.setGeometry(QtCore.QRect(360, 40, 111, 30))
        self.gradeText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.gradeText.setText("")
        self.gradeText.setAlignment(QtCore.Qt.AlignCenter)
        self.gradeText.setObjectName("gradeText")
        self.label_8 = QtWidgets.QLabel(self.RatingsTab)
        self.label_8.setGeometry(QtCore.QRect(360, 20, 111, 16))
        self.label_8.setStyleSheet("background-color: none")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.BusinessRatingsText = QtWidgets.QLineEdit(self.RatingsTab)
        self.BusinessRatingsText.setGeometry(QtCore.QRect(240, 50, 111, 21))
        self.BusinessRatingsText.setStyleSheet("\n"
"border-radius: 7px;\n"
"border: 1px solid  rgb(137, 139, 255);\n"
"")
        self.BusinessRatingsText.setAlignment(QtCore.Qt.AlignCenter)
        self.BusinessRatingsText.setObjectName("BusinessRatingsText")
        self.addRatingsButton_2 = QtWidgets.QPushButton(self.RatingsTab)
        self.addRatingsButton_2.setGeometry(QtCore.QRect(30, 20, 93, 29))
        self.addRatingsButton_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.addRatingsButton_2.setIcon(icon)
        self.addRatingsButton_2.setObjectName("addRatingsButton_2")
        self.addRatingsButton_4 = QtWidgets.QPushButton(self.RatingsTab)
        self.addRatingsButton_4.setGeometry(QtCore.QRect(130, 18, 101, 31))
        self.addRatingsButton_4.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.addRatingsButton_4.setIcon(icon1)
        self.addRatingsButton_4.setObjectName("addRatingsButton_4")
        self.addRatingsButton_3 = QtWidgets.QPushButton(self.RatingsTab)
        self.addRatingsButton_3.setGeometry(QtCore.QRect(130, 60, 93, 29))
        self.addRatingsButton_3.setStyleSheet("QPushButton {\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid  rgb(114, 108, 199);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(210, 213, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(229, 231, 255);\n"
"}")
        self.addRatingsButton_3.setIcon(icon3)
        self.addRatingsButton_3.setObjectName("addRatingsButton_3")
        self.feedbackText.raise_()
        self.gradeText.raise_()
        self.label_8.raise_()
        self.BusinessRatingsText.raise_()
        self.ratingsTable.raise_()
        self.addRatingsButton.raise_()
        self.addRatingsButton_3.raise_()
        self.addRatingsButton_2.raise_()
        self.addRatingsButton_4.raise_()
        self.tabWidget.addTab(self.RatingsTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionClear_table = QtWidgets.QAction(MainWindow)
        self.actionClear_table.setObjectName("actionClear_table")
        self.actionClear_all = QtWidgets.QAction(MainWindow)
        self.actionClear_all.setObjectName("actionClear_all")
        self.actionClear_Tables = QtWidgets.QAction(MainWindow)
        self.actionClear_Tables.setObjectName("actionClear_Tables")
        self.actionDelete_database = QtWidgets.QAction(MainWindow)
        self.actionDelete_database.setObjectName("actionDelete_database")
        self.menuDatabase.addAction(self.actionConnect)
        self.menuDatabase.addAction(self.actionDelete_database)
        self.menuDatabase.addAction(self.actionClear_Tables)
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interface"))
        self.businessNameText.setPlaceholderText(_translate("MainWindow", "Business name"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.addressText.setPlaceholderText(_translate("MainWindow", "Address"))
        self.supplierText.setPlaceholderText(_translate("MainWindow", "Supplier"))
        self.ownerNameText_2.setPlaceholderText(_translate("MainWindow", "Owner\'s name"))
        self.featureText.setPlaceholderText(_translate("MainWindow", "Feature"))
        self.label.setText(_translate("MainWindow", "Search and delete by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BusinessTab), _translate("MainWindow", "Business"))
        self.ownerNameText.setPlaceholderText(_translate("MainWindow", "Owner\'s name"))
        self.addOwnersButton.setText(_translate("MainWindow", "Add"))
        self.deleteOwnersButton.setText(_translate("MainWindow", "Delete"))
        self.searchOwnersButton.setText(_translate("MainWindow", "Search"))
        self.clearOwnersButton.setText(_translate("MainWindow", "Clear"))
        self.emailText.setPlaceholderText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Foundation date"))
        self.label_3.setText(_translate("MainWindow", "Search and delete by email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OwnersTab), _translate("MainWindow", "Owners"))
        self.volumePurchaseText.setPlaceholderText(_translate("MainWindow", "Rewiews"))
        item = self.suppliersTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "htnhn"))
        item = self.suppliersTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "gtbr"))
        __sortingEnabled = self.suppliersTable.isSortingEnabled()
        self.suppliersTable.setSortingEnabled(False)
        item = self.suppliersTable.item(0, 0)
        item.setText(_translate("MainWindow", "jnhjnhjn"))
        self.suppliersTable.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Search and delete by phone number"))
        self.addSuppliersButton.setText(_translate("MainWindow", "Add"))
        self.searchSuppliersButton.setText(_translate("MainWindow", "Search"))
        self.clearSuppliersButton.setText(_translate("MainWindow", "Clear"))
        self.deleteSuppliersButton.setText(_translate("MainWindow", "Delete"))
        self.organisationText.setPlaceholderText(_translate("MainWindow", "Organisation"))
        self.phoneNumberText.setPlaceholderText(_translate("MainWindow", "Phone number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SuppliersTab), _translate("MainWindow", "Suppliers"))
        item = self.ratingsTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "r2fewd"))
        item = self.ratingsTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "wqertyhjkhtrewqertgh"))
        item = self.ratingsTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.ratingsTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "ertgyhjgtrewertgh"))
        item = self.ratingsTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "wertgyhjgtrew"))
        item = self.ratingsTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "wqertyuhjytrewqedrftghj"))
        item = self.ratingsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "rf4ed"))
        item = self.ratingsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "srdtfnyghfdsreasrdtghjh"))
        item = self.ratingsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ertyuhjgtrewert"))
        __sortingEnabled = self.ratingsTable.isSortingEnabled()
        self.ratingsTable.setSortingEnabled(False)
        item = self.ratingsTable.item(0, 0)
        item.setText(_translate("MainWindow", "edfwrd"))
        self.ratingsTable.setSortingEnabled(__sortingEnabled)
        self.feedbackText.setPlaceholderText(_translate("MainWindow", "Feedback"))
        self.addRatingsButton.setText(_translate("MainWindow", "Search"))
        self.gradeText.setPlaceholderText(_translate("MainWindow", "Grade"))
        self.label_8.setText(_translate("MainWindow", "Rate from 0 to 10"))
        self.BusinessRatingsText.setPlaceholderText(_translate("MainWindow", "Name"))
        self.addRatingsButton_2.setText(_translate("MainWindow", "Add"))
        self.addRatingsButton_4.setText(_translate("MainWindow", "Clear"))
        self.addRatingsButton_3.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RatingsTab), _translate("MainWindow", "Ratings"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionClear_table.setText(_translate("MainWindow", "Clear table"))
        self.actionClear_all.setText(_translate("MainWindow", "Clear all"))
        self.actionClear_Tables.setText(_translate("MainWindow", "Clear Tables"))
        self.actionDelete_database.setText(_translate("MainWindow", "Delete"))