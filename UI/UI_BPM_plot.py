# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_BPM_plot.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)
import qpprcc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1004)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.actionView_data = QAction(MainWindow)
        self.actionView_data.setObjectName(u"actionView_data")
        self.actionPD_ADC = QAction(MainWindow)
        self.actionPD_ADC.setObjectName(u"actionPD_ADC")
        self.actionpAmeter = QAction(MainWindow)
        self.actionpAmeter.setObjectName(u"actionpAmeter")
        self.actionDatabase = QAction(MainWindow)
        self.actionDatabase.setObjectName(u"actionDatabase")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 106, 60, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(85, 170, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_2.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.Channel_cbx = QComboBox(self.centralwidget)
        self.Channel_cbx.addItem("")
        self.Channel_cbx.addItem("")
        self.Channel_cbx.setObjectName(u"Channel_cbx")
        self.Channel_cbx.setMinimumSize(QSize(150, 40))
        self.Channel_cbx.setMaximumSize(QSize(220, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Channel_cbx.setFont(font1)
        self.Channel_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Channel_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.horizontalLayout_3.addWidget(self.Channel_cbx)

        self.Port_cbx = QComboBox(self.centralwidget)
        self.Port_cbx.setObjectName(u"Port_cbx")
        self.Port_cbx.setMinimumSize(QSize(150, 40))
        self.Port_cbx.setMaximumSize(QSize(220, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.Port_cbx.setFont(font2)
        self.Port_cbx.setLayoutDirection(Qt.LeftToRight)
        self.Port_cbx.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(180, 249, 255);")

        self.horizontalLayout_3.addWidget(self.Port_cbx)

        self.Connect_counter_btn = QPushButton(self.centralwidget)
        self.Connect_counter_btn.setObjectName(u"Connect_counter_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Connect_counter_btn.sizePolicy().hasHeightForWidth())
        self.Connect_counter_btn.setSizePolicy(sizePolicy1)
        self.Connect_counter_btn.setMinimumSize(QSize(150, 40))
        self.Connect_counter_btn.setMaximumSize(QSize(220, 16777215))
        self.Connect_counter_btn.setFont(font)
        self.Connect_counter_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_3.addWidget(self.Connect_counter_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.Input_scan_range_btn = QPushButton(self.centralwidget)
        self.Input_scan_range_btn.setObjectName(u"Input_scan_range_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Input_scan_range_btn.sizePolicy().hasHeightForWidth())
        self.Input_scan_range_btn.setSizePolicy(sizePolicy2)
        self.Input_scan_range_btn.setMinimumSize(QSize(180, 40))
        self.Input_scan_range_btn.setMaximumSize(QSize(250, 16777215))
        palette1 = QPalette()
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        brush6 = QBrush(QColor(0, 170, 127, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush6)
        brush7 = QBrush(QColor(208, 113, 87, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Input_scan_range_btn.setPalette(palette1)
        self.Input_scan_range_btn.setFont(font)
        self.Input_scan_range_btn.setStyleSheet(u"\n"
"QPushButton{background-color: rgb(0, 170, 127);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 3"
                        "3);}")

        self.horizontalLayout_3.addWidget(self.Input_scan_range_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.Plot_box = QGroupBox(self.centralwidget)
        self.Plot_box.setObjectName(u"Plot_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Plot_box.sizePolicy().hasHeightForWidth())
        self.Plot_box.setSizePolicy(sizePolicy3)
        self.Plot_box.setMinimumSize(QSize(900, 600))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(True)
        self.Plot_box.setFont(font3)
        self.Plot_box.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout.addWidget(self.Plot_box)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(900, 80))
        self.groupBox.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0882353 rgba(64, 252, 255, 200), stop:0.333333 rgba(119, 241, 255, 200), stop:0.588235 rgba(170, 255, 255, 200), stop:0.897059 rgba(190, 255, 244, 200));\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.Start_plot = QPushButton(self.groupBox)
        self.Start_plot.setObjectName(u"Start_plot")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Start_plot.sizePolicy().hasHeightForWidth())
        self.Start_plot.setSizePolicy(sizePolicy4)
        self.Start_plot.setMinimumSize(QSize(100, 60))
        palette2 = QPalette()
        brush8 = QBrush(QColor(255, 113, 84, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        brush9 = QBrush(QColor(35, 202, 166, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush5)
        brush10 = QBrush(QColor(127, 127, 127, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush10)
        brush11 = QBrush(QColor(170, 170, 170, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush9)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush12)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush7)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.Start_plot.setPalette(palette2)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.Start_plot.setFont(font4)
        self.Start_plot.setFocusPolicy(Qt.ClickFocus)
        self.Start_plot.setStyleSheet(u"\n"
"QPushButton{background-color:  rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 113, 84);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, "
                        "33);}")
        self.Start_plot.setCheckable(False)
        self.Start_plot.setAutoDefault(False)
        self.Start_plot.setFlat(False)

        self.horizontalLayout_5.addWidget(self.Start_plot)

        self.horizontalSpacer_8 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.Stop_plot = QPushButton(self.groupBox)
        self.Stop_plot.setObjectName(u"Stop_plot")
        sizePolicy4.setHeightForWidth(self.Stop_plot.sizePolicy().hasHeightForWidth())
        self.Stop_plot.setSizePolicy(sizePolicy4)
        self.Stop_plot.setMinimumSize(QSize(100, 60))
        self.Stop_plot.setFont(font4)
        self.Stop_plot.setFocusPolicy(Qt.WheelFocus)
        self.Stop_plot.setStyleSheet(u"QPushButton{background-color:  rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 117, 0) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_5.addWidget(self.Stop_plot)

        self.horizontalSpacer_9 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.Clear_Save = QPushButton(self.groupBox)
        self.Clear_Save.setObjectName(u"Clear_Save")
        sizePolicy4.setHeightForWidth(self.Clear_Save.sizePolicy().hasHeightForWidth())
        self.Clear_Save.setSizePolicy(sizePolicy4)
        self.Clear_Save.setMinimumSize(QSize(100, 60))
        self.Clear_Save.setFont(font4)
        self.Clear_Save.setStyleSheet(u"\n"
"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 113, 84);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 3"
                        "3);}\n"
"")

        self.horizontalLayout_5.addWidget(self.Clear_Save)

        self.horizontalSpacer_10 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.Caculate = QPushButton(self.groupBox)
        self.Caculate.setObjectName(u"Caculate")
        sizePolicy4.setHeightForWidth(self.Caculate.sizePolicy().hasHeightForWidth())
        self.Caculate.setSizePolicy(sizePolicy4)
        self.Caculate.setMinimumSize(QSize(100, 60))
        self.Caculate.setFont(font4)
        self.Caculate.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgb(255, 113, 84);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_5.addWidget(self.Caculate)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addWidget(self.groupBox)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Now_T = QLabel(self.centralwidget)
        self.Now_T.setObjectName(u"Now_T")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Now_T.sizePolicy().hasHeightForWidth())
        self.Now_T.setSizePolicy(sizePolicy5)
        self.Now_T.setMinimumSize(QSize(290, 30))
        self.Now_T.setMaximumSize(QSize(1000, 40))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        brush13 = QBrush(QColor(44, 213, 196, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Now_T.setPalette(palette3)
        self.Now_T.setFont(font)
        self.Now_T.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Now_T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.Now_T)

        self.Expect_FN_T = QLabel(self.centralwidget)
        self.Expect_FN_T.setObjectName(u"Expect_FN_T")
        sizePolicy5.setHeightForWidth(self.Expect_FN_T.sizePolicy().hasHeightForWidth())
        self.Expect_FN_T.setSizePolicy(sizePolicy5)
        self.Expect_FN_T.setMinimumSize(QSize(290, 30))
        self.Expect_FN_T.setMaximumSize(QSize(1000, 40))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Expect_FN_T.setPalette(palette4)
        self.Expect_FN_T.setFont(font)
        self.Expect_FN_T.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Expect_FN_T.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.Expect_FN_T)

        self.Done_time = QLabel(self.centralwidget)
        self.Done_time.setObjectName(u"Done_time")
        sizePolicy5.setHeightForWidth(self.Done_time.sizePolicy().hasHeightForWidth())
        self.Done_time.setSizePolicy(sizePolicy5)
        self.Done_time.setMinimumSize(QSize(290, 30))
        self.Done_time.setMaximumSize(QSize(1000, 40))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Done_time.setPalette(palette5)
        self.Done_time.setFont(font)
        self.Done_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Done_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.Done_time)


        self.verticalLayout.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Select_instruments = QTabWidget(self.centralwidget)
        self.Select_instruments.setObjectName(u"Select_instruments")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Select_instruments.sizePolicy().hasHeightForWidth())
        self.Select_instruments.setSizePolicy(sizePolicy6)
        self.Select_instruments.setMaximumSize(QSize(450, 800))
        palette6 = QPalette()
        brush14 = QBrush(QColor(255, 85, 0, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        brush15 = QBrush(QColor(255, 85, 0, 128))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Select_instruments.setPalette(palette6)
        self.Select_instruments.setFont(font)
        self.Select_instruments.setTabPosition(QTabWidget.North)
        self.Select_instruments.setTabShape(QTabWidget.Rounded)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.PD_plot_pAmeter = QGroupBox(self.tab_4)
        self.PD_plot_pAmeter.setObjectName(u"PD_plot_pAmeter")
        sizePolicy6.setHeightForWidth(self.PD_plot_pAmeter.sizePolicy().hasHeightForWidth())
        self.PD_plot_pAmeter.setSizePolicy(sizePolicy6)
        self.PD_plot_pAmeter.setMinimumSize(QSize(400, 200))
        self.PD_plot_pAmeter.setMaximumSize(QSize(400, 16777215))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.PD_plot_pAmeter.setPalette(palette7)
        self.PD_plot_pAmeter.setFont(font1)

        self.verticalLayout_2.addWidget(self.PD_plot_pAmeter)

        self.Adc_box_2 = QGroupBox(self.tab_4)
        self.Adc_box_2.setObjectName(u"Adc_box_2")
        sizePolicy4.setHeightForWidth(self.Adc_box_2.sizePolicy().hasHeightForWidth())
        self.Adc_box_2.setSizePolicy(sizePolicy4)
        self.Adc_box_2.setMinimumSize(QSize(400, 125))
        self.Adc_box_2.setMaximumSize(QSize(400, 16777215))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_2.setPalette(palette8)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.Adc_box_2.setFont(font5)
        self.gridLayout = QGridLayout(self.Adc_box_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.lcd_PD_pA = QLCDNumber(self.Adc_box_2)
        self.lcd_PD_pA.setObjectName(u"lcd_PD_pA")
        sizePolicy4.setHeightForWidth(self.lcd_PD_pA.sizePolicy().hasHeightForWidth())
        self.lcd_PD_pA.setSizePolicy(sizePolicy4)
        self.lcd_PD_pA.setMinimumSize(QSize(120, 30))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.lcd_PD_pA.setPalette(palette9)
        self.lcd_PD_pA.setDigitCount(8)
        self.lcd_PD_pA.setSegmentStyle(QLCDNumber.Filled)

        self.horizontalLayout_7.addWidget(self.lcd_PD_pA)

        self.label_3 = QLabel(self.Adc_box_2)
        self.label_3.setObjectName(u"label_3")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_3.setPalette(palette10)
        self.label_3.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_19)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_20 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_20)

        self.Monitor_PD_pA = QPushButton(self.Adc_box_2)
        self.Monitor_PD_pA.setObjectName(u"Monitor_PD_pA")
        sizePolicy6.setHeightForWidth(self.Monitor_PD_pA.sizePolicy().hasHeightForWidth())
        self.Monitor_PD_pA.setSizePolicy(sizePolicy6)
        self.Monitor_PD_pA.setMinimumSize(QSize(75, 40))
        self.Monitor_PD_pA.setFont(font1)
        self.Monitor_PD_pA.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.Monitor_PD_pA.setFlat(False)

        self.horizontalLayout_8.addWidget(self.Monitor_PD_pA)

        self.horizontalSpacer_21 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_21)

        self.Stop_Monitor_PD_pA = QPushButton(self.Adc_box_2)
        self.Stop_Monitor_PD_pA.setObjectName(u"Stop_Monitor_PD_pA")
        sizePolicy6.setHeightForWidth(self.Stop_Monitor_PD_pA.sizePolicy().hasHeightForWidth())
        self.Stop_Monitor_PD_pA.setSizePolicy(sizePolicy6)
        self.Stop_Monitor_PD_pA.setMinimumSize(QSize(75, 40))
        self.Stop_Monitor_PD_pA.setFont(font1)
        self.Stop_Monitor_PD_pA.setStyleSheet(u"QPushButton{background-color:  rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 85, 127) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(33, 190, 193);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);"
                        "}")

        self.horizontalLayout_8.addWidget(self.Stop_Monitor_PD_pA)

        self.horizontalSpacer_22 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_22)

        self.Clear_Monitor_PD_clear = QPushButton(self.Adc_box_2)
        self.Clear_Monitor_PD_clear.setObjectName(u"Clear_Monitor_PD_clear")
        sizePolicy6.setHeightForWidth(self.Clear_Monitor_PD_clear.sizePolicy().hasHeightForWidth())
        self.Clear_Monitor_PD_clear.setSizePolicy(sizePolicy6)
        self.Clear_Monitor_PD_clear.setMinimumSize(QSize(75, 40))
        self.Clear_Monitor_PD_clear.setFont(font1)
        self.Clear_Monitor_PD_clear.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_8.addWidget(self.Clear_Monitor_PD_clear)

        self.horizontalSpacer_23 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_23)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.Adc_box_2)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.Select_instruments.addTab(self.tab_4, "")

        self.verticalLayout_6.addWidget(self.Select_instruments)

        self.Monitor_pos = QTabWidget(self.centralwidget)
        self.Monitor_pos.setObjectName(u"Monitor_pos")
        sizePolicy6.setHeightForWidth(self.Monitor_pos.sizePolicy().hasHeightForWidth())
        self.Monitor_pos.setSizePolicy(sizePolicy6)
        self.Monitor_pos.setMinimumSize(QSize(430, 300))
        self.Monitor_pos.setMaximumSize(QSize(450, 800))
        self.Monitor_pos.setSizeIncrement(QSize(100, 100))
        self.Monitor_pos.setBaseSize(QSize(50, 50))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Monitor_pos.setPalette(palette11)
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.Monitor_pos.setFont(font6)
        self.Monitor_pos.setStyleSheet(u"")
        self.Monitor_pos.setTabPosition(QTabWidget.South)
        self.Monitor_pos.setTabShape(QTabWidget.Rounded)
        self.Monitor_pos.setUsesScrollButtons(False)
        self.Monitor_pos.setDocumentMode(False)
        self.Monitor_pos.setTabsClosable(False)
        self.Monitor_pos.setMovable(False)
        self.Monitor_pos.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.X_position = QGroupBox(self.tab_2)
        self.X_position.setObjectName(u"X_position")
        sizePolicy6.setHeightForWidth(self.X_position.sizePolicy().hasHeightForWidth())
        self.X_position.setSizePolicy(sizePolicy6)
        self.X_position.setMinimumSize(QSize(400, 150))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.X_position.setPalette(palette12)
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setItalic(True)
        font7.setStyleStrategy(QFont.PreferAntialias)
        self.X_position.setFont(font7)

        self.verticalLayout_5.addWidget(self.X_position)

        self.Adc_box_3 = QGroupBox(self.tab_2)
        self.Adc_box_3.setObjectName(u"Adc_box_3")
        sizePolicy4.setHeightForWidth(self.Adc_box_3.sizePolicy().hasHeightForWidth())
        self.Adc_box_3.setSizePolicy(sizePolicy4)
        self.Adc_box_3.setMinimumSize(QSize(400, 125))
        self.Adc_box_3.setMaximumSize(QSize(400, 16777215))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_3.setPalette(palette13)
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setStyleStrategy(QFont.PreferAntialias)
        self.Adc_box_3.setFont(font8)
        self.verticalLayout_4 = QVBoxLayout(self.Adc_box_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.lcd_X_pos = QLCDNumber(self.Adc_box_3)
        self.lcd_X_pos.setObjectName(u"lcd_X_pos")
        sizePolicy4.setHeightForWidth(self.lcd_X_pos.sizePolicy().hasHeightForWidth())
        self.lcd_X_pos.setSizePolicy(sizePolicy4)
        self.lcd_X_pos.setMinimumSize(QSize(120, 30))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.lcd_X_pos.setPalette(palette14)
        self.lcd_X_pos.setDigitCount(8)
        self.lcd_X_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_9.addWidget(self.lcd_X_pos)

        self.label_5 = QLabel(self.Adc_box_3)
        self.label_5.setObjectName(u"label_5")
        palette15 = QPalette()
        brush16 = QBrush(QColor(0, 170, 255, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush16)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush16)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_5.setPalette(palette15)
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setStyleStrategy(QFont.PreferAntialias)
        self.label_5.setFont(font9)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.X_pos_left = QPushButton(self.Adc_box_3)
        self.X_pos_left.setObjectName(u"X_pos_left")
        sizePolicy6.setHeightForWidth(self.X_pos_left.sizePolicy().hasHeightForWidth())
        self.X_pos_left.setSizePolicy(sizePolicy6)
        self.X_pos_left.setMinimumSize(QSize(60, 40))
        self.X_pos_left.setMaximumSize(QSize(16777215, 40))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush9)
        brush17 = QBrush(QColor(255, 85, 127, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.X_pos_left.setPalette(palette16)
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(28)
        font10.setBold(False)
        font10.setStyleStrategy(QFont.PreferDefault)
        self.X_pos_left.setFont(font10)
        self.X_pos_left.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.X_pos_left.setAutoDefault(False)
        self.X_pos_left.setFlat(False)

        self.horizontalLayout.addWidget(self.X_pos_left)

        self.Step_X_pos = QDoubleSpinBox(self.Adc_box_3)
        self.Step_X_pos.setObjectName(u"Step_X_pos")
        sizePolicy4.setHeightForWidth(self.Step_X_pos.sizePolicy().hasHeightForWidth())
        self.Step_X_pos.setSizePolicy(sizePolicy4)
        self.Step_X_pos.setMinimumSize(QSize(200, 40))
        self.Step_X_pos.setFont(font6)
        self.Step_X_pos.setInputMethodHints(Qt.ImhFormattedNumbersOnly|Qt.ImhNoAutoUppercase|Qt.ImhPreferNumbers)
        self.Step_X_pos.setAlignment(Qt.AlignCenter)
        self.Step_X_pos.setDecimals(1)
        self.Step_X_pos.setMinimum(0.100000000000000)
        self.Step_X_pos.setMaximum(10000.000000000000000)
        self.Step_X_pos.setSingleStep(1.000000000000000)
        self.Step_X_pos.setValue(0.500000000000000)

        self.horizontalLayout.addWidget(self.Step_X_pos)

        self.X_pos_right = QPushButton(self.Adc_box_3)
        self.X_pos_right.setObjectName(u"X_pos_right")
        sizePolicy6.setHeightForWidth(self.X_pos_right.sizePolicy().hasHeightForWidth())
        self.X_pos_right.setSizePolicy(sizePolicy6)
        self.X_pos_right.setMinimumSize(QSize(60, 40))
        self.X_pos_right.setMaximumSize(QSize(60, 40))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Active, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.X_pos_right.setPalette(palette17)
        self.X_pos_right.setFont(font10)
        self.X_pos_right.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout.addWidget(self.X_pos_right)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.Adc_box_3)


        self.gridLayout_4.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.Monitor_pos.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Z_position = QGroupBox(self.tab)
        self.Z_position.setObjectName(u"Z_position")
        sizePolicy6.setHeightForWidth(self.Z_position.sizePolicy().hasHeightForWidth())
        self.Z_position.setSizePolicy(sizePolicy6)
        self.Z_position.setMinimumSize(QSize(400, 150))
        palette18 = QPalette()
        brush18 = QBrush(QColor(255, 85, 255, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Z_position.setPalette(palette18)
        self.Z_position.setFont(font7)

        self.gridLayout_2.addWidget(self.Z_position, 0, 0, 1, 1)

        self.Adc_box_4 = QGroupBox(self.tab)
        self.Adc_box_4.setObjectName(u"Adc_box_4")
        sizePolicy4.setHeightForWidth(self.Adc_box_4.sizePolicy().hasHeightForWidth())
        self.Adc_box_4.setSizePolicy(sizePolicy4)
        self.Adc_box_4.setMinimumSize(QSize(400, 125))
        self.Adc_box_4.setMaximumSize(QSize(400, 16777215))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_4.setPalette(palette19)
        self.Adc_box_4.setFont(font8)
        self.verticalLayout_3 = QVBoxLayout(self.Adc_box_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.lcd_Z_pos = QLCDNumber(self.Adc_box_4)
        self.lcd_Z_pos.setObjectName(u"lcd_Z_pos")
        sizePolicy4.setHeightForWidth(self.lcd_Z_pos.sizePolicy().hasHeightForWidth())
        self.lcd_Z_pos.setSizePolicy(sizePolicy4)
        self.lcd_Z_pos.setMinimumSize(QSize(120, 30))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.lcd_Z_pos.setPalette(palette20)
        self.lcd_Z_pos.setDigitCount(8)

        self.horizontalLayout_6.addWidget(self.lcd_Z_pos)

        self.label_4 = QLabel(self.Adc_box_4)
        self.label_4.setObjectName(u"label_4")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_4.setPalette(palette21)
        self.label_4.setFont(font9)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Z_pos_left = QPushButton(self.Adc_box_4)
        self.Z_pos_left.setObjectName(u"Z_pos_left")
        sizePolicy6.setHeightForWidth(self.Z_pos_left.sizePolicy().hasHeightForWidth())
        self.Z_pos_left.setSizePolicy(sizePolicy6)
        self.Z_pos_left.setMinimumSize(QSize(60, 40))
        self.Z_pos_left.setMaximumSize(QSize(16777215, 40))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette22.setBrush(QPalette.Active, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette22.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette22.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Z_pos_left.setPalette(palette22)
        self.Z_pos_left.setFont(font10)
        self.Z_pos_left.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")
        self.Z_pos_left.setAutoDefault(False)
        self.Z_pos_left.setFlat(False)

        self.horizontalLayout_2.addWidget(self.Z_pos_left)

        self.Step_Z_pos = QDoubleSpinBox(self.Adc_box_4)
        self.Step_Z_pos.setObjectName(u"Step_Z_pos")
        sizePolicy4.setHeightForWidth(self.Step_Z_pos.sizePolicy().hasHeightForWidth())
        self.Step_Z_pos.setSizePolicy(sizePolicy4)
        self.Step_Z_pos.setMinimumSize(QSize(160, 40))
        self.Step_Z_pos.setMaximumSize(QSize(16777215, 40))
        self.Step_Z_pos.setFont(font6)
        self.Step_Z_pos.setInputMethodHints(Qt.ImhFormattedNumbersOnly|Qt.ImhNoAutoUppercase|Qt.ImhPreferNumbers)
        self.Step_Z_pos.setAlignment(Qt.AlignCenter)
        self.Step_Z_pos.setDecimals(1)
        self.Step_Z_pos.setMinimum(0.500000000000000)
        self.Step_Z_pos.setMaximum(10000.000000000000000)
        self.Step_Z_pos.setSingleStep(1.000000000000000)
        self.Step_Z_pos.setValue(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.Step_Z_pos)

        self.Z_pos_right = QPushButton(self.Adc_box_4)
        self.Z_pos_right.setObjectName(u"Z_pos_right")
        sizePolicy6.setHeightForWidth(self.Z_pos_right.sizePolicy().hasHeightForWidth())
        self.Z_pos_right.setSizePolicy(sizePolicy6)
        self.Z_pos_right.setMinimumSize(QSize(60, 40))
        self.Z_pos_right.setMaximumSize(QSize(16777215, 40))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette23.setBrush(QPalette.Active, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette23.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Z_pos_right.setPalette(palette23)
        self.Z_pos_right.setFont(font10)
        self.Z_pos_right.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_2.addWidget(self.Z_pos_right)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.Adc_box_4, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.Monitor_pos.addTab(self.tab, "")

        self.verticalLayout_6.addWidget(self.Monitor_pos)

        self.Msg_box = QTextBrowser(self.centralwidget)
        self.Msg_box.setObjectName(u"Msg_box")
        self.Msg_box.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Msg_box.sizePolicy().hasHeightForWidth())
        self.Msg_box.setSizePolicy(sizePolicy7)
        self.Msg_box.setMinimumSize(QSize(430, 100))
        self.Msg_box.setMaximumSize(QSize(450, 200))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.Text, brush6)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.NoBrush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush19)
        brush20 = QBrush(QColor(0, 170, 255, 128))
        brush20.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        brush21 = QBrush(QColor(0, 0, 0, 255))
        brush21.setStyle(Qt.NoBrush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush21)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush22 = QBrush(QColor(0, 0, 0, 255))
        brush22.setStyle(Qt.NoBrush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Msg_box.setPalette(palette24)
        self.Msg_box.setFont(font)
        self.Msg_box.setStyleSheet(u"background-image:url(:/icons/icons/my_style_signature.png)\n"
"")

        self.verticalLayout_6.addWidget(self.Msg_box)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 28))
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy8)
        self.menubar.setMinimumSize(QSize(0, 0))
        self.menubar.setSizeIncrement(QSize(0, 0))
        self.menubar.setBaseSize(QSize(0, 0))
        palette25 = QPalette()
        self.menubar.setPalette(palette25)
        self.menubar.setFont(font)
        self.menubar.setDefaultUp(False)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setGeometry(QRect(342, 306, 163, 100))
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.menuMenu.sizePolicy().hasHeightForWidth())
        self.menuMenu.setSizePolicy(sizePolicy9)
        self.menuMenu.setMinimumSize(QSize(120, 50))
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(12)
        font11.setBold(False)
        self.menuMenu.setFont(font11)
        self.menuAnalysis = QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.Text, brush6)
        brush23 = QBrush(QColor(0, 170, 127, 128))
        brush23.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush23)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush23)
#endif
        brush24 = QBrush(QColor(109, 109, 109, 255))
        brush24.setStyle(Qt.SolidPattern)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush24)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.menuAnalysis.setPalette(palette26)
        self.menuAnalysis.setFont(font11)
        self.menuInstrument = QMenu(self.menubar)
        self.menuInstrument.setObjectName(u"menuInstrument")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.Text, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush23)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush23)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush24)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.menuInstrument.setPalette(palette27)
        self.menuInstrument.setFont(font11)
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuInstrument.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuAnalysis.addAction(self.actionView_data)
        self.menuAnalysis.addAction(self.actionDatabase)
        self.menuInstrument.addAction(self.actionPD_ADC)
        self.menuInstrument.addAction(self.actionpAmeter)

        self.retranslateUi(MainWindow)

        self.Start_plot.setDefault(False)
        self.Select_instruments.setCurrentIndex(0)
        self.Monitor_pos.setCurrentIndex(1)
        self.X_pos_left.setDefault(False)
        self.Z_pos_left.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionView_data.setText(QCoreApplication.translate("MainWindow", u"View data", None))
        self.actionPD_ADC.setText(QCoreApplication.translate("MainWindow", u"PD_ADC", None))
        self.actionpAmeter.setText(QCoreApplication.translate("MainWindow", u"pAmeter", None))
        self.actionDatabase.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.Channel_cbx.setItemText(0, QCoreApplication.translate("MainWindow", u"Axis_X", None))
        self.Channel_cbx.setItemText(1, QCoreApplication.translate("MainWindow", u"Axis_Y", None))

#if QT_CONFIG(tooltip)
        self.Connect_counter_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect EPICS PVs for Energy and Grating motion ", None))
#endif // QT_CONFIG(tooltip)
        self.Connect_counter_btn.setText(QCoreApplication.translate("MainWindow", u"Electrometer", None))
        self.Input_scan_range_btn.setText(QCoreApplication.translate("MainWindow", u"Input Scan Range", None))
#if QT_CONFIG(statustip)
        self.Plot_box.setStatusTip(QCoreApplication.translate("MainWindow", u"Plot_area", None))
#endif // QT_CONFIG(statustip)
        self.Plot_box.setTitle(QCoreApplication.translate("MainWindow", u"BeamSize_plot", None))
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.Start_plot.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Start_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"begin scan,should choose scan mode and scan range", None))
#endif // QT_CONFIG(statustip)
        self.Start_plot.setText(QCoreApplication.translate("MainWindow", u"Start_plot", None))
