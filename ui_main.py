# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DownloawDetector.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, 
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDateTimeEdit,
    QMainWindow, QSizePolicy, QStatusBar, QTextEdit, QTextBrowser,
    QTimeEdit, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(453, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(150, 380, 141, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setAutoFillBackground(False)
        self.timeEdit.setWrapping(False)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.timeEdit.setProperty("showGroupSeparator", False)
        self.timeEdit.setCurrentSection(QDateTimeEdit.SecondSection)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(160, 450, 131, 31))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(250, 190, 161, 31))
        self.toolButton.setAutoFillBackground(False)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textEdit")
        self.textBrowser.setGeometry(QRect(40, 30, 371, 161))
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textEdit_2")
        self.textBrowser_2.setGeometry(QRect(40, 320, 381, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u0442\u0430\u0439\u043c\u0435\u0440\u0430", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u043f\u043a\u0438 Steam", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 downloading \u0432\u0430\u0448\u0435\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438 Steam </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">(.../SteamLibrary/steamapps/downloading)<br />\u0415\u0441\u043b\u0438 \u0442\u0430\u043a\u0438\u0445 \u043f\u0430\u043f\u043e\u043a"
                        " \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0445 \u0432\u0441\u0435 \u0438\u043b\u0438 \u0442\u043e\u043b\u044c\u043a\u043e \u0436\u0435\u043b\u0430\u0435\u043c\u044b\u0435 </span></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435, \u0447\u0435\u0440\u0435\u0437 \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 (\u0447\u0430\u0441\u044b:\u043c\u0438\u043d\u0443\u0442\u044b:\u0441\u0435\u043a\u0443\u043d\u0434\u044b) \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d \u043f\u043e\u0441\u043b\u0435 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f</p></body></html>", None))
    # retranslateUi

