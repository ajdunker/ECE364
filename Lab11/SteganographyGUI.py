# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SteganographyGUI.ui'
#
# Created: Wed Apr 13 20:05:38 2016
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 640)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabOption = QtGui.QTabWidget(self.centralwidget)
        self.tabOption.setGeometry(QtCore.QRect(10, 10, 861, 581))
        self.tabOption.setObjectName("tabOption")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.grpCarrier1 = QtGui.QGroupBox(self.tab)
        self.grpCarrier1.setGeometry(QtCore.QRect(470, 10, 381, 461))
        self.grpCarrier1.setAlignment(QtCore.Qt.AlignCenter)
        self.grpCarrier1.setFlat(False)
        self.grpCarrier1.setObjectName("grpCarrier1")
        self.chkOverride = QtGui.QCheckBox(self.grpCarrier1)
        self.chkOverride.setEnabled(False)
        self.chkOverride.setGeometry(QtCore.QRect(20, 370, 141, 22))
        self.chkOverride.setObjectName("chkOverride")
        self.lblPayloadFound = QtGui.QLabel(self.grpCarrier1)
        self.lblPayloadFound.setGeometry(QtCore.QRect(30, 330, 331, 21))
        font = QtGui.QFont()
        font.setFamily("CM Roman")
        font.setPointSize(15)
        self.lblPayloadFound.setFont(font)
        self.lblPayloadFound.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPayloadFound.setObjectName("lblPayloadFound")
        self.txtCarrierSize = QtGui.QLineEdit(self.grpCarrier1)
        self.txtCarrierSize.setGeometry(QtCore.QRect(140, 410, 231, 27))
        self.txtCarrierSize.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCarrierSize.setReadOnly(True)
        self.txtCarrierSize.setObjectName("txtCarrierSize")
        self.lblCarrierSize = QtGui.QLabel(self.grpCarrier1)
        self.lblCarrierSize.setGeometry(QtCore.QRect(10, 410, 121, 21))
        font = QtGui.QFont()
        font.setFamily("CM Roman")
        font.setPointSize(15)
        self.lblCarrierSize.setFont(font)
        self.lblCarrierSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCarrierSize.setObjectName("lblCarrierSize")
        self.lblArrow = QtGui.QLabel(self.tab)
        self.lblArrow.setGeometry(QtCore.QRect(390, 180, 71, 21))
        font = QtGui.QFont()
        font.setFamily("CM Roman")
        font.setPointSize(15)
        self.lblArrow.setFont(font)
        self.lblArrow.setAlignment(QtCore.Qt.AlignCenter)
        self.lblArrow.setObjectName("lblArrow")
        self.grpPayload1 = QtGui.QGroupBox(self.tab)
        self.grpPayload1.setGeometry(QtCore.QRect(0, 10, 381, 461))
        self.grpPayload1.setAlignment(QtCore.Qt.AlignCenter)
        self.grpPayload1.setFlat(False)
        self.grpPayload1.setObjectName("grpPayload1")
        self.txtCompression = QtGui.QLineEdit(self.grpPayload1)
        self.txtCompression.setEnabled(False)
        self.txtCompression.setGeometry(QtCore.QRect(340, 370, 31, 27))
        self.txtCompression.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCompression.setReadOnly(True)
        self.txtCompression.setObjectName("txtCompression")
        self.slideCompression = QtGui.QSlider(self.grpPayload1)
        self.slideCompression.setEnabled(False)
        self.slideCompression.setGeometry(QtCore.QRect(80, 363, 251, 31))
        self.slideCompression.setMaximum(9)
        self.slideCompression.setPageStep(1)
        self.slideCompression.setProperty("value", 0)
        self.slideCompression.setTracking(True)
        self.slideCompression.setOrientation(QtCore.Qt.Horizontal)
        self.slideCompression.setInvertedAppearance(False)
        self.slideCompression.setTickPosition(QtGui.QSlider.TicksBelow)
        self.slideCompression.setTickInterval(1)
        self.slideCompression.setObjectName("slideCompression")
        self.lblLevel = QtGui.QLabel(self.grpPayload1)
        self.lblLevel.setEnabled(False)
        self.lblLevel.setGeometry(QtCore.QRect(30, 370, 35, 21))
        self.lblLevel.setObjectName("lblLevel")
        self.chkApplyCompression = QtGui.QCheckBox(self.grpPayload1)
        self.chkApplyCompression.setGeometry(QtCore.QRect(10, 340, 161, 22))
        self.chkApplyCompression.setObjectName("chkApplyCompression")
        self.lblPayloadSize = QtGui.QLabel(self.grpPayload1)
        self.lblPayloadSize.setGeometry(QtCore.QRect(10, 410, 121, 21))
        font = QtGui.QFont()
        font.setFamily("CM Roman")
        font.setPointSize(15)
        self.lblPayloadSize.setFont(font)
        self.lblPayloadSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPayloadSize.setObjectName("lblPayloadSize")
        self.txtPayloadSize = QtGui.QLineEdit(self.grpPayload1)
        self.txtPayloadSize.setGeometry(QtCore.QRect(140, 410, 231, 27))
        self.txtPayloadSize.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPayloadSize.setReadOnly(True)
        self.txtPayloadSize.setObjectName("txtPayloadSize")
        self.btnSave = QtGui.QPushButton(self.tab)
        self.btnSave.setEnabled(False)
        self.btnSave.setGeometry(QtCore.QRect(340, 510, 161, 27))
        self.btnSave.setObjectName("btnSave")
        self.tabOption.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.grpPayload2 = QtGui.QGroupBox(self.tab_2)
        self.grpPayload2.setGeometry(QtCore.QRect(470, 10, 381, 331))
        self.grpPayload2.setAlignment(QtCore.Qt.AlignCenter)
        self.grpPayload2.setFlat(False)
        self.grpPayload2.setObjectName("grpPayload2")
        self.viewPayload2 = QtGui.QGraphicsView(self.grpPayload2)
        self.viewPayload2.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewPayload2.setObjectName("viewPayload2")
        self.grpCarrier2 = QtGui.QGroupBox(self.tab_2)
        self.grpCarrier2.setGeometry(QtCore.QRect(0, 10, 381, 461))
        self.grpCarrier2.setAlignment(QtCore.Qt.AlignCenter)
        self.grpCarrier2.setFlat(False)
        self.grpCarrier2.setObjectName("grpCarrier2")
        self.lblCarrierEmpty = QtGui.QLabel(self.grpCarrier2)
        self.lblCarrierEmpty.setGeometry(QtCore.QRect(20, 330, 331, 21))
        font = QtGui.QFont()
        font.setFamily("CM Roman")
        font.setPointSize(15)
        self.lblCarrierEmpty.setFont(font)
        self.lblCarrierEmpty.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCarrierEmpty.setObjectName("lblCarrierEmpty")
        self.btnExtract = QtGui.QPushButton(self.grpCarrier2)
        self.btnExtract.setEnabled(False)
        self.btnExtract.setGeometry(QtCore.QRect(50, 370, 281, 27))
        self.btnExtract.setObjectName("btnExtract")
        self.btnClean = QtGui.QPushButton(self.grpCarrier2)
        self.btnClean.setEnabled(False)
        self.btnClean.setGeometry(QtCore.QRect(50, 410, 281, 27))
        self.btnClean.setObjectName("btnClean")
        self.lblArrow2 = QtGui.QLabel(self.tab_2)
        self.lblArrow2.setGeometry(QtCore.QRect(390, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily("CM Roman")
        font.setPointSize(15)
        self.lblArrow2.setFont(font)
        self.lblArrow2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblArrow2.setObjectName("lblArrow2")
        self.tabOption.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabOption.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.grpCarrier1.setTitle(QtGui.QApplication.translate("MainWindow", "Carrier", None, QtGui.QApplication.UnicodeUTF8))
        self.chkOverride.setText(QtGui.QApplication.translate("MainWindow", "Override Payload", None, QtGui.QApplication.UnicodeUTF8))
        self.txtCarrierSize.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCarrierSize.setText(QtGui.QApplication.translate("MainWindow", "Carrier Size", None, QtGui.QApplication.UnicodeUTF8))
        self.lblArrow.setText(QtGui.QApplication.translate("MainWindow", "==>", None, QtGui.QApplication.UnicodeUTF8))
        self.grpPayload1.setTitle(QtGui.QApplication.translate("MainWindow", "Payload", None, QtGui.QApplication.UnicodeUTF8))
        self.txtCompression.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLevel.setText(QtGui.QApplication.translate("MainWindow", "Level", None, QtGui.QApplication.UnicodeUTF8))
        self.chkApplyCompression.setText(QtGui.QApplication.translate("MainWindow", "Apply Compression", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPayloadSize.setText(QtGui.QApplication.translate("MainWindow", "Payload Size", None, QtGui.QApplication.UnicodeUTF8))
        self.txtPayloadSize.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("MainWindow", "Embed and Save To ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabOption.setTabText(self.tabOption.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Embed Payload in Carrier", None, QtGui.QApplication.UnicodeUTF8))
        self.grpPayload2.setTitle(QtGui.QApplication.translate("MainWindow", "Payload", None, QtGui.QApplication.UnicodeUTF8))
        self.grpCarrier2.setTitle(QtGui.QApplication.translate("MainWindow", "Carrier", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExtract.setText(QtGui.QApplication.translate("MainWindow", "Extract Payload", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClean.setText(QtGui.QApplication.translate("MainWindow", "Clean Carrier", None, QtGui.QApplication.UnicodeUTF8))
        self.lblArrow2.setText(QtGui.QApplication.translate("MainWindow", "==>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabOption.setTabText(self.tabOption.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Extract Payload from Carrier", None, QtGui.QApplication.UnicodeUTF8))

