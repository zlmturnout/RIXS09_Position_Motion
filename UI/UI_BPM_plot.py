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
        MainWindow.resize(1870, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1870, 900))
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
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_26)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 50))
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
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.Choose_PD_or_pA = QComboBox(self.centralwidget)
        self.Choose_PD_or_pA.addItem("")
        self.Choose_PD_or_pA.addItem("")
        self.Choose_PD_or_pA.setObjectName(u"Choose_PD_or_pA")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Choose_PD_or_pA.sizePolicy().hasHeightForWidth())
        self.Choose_PD_or_pA.setSizePolicy(sizePolicy1)
        self.Choose_PD_or_pA.setMinimumSize(QSize(160, 35))
        self.Choose_PD_or_pA.setMaximumSize(QSize(250, 16777215))
        palette1 = QPalette()
        brush5 = QBrush(QColor(7, 197, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush5)
        brush6 = QBrush(QColor(255, 85, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        self.Choose_PD_or_pA.setPalette(palette1)
        self.Choose_PD_or_pA.setFont(font)
        self.Choose_PD_or_pA.setLayoutDirection(Qt.LeftToRight)
        self.Choose_PD_or_pA.setStyleSheet(u"background-color:rgb(7, 197, 255);\n"
"border-radius:5px;\n"
"selection-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(7, 197, 255);\n"
"border-color: rgb(255, 0, 127);")
        self.Choose_PD_or_pA.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.Choose_PD_or_pA.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_10.addWidget(self.Choose_PD_or_pA)

        self.horizontalSpacer_17 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_17)

        self.Select_plot_axis = QComboBox(self.centralwidget)
        self.Select_plot_axis.addItem("")
        self.Select_plot_axis.addItem("")
        self.Select_plot_axis.setObjectName(u"Select_plot_axis")
        self.Select_plot_axis.setMinimumSize(QSize(160, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush5)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.Select_plot_axis.setPalette(palette2)
        self.Select_plot_axis.setFont(font)
        self.Select_plot_axis.setStyleSheet(u"background-color:rgb(7, 197, 255);\n"
"border-radius:5px;\n"
"selection-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(7, 197, 255);\n"
"border-color: rgb(255, 0, 127);\n"
"color:rgb(0, 0, 0)")

        self.horizontalLayout_10.addWidget(self.Select_plot_axis)

        self.Start_axis_monitor = QPushButton(self.centralwidget)
        self.Start_axis_monitor.setObjectName(u"Start_axis_monitor")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Start_axis_monitor.sizePolicy().hasHeightForWidth())
        self.Start_axis_monitor.setSizePolicy(sizePolicy2)
        self.Start_axis_monitor.setMinimumSize(QSize(180, 40))
        self.Start_axis_monitor.setMaximumSize(QSize(250, 16777215))
        self.Start_axis_monitor.setFont(font)
        self.Start_axis_monitor.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(0, 0, 0);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_10.addWidget(self.Start_axis_monitor)

        self.Input_scan_range_btn = QPushButton(self.centralwidget)
        self.Input_scan_range_btn.setObjectName(u"Input_scan_range_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Input_scan_range_btn.sizePolicy().hasHeightForWidth())
        self.Input_scan_range_btn.setSizePolicy(sizePolicy3)
        self.Input_scan_range_btn.setMinimumSize(QSize(200, 40))
        self.Input_scan_range_btn.setMaximumSize(QSize(250, 16777215))
        palette3 = QPalette()
        brush8 = QBrush(QColor(35, 202, 166, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush9 = QBrush(QColor(208, 113, 87, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush9)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush9)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush9)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.Input_scan_range_btn.setPalette(palette3)
        self.Input_scan_range_btn.setFont(font)
        self.Input_scan_range_btn.setStyleSheet(u"\n"
"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(208, 113, 87);color:rgbrgb(0, 0, 0);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33)"
                        ";}")

        self.horizontalLayout_10.addWidget(self.Input_scan_range_btn)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_27)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.Plot_box = QGroupBox(self.centralwidget)
        self.Plot_box.setObjectName(u"Plot_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Plot_box.sizePolicy().hasHeightForWidth())
        self.Plot_box.setSizePolicy(sizePolicy4)
        self.Plot_box.setMinimumSize(QSize(900, 600))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.Plot_box.setFont(font1)
        self.Plot_box.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout.addWidget(self.Plot_box)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(900, 80))
        self.groupBox.setStyleSheet(u"background-color:  rgba(52, 235, 198, 120);\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.Start_plot = QPushButton(self.groupBox)
        self.Start_plot.setObjectName(u"Start_plot")
        sizePolicy1.setHeightForWidth(self.Start_plot.sizePolicy().hasHeightForWidth())
        self.Start_plot.setSizePolicy(sizePolicy1)
        self.Start_plot.setMinimumSize(QSize(100, 60))
        palette4 = QPalette()
        brush13 = QBrush(QColor(255, 113, 84, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush8)
        brush14 = QBrush(QColor(255, 255, 255, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        brush15 = QBrush(QColor(127, 127, 127, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush15)
        brush16 = QBrush(QColor(170, 170, 170, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Active, QPalette.HighlightedText, brush9)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.Start_plot.setPalette(palette4)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.Start_plot.setFont(font2)
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
        sizePolicy1.setHeightForWidth(self.Stop_plot.sizePolicy().hasHeightForWidth())
        self.Stop_plot.setSizePolicy(sizePolicy1)
        self.Stop_plot.setMinimumSize(QSize(100, 60))
        self.Stop_plot.setFont(font2)
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
        sizePolicy1.setHeightForWidth(self.Clear_Save.sizePolicy().hasHeightForWidth())
        self.Clear_Save.setSizePolicy(sizePolicy1)
        self.Clear_Save.setMinimumSize(QSize(100, 60))
        self.Clear_Save.setFont(font2)
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
        sizePolicy1.setHeightForWidth(self.Caculate.sizePolicy().hasHeightForWidth())
        self.Caculate.setSizePolicy(sizePolicy1)
        self.Caculate.setMinimumSize(QSize(100, 60))
        self.Caculate.setFont(font2)
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
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        brush17 = QBrush(QColor(44, 213, 196, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.Now_T.setPalette(palette5)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.Now_T.setFont(font3)
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
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.Expect_FN_T.setPalette(palette6)
        self.Expect_FN_T.setFont(font3)
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
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.Done_time.setPalette(palette7)
        self.Done_time.setFont(font3)
        self.Done_time.setStyleSheet(u"background-color: rgb(44, 213, 196);\n"
"color:rgb(255, 255, 255)")
        self.Done_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.Done_time)


        self.verticalLayout.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_12.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Select_instruments = QTabWidget(self.centralwidget)
        self.Select_instruments.setObjectName(u"Select_instruments")
        sizePolicy1.setHeightForWidth(self.Select_instruments.sizePolicy().hasHeightForWidth())
        self.Select_instruments.setSizePolicy(sizePolicy1)
        self.Select_instruments.setMaximumSize(QSize(450, 800))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        brush18 = QBrush(QColor(255, 85, 0, 128))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Select_instruments.setPalette(palette8)
        self.Select_instruments.setFont(font3)
        self.Select_instruments.setTabPosition(QTabWidget.South)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.PD_plot_adc = QGroupBox(self.tab_3)
        self.PD_plot_adc.setObjectName(u"PD_plot_adc")
        sizePolicy1.setHeightForWidth(self.PD_plot_adc.sizePolicy().hasHeightForWidth())
        self.PD_plot_adc.setSizePolicy(sizePolicy1)
        self.PD_plot_adc.setMinimumSize(QSize(400, 400))
        self.PD_plot_adc.setMaximumSize(QSize(400, 16777215))
        palette9 = QPalette()
        brush19 = QBrush(QColor(0, 170, 255, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.PD_plot_adc.setPalette(palette9)
        self.PD_plot_adc.setFont(font)

        self.gridLayout_7.addWidget(self.PD_plot_adc, 0, 0, 1, 1)

        self.Adc_box = QGroupBox(self.tab_3)
        self.Adc_box.setObjectName(u"Adc_box")
        sizePolicy1.setHeightForWidth(self.Adc_box.sizePolicy().hasHeightForWidth())
        self.Adc_box.setSizePolicy(sizePolicy1)
        self.Adc_box.setMinimumSize(QSize(400, 125))
        self.Adc_box.setMaximumSize(QSize(400, 16777215))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box.setPalette(palette10)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.Adc_box.setFont(font4)
        self.gridLayout_2 = QGridLayout(self.Adc_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_13 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)

        self.Monitor_PD_adc = QPushButton(self.Adc_box)
        self.Monitor_PD_adc.setObjectName(u"Monitor_PD_adc")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Monitor_PD_adc.sizePolicy().hasHeightForWidth())
        self.Monitor_PD_adc.setSizePolicy(sizePolicy6)
        self.Monitor_PD_adc.setMinimumSize(QSize(75, 40))
        self.Monitor_PD_adc.setFont(font)
        self.Monitor_PD_adc.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_3.addWidget(self.Monitor_PD_adc)

        self.horizontalSpacer_14 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_14)

        self.Stop_Monitor_PD_adc = QPushButton(self.Adc_box)
        self.Stop_Monitor_PD_adc.setObjectName(u"Stop_Monitor_PD_adc")
        sizePolicy6.setHeightForWidth(self.Stop_Monitor_PD_adc.sizePolicy().hasHeightForWidth())
        self.Stop_Monitor_PD_adc.setSizePolicy(sizePolicy6)
        self.Stop_Monitor_PD_adc.setMinimumSize(QSize(75, 40))
        self.Stop_Monitor_PD_adc.setFont(font)
        self.Stop_Monitor_PD_adc.setStyleSheet(u"QPushButton{background-color:  rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 255, 255);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
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

        self.horizontalLayout_3.addWidget(self.Stop_Monitor_PD_adc)

        self.horizontalSpacer_15 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_15)

        self.Clear_Monitor_PD_adc = QPushButton(self.Adc_box)
        self.Clear_Monitor_PD_adc.setObjectName(u"Clear_Monitor_PD_adc")
        sizePolicy6.setHeightForWidth(self.Clear_Monitor_PD_adc.sizePolicy().hasHeightForWidth())
        self.Clear_Monitor_PD_adc.setSizePolicy(sizePolicy6)
        self.Clear_Monitor_PD_adc.setMinimumSize(QSize(75, 40))
        self.Clear_Monitor_PD_adc.setFont(font)
        self.Clear_Monitor_PD_adc.setStyleSheet(u"QPushButton{background-color: rgb(35, 202, 166);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color:rgb(255, 85, 127);border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"\n"
"QPushButton:hover{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-top-color: rgb(167, 167, 167);border-left-color: rgb(138, 138, 138);\n"
"border-right-color: rgb(56, 56, 56);\n"
"border-bottom-color: rgb(33, 33, 33);}\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);border:2px;border-radius:10px;padding:2px 4px;selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255) ;border-style:inset;border-bottom-color: rgb(167, 167, 167);border-right-color: rgb(138, 138, 138);\n"
"border-left-color: rgb(56, 56, 56);\n"
"border-top-color: rgb(33, 33, 33);}")

        self.horizontalLayout_3.addWidget(self.Clear_Monitor_PD_adc)

        self.horizontalSpacer_16 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ADC_channel = QComboBox(self.Adc_box)
        self.ADC_channel.addItem("")
        self.ADC_channel.addItem("")
        self.ADC_channel.addItem("")
        self.ADC_channel.addItem("")
        self.ADC_channel.addItem("")
        self.ADC_channel.addItem("")
        self.ADC_channel.addItem("")
        self.ADC_channel.addItem("")
        self.ADC_channel.setObjectName(u"ADC_channel")

        self.horizontalLayout_4.addWidget(self.ADC_channel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.lcd_PD_adc = QLCDNumber(self.Adc_box)
        self.lcd_PD_adc.setObjectName(u"lcd_PD_adc")
        sizePolicy6.setHeightForWidth(self.lcd_PD_adc.sizePolicy().hasHeightForWidth())
        self.lcd_PD_adc.setSizePolicy(sizePolicy6)
        self.lcd_PD_adc.setMinimumSize(QSize(120, 30))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.lcd_PD_adc.setPalette(palette11)
        self.lcd_PD_adc.setDigitCount(8)
        self.lcd_PD_adc.setSegmentStyle(QLCDNumber.Filled)

        self.horizontalLayout_4.addWidget(self.lcd_PD_adc)

        self.label = QLabel(self.Adc_box)
        self.label.setObjectName(u"label")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label.setPalette(palette12)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.ADC_ULrange = QComboBox(self.Adc_box)
        self.ADC_ULrange.addItem("")
        self.ADC_ULrange.addItem("")
        self.ADC_ULrange.addItem("")
        self.ADC_ULrange.addItem("")
        self.ADC_ULrange.setObjectName(u"ADC_ULrange")

        self.horizontalLayout_4.addWidget(self.ADC_ULrange)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.Select_ADC = QComboBox(self.Adc_box)
        self.Select_ADC.addItem("")
        self.Select_ADC.addItem("")
        self.Select_ADC.addItem("")
        self.Select_ADC.setObjectName(u"Select_ADC")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.Select_ADC.setFont(font5)

        self.gridLayout_2.addWidget(self.Select_ADC, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.Adc_box, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.Select_instruments.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.PD_plot_pAmeter = QGroupBox(self.tab_4)
        self.PD_plot_pAmeter.setObjectName(u"PD_plot_pAmeter")
        sizePolicy1.setHeightForWidth(self.PD_plot_pAmeter.sizePolicy().hasHeightForWidth())
        self.PD_plot_pAmeter.setSizePolicy(sizePolicy1)
        self.PD_plot_pAmeter.setMinimumSize(QSize(400, 400))
        self.PD_plot_pAmeter.setMaximumSize(QSize(400, 16777215))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.PD_plot_pAmeter.setPalette(palette13)
        self.PD_plot_pAmeter.setFont(font)

        self.verticalLayout_2.addWidget(self.PD_plot_pAmeter)

        self.Adc_box_2 = QGroupBox(self.tab_4)
        self.Adc_box_2.setObjectName(u"Adc_box_2")
        sizePolicy1.setHeightForWidth(self.Adc_box_2.sizePolicy().hasHeightForWidth())
        self.Adc_box_2.setSizePolicy(sizePolicy1)
        self.Adc_box_2.setMinimumSize(QSize(400, 125))
        self.Adc_box_2.setMaximumSize(QSize(400, 16777215))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_2.setPalette(palette14)
        self.Adc_box_2.setFont(font4)
        self.gridLayout = QGridLayout(self.Adc_box_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.lcd_PD_pA = QLCDNumber(self.Adc_box_2)
        self.lcd_PD_pA.setObjectName(u"lcd_PD_pA")
        sizePolicy1.setHeightForWidth(self.lcd_PD_pA.sizePolicy().hasHeightForWidth())
        self.lcd_PD_pA.setSizePolicy(sizePolicy1)
        self.lcd_PD_pA.setMinimumSize(QSize(120, 30))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.lcd_PD_pA.setPalette(palette15)
        self.lcd_PD_pA.setDigitCount(8)
        self.lcd_PD_pA.setSegmentStyle(QLCDNumber.Filled)

        self.horizontalLayout_7.addWidget(self.lcd_PD_pA)

        self.label_3 = QLabel(self.Adc_box_2)
        self.label_3.setObjectName(u"label_3")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_3.setPalette(palette16)
        self.label_3.setFont(font)

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
        self.Monitor_PD_pA.setFont(font)
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
        self.Stop_Monitor_PD_pA.setFont(font)
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
        self.Clear_Monitor_PD_clear.setFont(font)
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

        self.horizontalLayout_11.addWidget(self.Select_instruments)

        self.Monitor_pos = QTabWidget(self.centralwidget)
        self.Monitor_pos.setObjectName(u"Monitor_pos")
        sizePolicy1.setHeightForWidth(self.Monitor_pos.sizePolicy().hasHeightForWidth())
        self.Monitor_pos.setSizePolicy(sizePolicy1)
        self.Monitor_pos.setMinimumSize(QSize(430, 600))
        self.Monitor_pos.setMaximumSize(QSize(450, 800))
        self.Monitor_pos.setSizeIncrement(QSize(100, 100))
        self.Monitor_pos.setBaseSize(QSize(50, 50))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Monitor_pos.setPalette(palette17)
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
        sizePolicy1.setHeightForWidth(self.X_position.sizePolicy().hasHeightForWidth())
        self.X_position.setSizePolicy(sizePolicy1)
        self.X_position.setMinimumSize(QSize(400, 400))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.X_position.setPalette(palette18)
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
        sizePolicy1.setHeightForWidth(self.Adc_box_3.sizePolicy().hasHeightForWidth())
        self.Adc_box_3.setSizePolicy(sizePolicy1)
        self.Adc_box_3.setMinimumSize(QSize(400, 125))
        self.Adc_box_3.setMaximumSize(QSize(400, 16777215))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_3.setPalette(palette19)
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
        sizePolicy1.setHeightForWidth(self.lcd_X_pos.sizePolicy().hasHeightForWidth())
        self.lcd_X_pos.setSizePolicy(sizePolicy1)
        self.lcd_X_pos.setMinimumSize(QSize(120, 30))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.lcd_X_pos.setPalette(palette20)
        self.lcd_X_pos.setDigitCount(8)
        self.lcd_X_pos.setProperty("value", 0.000000000000000)

        self.horizontalLayout_9.addWidget(self.lcd_X_pos)

        self.label_5 = QLabel(self.Adc_box_3)
        self.label_5.setObjectName(u"label_5")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_5.setPalette(palette21)
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
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush20 = QBrush(QColor(255, 85, 127, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette22.setBrush(QPalette.Active, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.X_pos_left.setPalette(palette22)
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
        sizePolicy1.setHeightForWidth(self.Step_X_pos.sizePolicy().hasHeightForWidth())
        self.Step_X_pos.setSizePolicy(sizePolicy1)
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
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette23.setBrush(QPalette.Active, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette23.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.X_pos_right.setPalette(palette23)
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
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Z_position = QGroupBox(self.tab)
        self.Z_position.setObjectName(u"Z_position")
        sizePolicy1.setHeightForWidth(self.Z_position.sizePolicy().hasHeightForWidth())
        self.Z_position.setSizePolicy(sizePolicy1)
        self.Z_position.setMinimumSize(QSize(400, 400))
        palette24 = QPalette()
        brush21 = QBrush(QColor(255, 85, 255, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Z_position.setPalette(palette24)
        self.Z_position.setFont(font7)

        self.verticalLayout_6.addWidget(self.Z_position)

        self.Adc_box_4 = QGroupBox(self.tab)
        self.Adc_box_4.setObjectName(u"Adc_box_4")
        sizePolicy1.setHeightForWidth(self.Adc_box_4.sizePolicy().hasHeightForWidth())
        self.Adc_box_4.setSizePolicy(sizePolicy1)
        self.Adc_box_4.setMinimumSize(QSize(400, 125))
        self.Adc_box_4.setMaximumSize(QSize(400, 16777215))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.Adc_box_4.setPalette(palette25)
        self.Adc_box_4.setFont(font8)
        self.verticalLayout_3 = QVBoxLayout(self.Adc_box_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.lcd_Z_pos = QLCDNumber(self.Adc_box_4)
        self.lcd_Z_pos.setObjectName(u"lcd_Z_pos")
        sizePolicy1.setHeightForWidth(self.lcd_Z_pos.sizePolicy().hasHeightForWidth())
        self.lcd_Z_pos.setSizePolicy(sizePolicy1)
        self.lcd_Z_pos.setMinimumSize(QSize(120, 30))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.lcd_Z_pos.setPalette(palette26)
        self.lcd_Z_pos.setDigitCount(8)

        self.horizontalLayout_6.addWidget(self.lcd_Z_pos)

        self.label_4 = QLabel(self.Adc_box_4)
        self.label_4.setObjectName(u"label_4")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_4.setPalette(palette27)
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
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette28.setBrush(QPalette.Active, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.Z_pos_left.setPalette(palette28)
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
        sizePolicy1.setHeightForWidth(self.Step_Z_pos.sizePolicy().hasHeightForWidth())
        self.Step_Z_pos.setSizePolicy(sizePolicy1)
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
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette29.setBrush(QPalette.Active, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette29.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette29.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.Z_pos_right.setPalette(palette29)
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


        self.verticalLayout_6.addWidget(self.Adc_box_4)


        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.Monitor_pos.addTab(self.tab, "")

        self.horizontalLayout_11.addWidget(self.Monitor_pos)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.Msg_box = QTextBrowser(self.centralwidget)
        self.Msg_box.setObjectName(u"Msg_box")
        self.Msg_box.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.Msg_box.sizePolicy().hasHeightForWidth())
        self.Msg_box.setSizePolicy(sizePolicy4)
        self.Msg_box.setMinimumSize(QSize(470, 180))
        self.Msg_box.setMaximumSize(QSize(1000, 800))
        palette30 = QPalette()
        brush22 = QBrush(QColor(0, 170, 127, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush22)
        brush23 = QBrush(QColor(0, 0, 0, 255))
        brush23.setStyle(Qt.NoBrush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush23)
        brush24 = QBrush(QColor(0, 170, 255, 128))
        brush24.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush22)
        brush25 = QBrush(QColor(0, 0, 0, 255))
        brush25.setStyle(Qt.NoBrush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush25)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush26 = QBrush(QColor(0, 0, 0, 255))
        brush26.setStyle(Qt.NoBrush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Msg_box.setPalette(palette30)
        self.Msg_box.setFont(font3)
        self.Msg_box.setStyleSheet(u"background-image:url(:/icons/icons/my_style_signature.png)\n"
"")

        self.verticalLayout_7.addWidget(self.Msg_box)


        self.horizontalLayout_12.addLayout(self.verticalLayout_7)


        self.gridLayout_8.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1870, 28))
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy7)
        self.menubar.setMinimumSize(QSize(0, 0))
        self.menubar.setSizeIncrement(QSize(0, 0))
        self.menubar.setBaseSize(QSize(0, 0))
        palette31 = QPalette()
        self.menubar.setPalette(palette31)
        self.menubar.setFont(font3)
        self.menubar.setDefaultUp(False)
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setGeometry(QRect(286, 584, 140, 50))
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.menuMenu.sizePolicy().hasHeightForWidth())
        self.menuMenu.setSizePolicy(sizePolicy8)
        self.menuMenu.setMinimumSize(QSize(120, 50))
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(12)
        font11.setBold(False)
        self.menuMenu.setFont(font11)
        self.menuAnalysis = QMenu(self.menubar)
        self.menuAnalysis.setObjectName(u"menuAnalysis")
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.Text, brush22)
        brush27 = QBrush(QColor(0, 170, 127, 128))
        brush27.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush27)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush27)
#endif
        brush28 = QBrush(QColor(109, 109, 109, 255))
        brush28.setStyle(Qt.SolidPattern)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush28)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.menuAnalysis.setPalette(palette32)
        self.menuAnalysis.setFont(font11)
        self.menuInstrument = QMenu(self.menubar)
        self.menuInstrument.setObjectName(u"menuInstrument")
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.Text, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush27)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush27)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush28)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.menuInstrument.setPalette(palette33)
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
        self.Choose_PD_or_pA.currentIndexChanged.connect(self.Select_instruments.setCurrentIndex)
        self.Select_plot_axis.currentIndexChanged.connect(self.Monitor_pos.setCurrentIndex)

        self.Select_plot_axis.setCurrentIndex(0)
        self.Start_plot.setDefault(False)
        self.Select_instruments.setCurrentIndex(1)
        self.ADC_channel.setCurrentIndex(0)
        self.ADC_ULrange.setCurrentIndex(0)
        self.Select_ADC.setCurrentIndex(0)
        self.Monitor_pos.setCurrentIndex(0)
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Scan Mode", None))
        self.Choose_PD_or_pA.setItemText(0, QCoreApplication.translate("MainWindow", u"Use PD ADC", None))
        self.Choose_PD_or_pA.setItemText(1, QCoreApplication.translate("MainWindow", u"Use pAmeter", None))

        self.Select_plot_axis.setItemText(0, QCoreApplication.translate("MainWindow", u"Move_X_axis", None))
        self.Select_plot_axis.setItemText(1, QCoreApplication.translate("MainWindow", u"Move_Z_axis", None))

#if QT_CONFIG(tooltip)
        self.Select_plot_axis.setToolTip(QCoreApplication.translate("MainWindow", u"Choose which axis to move", None))
#endif // QT_CONFIG(tooltip)
        self.Start_axis_monitor.setText(QCoreApplication.translate("MainWindow", u"X/Z axis monitor", None))
        self.Input_scan_range_btn.setText(QCoreApplication.translate("MainWindow", u"Input Scan Range", None))
#if QT_CONFIG(statustip)
        self.Plot_box.setStatusTip(QCoreApplication.translate("MainWindow", u"Plot_area", None))
#endif // QT_CONFIG(statustip)
        self.Plot_box.setTitle(QCoreApplication.translate("MainWindow", u"BPM_plot", None))
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
        self.PD_plot_adc.setTitle(QCoreApplication.translate("MainWindow", u"PD_plot", None))
        self.Adc_box.setTitle(QCoreApplication.translate("MainWindow", u"ADC_PD", None))
        self.Monitor_PD_adc.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.Stop_Monitor_PD_adc.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Clear_Monitor_PD_adc.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.ADC_channel.setItemText(0, QCoreApplication.translate("MainWindow", u"Channel 0", None))
        self.ADC_channel.setItemText(1, QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.ADC_channel.setItemText(2, QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.ADC_channel.setItemText(3, QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.ADC_channel.setItemText(4, QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.ADC_channel.setItemText(5, QCoreApplication.translate("MainWindow", u"Channel 5", None))
        self.ADC_channel.setItemText(6, QCoreApplication.translate("MainWindow", u"Channel 6", None))
        self.ADC_channel.setItemText(7, QCoreApplication.translate("MainWindow", u"Channel 7", None))

#if QT_CONFIG(tooltip)
        self.ADC_channel.setToolTip(QCoreApplication.translate("MainWindow", u"select channel", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lcd_PD_adc.setToolTip(QCoreApplication.translate("MainWindow", u"read value", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.ADC_ULrange.setItemText(0, QCoreApplication.translate("MainWindow", u"BIP1V", None))
        self.ADC_ULrange.setItemText(1, QCoreApplication.translate("MainWindow", u"BIP2V", None))
        self.ADC_ULrange.setItemText(2, QCoreApplication.translate("MainWindow", u"BIP5V", None))
        self.ADC_ULrange.setItemText(3, QCoreApplication.translate("MainWindow", u"BIP10V", None))

#if QT_CONFIG(tooltip)
        self.ADC_ULrange.setToolTip(QCoreApplication.translate("MainWindow", u"UL_range", None))
#endif // QT_CONFIG(tooltip)
        self.Select_ADC.setItemText(0, QCoreApplication.translate("MainWindow", u"Ion-ADC", None))
        self.Select_ADC.setItemText(1, QCoreApplication.translate("MainWindow", u"RXES-ADC", None))
        self.Select_ADC.setItemText(2, QCoreApplication.translate("MainWindow", u"QREXS-ADC", None))

        self.Select_instruments.setTabText(self.Select_instruments.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"PD ADC", None))
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