#if QT_CONFIG(tooltip)
        self.Stop_plot.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Stop_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"Stop scan", None))
#endif // QT_CONFIG(statustip)
        self.Stop_plot.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.Clear_Save.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Clear_Save.setStatusTip(QCoreApplication.translate("MainWindow", u"Clear data in the plot and save ", None))
#endif // QT_CONFIG(statustip)
        self.Clear_Save.setText(QCoreApplication.translate("MainWindow", u"Clear+Save", None))
#if QT_CONFIG(tooltip)
        self.Caculate.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Caculate.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate fit", None))
#endif // QT_CONFIG(statustip)
        self.Caculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.Now_T.setText(QCoreApplication.translate("MainWindow", u"Now", None))
        self.Expect_FN_T.setText("")
        self.Done_time.setText("")
        self.PD_plot_pAmeter.setTitle(QCoreApplication.translate("MainWindow", u"pA_plot", None))
        self.Adc_box_2.setTitle(QCoreApplication.translate("MainWindow", u"pA 6517B", None))
#if QT_CONFIG(tooltip)
        self.lcd_PD_pA.setToolTip(QCoreApplication.translate("MainWindow", u"read value", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"pA", None))
        self.Monitor_PD_pA.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.Stop_Monitor_PD_pA.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Clear_Monitor_PD_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Select_instruments.setTabText(self.Select_instruments.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"pAmeter", None))
        self.X_position.setTitle(QCoreApplication.translate("MainWindow", u"X_position", None))
        self.Adc_box_3.setTitle(QCoreApplication.translate("MainWindow", u"X_set", None))
#if QT_CONFIG(tooltip)
        self.lcd_X_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current X position", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"um", None))
        self.X_pos_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(tooltip)
        self.Step_X_pos.setToolTip(QCoreApplication.translate("MainWindow", u"Each Step size X", None))
#endif // QT_CONFIG(tooltip)
        self.Step_X_pos.setSuffix(QCoreApplication.translate("MainWindow", u" um", None))
        self.X_pos_right.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.Monitor_pos.setTabText(self.Monitor_pos.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"X_axis", None))
        self.Z_position.setTitle(QCoreApplication.translate("MainWindow", u"Z_position", None))
        self.Adc_box_4.setTitle(QCoreApplication.translate("MainWindow", u"Z_set", None))
#if QT_CONFIG(tooltip)
        self.lcd_Z_pos.setToolTip(QCoreApplication.translate("MainWindow", u"current Z position", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"um", None))
#if QT_CONFIG(tooltip)
        self.Z_pos_left.setToolTip(QCoreApplication.translate("MainWindow", u"Decrease", None))
#endif // QT_CONFIG(tooltip)
        self.Z_pos_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(tooltip)
        self.Step_Z_pos.setToolTip(QCoreApplication.translate("MainWindow", u"Each Step size Z", None))
#endif // QT_CONFIG(tooltip)
        self.Step_Z_pos.setPrefix("")
        self.Step_Z_pos.setSuffix(QCoreApplication.translate("MainWindow", u" um", None))
#if QT_CONFIG(tooltip)
        self.Z_pos_right.setToolTip(QCoreApplication.translate("MainWindow", u"Increase", None))
#endif // QT_CONFIG(tooltip)
        self.Z_pos_right.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.Monitor_pos.setTabText(self.Monitor_pos.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Z_axis", None))
        self.Msg_box.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt;&gt;</span></p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAnalysis.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuInstrument.setTitle(QCoreApplication.translate("MainWindow", u"Instrument", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

