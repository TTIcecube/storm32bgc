# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NTLoggerTool_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wWindow(object):

    WINSCALE = 1.0

    def SCALE(self, scale):
        if( scale>=16777215 ): return scale
        return int(self.WINSCALE*scale)

    def setupUi(self, wWindow, winScale):
        self.WINSCALE = winScale

        wWindow.setObjectName("wWindow")
        wWindow.resize(self.SCALE(800), self.SCALE(600))
        wWindow.setMinimumSize(QtCore.QSize(self.SCALE(600), self.SCALE(300)))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/owdefault.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(wWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(self.SCALE(250), self.SCALE(180)))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layout1 = QtWidgets.QGridLayout()
        self.layout1.setContentsMargins(self.SCALE(-1), self.SCALE(-1), self.SCALE(-1), self.SCALE(3))
        self.layout1.setObjectName("layout1")
        self.wLogFileName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wLogFileName.sizePolicy().hasHeightForWidth())
        self.wLogFileName.setSizePolicy(sizePolicy)
        self.wLogFileName.setText("")
        self.wLogFileName.setObjectName("wLogFileName")
        self.layout1.addWidget(self.wLogFileName, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(self.SCALE(5), self.SCALE(20), QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout1.addItem(spacerItem, 0, 4, 1, 1)
        self.wProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.wProgressBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wProgressBar.sizePolicy().hasHeightForWidth())
        self.wProgressBar.setSizePolicy(sizePolicy)
        self.wProgressBar.setMinimumSize(QtCore.QSize(0, self.SCALE(19)))
        self.wProgressBar.setMaximumSize(QtCore.QSize(self.SCALE(100), self.SCALE(19)))
        self.wProgressBar.setProperty("value", 0)
        self.wProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.wProgressBar.setTextVisible(True)
        self.wProgressBar.setObjectName("wProgressBar")
        self.layout1.addWidget(self.wProgressBar, 0, 3, 1, 1)
        self.bLoad = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bLoad.sizePolicy().hasHeightForWidth())
        self.bLoad.setSizePolicy(sizePolicy)
        self.bLoad.setMinimumSize(QtCore.QSize(self.SCALE(65), 0))
        self.bLoad.setMaximumSize(QtCore.QSize(self.SCALE(65), 16777215))
        self.bLoad.setObjectName("bLoad")
        self.layout1.addWidget(self.bLoad, 0, 0, 1, 1)
        self.bSave = QtWidgets.QPushButton(self.centralwidget)
        self.bSave.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bSave.sizePolicy().hasHeightForWidth())
        self.bSave.setSizePolicy(sizePolicy)
        self.bSave.setMinimumSize(QtCore.QSize(self.SCALE(65), 0))
        self.bSave.setMaximumSize(QtCore.QSize(self.SCALE(65), 16777215))
        self.bSave.setObjectName("bSave")
        self.layout1.addWidget(self.bSave, 0, 1, 1, 1)
        self.bCancelLoad = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bCancelLoad.sizePolicy().hasHeightForWidth())
        self.bCancelLoad.setSizePolicy(sizePolicy)
        self.bCancelLoad.setMinimumSize(QtCore.QSize(self.SCALE(65), 0))
        self.bCancelLoad.setMaximumSize(QtCore.QSize(self.SCALE(65), 16777215))
        self.bCancelLoad.setObjectName("bCancelLoad")
        self.layout1.addWidget(self.bCancelLoad, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.layout1)
        self.wTab = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.wTab.setFont(font)
        self.wTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.wTab.setObjectName("wTab")
        self.wTraffic = QtWidgets.QWidget()
        self.wTraffic.setObjectName("wTraffic")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wTraffic)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bLoadTraffic = QtWidgets.QCheckBox(self.wTraffic)
        self.bLoadTraffic.setObjectName("bLoadTraffic")
        self.verticalLayout.addWidget(self.bLoadTraffic)
        self.wTrafficText = QtWidgets.QPlainTextEdit(self.wTraffic)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.wTrafficText.setFont(font)
        self.wTrafficText.setAcceptDrops(False)
        self.wTrafficText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wTrafficText.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wTrafficText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.wTrafficText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.wTrafficText.setUndoRedoEnabled(False)
        self.wTrafficText.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.wTrafficText.setReadOnly(True)
        self.wTrafficText.setCursorWidth(1)
        self.wTrafficText.setObjectName("wTrafficText")
        self.verticalLayout.addWidget(self.wTrafficText)
        self.wTab.addTab(self.wTraffic, "")
        self.wData = QtWidgets.QWidget()
        self.wData.setObjectName("wData")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wData)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wDataText = QtWidgets.QPlainTextEdit(self.wData)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.wDataText.setFont(font)
        self.wDataText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.wDataText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.wDataText.setUndoRedoEnabled(False)
        self.wDataText.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.wDataText.setReadOnly(True)
        self.wDataText.setObjectName("wDataText")
        self.verticalLayout_2.addWidget(self.wDataText)
        self.wTab.addTab(self.wData, "")
        self.wGraphic = QtWidgets.QWidget()
        self.wGraphic.setObjectName("wGraphic")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wGraphic)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(self.SCALE(2))
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wGraphCentralWidget = QtWidgets.QWidget(self.wGraphic)
        self.wGraphCentralWidget.setObjectName("wGraphCentralWidget")
        self.wGraphCentralWidgetLayout = QtWidgets.QVBoxLayout(self.wGraphCentralWidget)
        self.wGraphCentralWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.wGraphCentralWidgetLayout.setSpacing(0)
        self.wGraphCentralWidgetLayout.setObjectName("wGraphCentralWidgetLayout")
        self.widget = QtWidgets.QWidget(self.wGraphCentralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(self.SCALE(6), self.SCALE(3), self.SCALE(6), self.SCALE(3))
        self.verticalLayout_4.setSpacing(self.SCALE(6))
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.wGraphLegend = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wGraphLegend.sizePolicy().hasHeightForWidth())
        self.wGraphLegend.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wGraphLegend.setFont(font)
        self.wGraphLegend.setAutoFillBackground(False)
        self.wGraphLegend.setText("textlabel")
        self.wGraphLegend.setWordWrap(True)
        self.wGraphLegend.setObjectName("wGraphLegend")
        self.verticalLayout_4.addWidget(self.wGraphLegend)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.wGraphCursor = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wGraphCursor.sizePolicy().hasHeightForWidth())
        self.wGraphCursor.setSizePolicy(sizePolicy)
        self.wGraphCursor.setMinimumSize(QtCore.QSize(self.SCALE(160), 0))
        self.wGraphCursor.setMaximumSize(QtCore.QSize(self.SCALE(160), 16777215))
        self.wGraphCursor.setObjectName("wGraphCursor")
        self.horizontalLayout_4.addWidget(self.wGraphCursor)
        spacerItem1 = QtWidgets.QSpacerItem(self.SCALE(40), self.SCALE(20), QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.wGraphTimeLabel = QtWidgets.QLabel(self.widget)
        self.wGraphTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.wGraphTimeLabel.setObjectName("wGraphTimeLabel")
        self.horizontalLayout_4.addWidget(self.wGraphTimeLabel)
        spacerItem2 = QtWidgets.QSpacerItem(self.SCALE(40), self.SCALE(20), QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(self.SCALE(140), self.SCALE(20), QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.wGraphCentralWidgetLayout.addWidget(self.widget)
        self.wGraphArea = QtWidgets.QWidget(self.wGraphCentralWidget)
        self.wGraphArea.setObjectName("wGraphArea")
        self.wGraphAreaLayout = QtWidgets.QVBoxLayout(self.wGraphArea)
        self.wGraphAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.wGraphAreaLayout.setSpacing(0)
        self.wGraphAreaLayout.setObjectName("wGraphAreaLayout")
        self.wGraphCentralWidgetLayout.addWidget(self.wGraphArea)
        self.widget_2 = QtWidgets.QWidget(self.wGraphCentralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(self.SCALE(6), self.SCALE(3), self.SCALE(6), 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wGraphTimeSlider = QtWidgets.QSlider(self.widget_2)
        self.wGraphTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.wGraphTimeSlider.setObjectName("wGraphTimeSlider")
        self.horizontalLayout_2.addWidget(self.wGraphTimeSlider)
        self.wGraphCentralWidgetLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.wGraphCentralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(self.SCALE(6), self.SCALE(3), self.SCALE(6), self.SCALE(3))
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bPlaybackBegin = QtWidgets.QPushButton(self.widget_3)
        self.bPlaybackBegin.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bPlaybackBegin.sizePolicy().hasHeightForWidth())
        self.bPlaybackBegin.setSizePolicy(sizePolicy)
        self.bPlaybackBegin.setMinimumSize(QtCore.QSize(self.SCALE(23), 0))
        self.bPlaybackBegin.setMaximumSize(QtCore.QSize(self.SCALE(23), 16777215))
        self.bPlaybackBegin.setText("")
        self.bPlaybackBegin.setObjectName("bPlaybackBegin")
        self.horizontalLayout_3.addWidget(self.bPlaybackBegin)
        self.bPlaybackSkipBackward = QtWidgets.QPushButton(self.widget_3)
        self.bPlaybackSkipBackward.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bPlaybackSkipBackward.sizePolicy().hasHeightForWidth())
        self.bPlaybackSkipBackward.setSizePolicy(sizePolicy)
        self.bPlaybackSkipBackward.setMinimumSize(QtCore.QSize(self.SCALE(23), 0))
        self.bPlaybackSkipBackward.setMaximumSize(QtCore.QSize(self.SCALE(23), 16777215))
        self.bPlaybackSkipBackward.setText("")
        self.bPlaybackSkipBackward.setObjectName("bPlaybackSkipBackward")
        self.horizontalLayout_3.addWidget(self.bPlaybackSkipBackward)
        self.bPlaybackPlayStop = QtWidgets.QPushButton(self.widget_3)
        self.bPlaybackPlayStop.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bPlaybackPlayStop.sizePolicy().hasHeightForWidth())
        self.bPlaybackPlayStop.setSizePolicy(sizePolicy)
        self.bPlaybackPlayStop.setMinimumSize(QtCore.QSize(self.SCALE(23), 0))
        self.bPlaybackPlayStop.setMaximumSize(QtCore.QSize(self.SCALE(23), 16777215))
        self.bPlaybackPlayStop.setText("")
        self.bPlaybackPlayStop.setObjectName("bPlaybackPlayStop")
        self.horizontalLayout_3.addWidget(self.bPlaybackPlayStop)
        self.bPlaybackSkipForward = QtWidgets.QPushButton(self.widget_3)
        self.bPlaybackSkipForward.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bPlaybackSkipForward.sizePolicy().hasHeightForWidth())
        self.bPlaybackSkipForward.setSizePolicy(sizePolicy)
        self.bPlaybackSkipForward.setMinimumSize(QtCore.QSize(self.SCALE(23), 0))
        self.bPlaybackSkipForward.setMaximumSize(QtCore.QSize(self.SCALE(23), 16777215))
        self.bPlaybackSkipForward.setText("")
        self.bPlaybackSkipForward.setObjectName("bPlaybackSkipForward")
        self.horizontalLayout_3.addWidget(self.bPlaybackSkipForward)
        self.bPlaybackEnd = QtWidgets.QPushButton(self.widget_3)
        self.bPlaybackEnd.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bPlaybackEnd.sizePolicy().hasHeightForWidth())
        self.bPlaybackEnd.setSizePolicy(sizePolicy)
        self.bPlaybackEnd.setMinimumSize(QtCore.QSize(self.SCALE(23), 0))
        self.bPlaybackEnd.setMaximumSize(QtCore.QSize(self.SCALE(23), 16777215))
        self.bPlaybackEnd.setText("")
        self.bPlaybackEnd.setObjectName("bPlaybackEnd")
        self.horizontalLayout_3.addWidget(self.bPlaybackEnd)
        spacerItem4 = QtWidgets.QSpacerItem(self.SCALE(10), self.SCALE(20), QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.wPlaybackSpeedFactor = QtWidgets.QComboBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wPlaybackSpeedFactor.sizePolicy().hasHeightForWidth())
        self.wPlaybackSpeedFactor.setSizePolicy(sizePolicy)
        self.wPlaybackSpeedFactor.setMinimumSize(QtCore.QSize(self.SCALE(55), self.SCALE(21)))
        self.wPlaybackSpeedFactor.setMaximumSize(QtCore.QSize(self.SCALE(55), self.SCALE(21)))
        self.wPlaybackSpeedFactor.setObjectName("wPlaybackSpeedFactor")
        self.horizontalLayout_3.addWidget(self.wPlaybackSpeedFactor)
        spacerItem5 = QtWidgets.QSpacerItem(self.SCALE(40), self.SCALE(20), QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.bGraphZoom = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bGraphZoom.sizePolicy().hasHeightForWidth())
        self.bGraphZoom.setSizePolicy(sizePolicy)
        self.bGraphZoom.setMinimumSize(QtCore.QSize(self.SCALE(65), 0))
        self.bGraphZoom.setMaximumSize(QtCore.QSize(self.SCALE(65), 16777215))
        self.bGraphZoom.setObjectName("bGraphZoom")
        self.horizontalLayout_3.addWidget(self.bGraphZoom)
        self.wGraphZoomFactor = QtWidgets.QComboBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wGraphZoomFactor.sizePolicy().hasHeightForWidth())
        self.wGraphZoomFactor.setSizePolicy(sizePolicy)
        self.wGraphZoomFactor.setMinimumSize(QtCore.QSize(self.SCALE(65), self.SCALE(21)))
        self.wGraphZoomFactor.setMaximumSize(QtCore.QSize(self.SCALE(65), self.SCALE(21)))
        self.wGraphZoomFactor.setObjectName("wGraphZoomFactor")
        self.horizontalLayout_3.addWidget(self.wGraphZoomFactor)
        spacerItem6 = QtWidgets.QSpacerItem(self.SCALE(40), self.SCALE(20), QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.wGraphCentralWidgetLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.wGraphCentralWidget)
        self.wGraphSelectorWidget = QtWidgets.QWidget(self.wGraphic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wGraphSelectorWidget.sizePolicy().hasHeightForWidth())
        self.wGraphSelectorWidget.setSizePolicy(sizePolicy)
        self.wGraphSelectorWidget.setMinimumSize(QtCore.QSize(self.SCALE(160), 0))
        self.wGraphSelectorWidget.setMaximumSize(QtCore.QSize(self.SCALE(160), 16777215))
        self.wGraphSelectorWidget.setObjectName("wGraphSelectorWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wGraphSelectorWidget)
        self.verticalLayout_5.setContentsMargins(0, self.SCALE(6), 0, self.SCALE(1))
        self.verticalLayout_5.setSpacing(self.SCALE(6))
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.bGraphSelectorClear = QtWidgets.QPushButton(self.wGraphSelectorWidget)
        self.bGraphSelectorClear.setObjectName("bGraphSelectorClear")
        self.verticalLayout_5.addWidget(self.bGraphSelectorClear)
        self.wGraphSelectorList = QtWidgets.QListWidget(self.wGraphSelectorWidget)
        self.wGraphSelectorList.setMinimumSize(QtCore.QSize(self.SCALE(160), 0))
        self.wGraphSelectorList.setMaximumSize(QtCore.QSize(self.SCALE(200), 16777215))
        self.wGraphSelectorList.setObjectName("wGraphSelectorList")
        self.verticalLayout_5.addWidget(self.wGraphSelectorList)
        self.bGraphShowPoints = QtWidgets.QCheckBox(self.wGraphSelectorWidget)
        self.bGraphShowPoints.setObjectName("bGraphShowPoints")
        self.verticalLayout_5.addWidget(self.bGraphShowPoints)
        self.horizontalLayout.addWidget(self.wGraphSelectorWidget)
        self.wTab.addTab(self.wGraphic, "")
        self.verticalLayout_3.addWidget(self.wTab)
        wWindow.setCentralWidget(self.centralwidget)
        self.wMenu = QtWidgets.QMenuBar(wWindow)
        self.wMenu.setGeometry(QtCore.QRect(0, 0, self.SCALE(800), self.SCALE(21)))
        self.wMenu.setObjectName("wMenu")
        self.mFile = QtWidgets.QMenu(self.wMenu)
        self.mFile.setObjectName("mFile")
        self.menu = QtWidgets.QMenu(self.wMenu)
        self.menu.setObjectName("menu")
        wWindow.setMenuBar(self.wMenu)
        self.actionLoad = QtWidgets.QAction(wWindow)
        icon = QtGui.QIcon.fromTheme("window-new")
        self.actionLoad.setIcon(icon)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(wWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(wWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(wWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(wWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClear = QtWidgets.QAction(wWindow)
        self.actionClear.setEnabled(False)
        self.actionClear.setObjectName("actionClear")
        self.mFile.addAction(self.actionLoad)
        self.mFile.addAction(self.actionSave)
        self.mFile.addAction(self.actionClear)
        self.mFile.addSeparator()
        self.mFile.addAction(self.actionExit)
        self.menu.addAction(self.actionAbout)
        self.wMenu.addAction(self.mFile.menuAction())
        self.wMenu.addAction(self.menu.menuAction())

        self.retranslateUi(wWindow)
        self.wTab.setCurrentIndex(2)
        self.actionLoad.triggered.connect(wWindow.loadLogFile)
        self.actionSave.triggered.connect(wWindow.saveDataIntoFile)
        self.actionExit.triggered.connect(wWindow.close)
        self.bLoad.clicked.connect(wWindow.loadLogFile)
        self.bSave.clicked.connect(wWindow.saveDataIntoFile)
        self.bCancelLoad.clicked.connect(wWindow.loadLogFileCancel)
        self.actionAbout.triggered.connect(wWindow.openAbout)
        self.actionClear.triggered.connect(wWindow.clearLogFile)
        self.bGraphZoom.clicked.connect(wWindow.doGraphZoomFactor)
        QtCore.QMetaObject.connectSlotsByName(wWindow)
        wWindow.setTabOrder(self.wTab, self.wTrafficText)

    def retranslateUi(self, wWindow):
        _translate = QtCore.QCoreApplication.translate
        wWindow.setWindowTitle(_translate("wWindow", "NT DataLogger Tool"))
        self.bLoad.setText(_translate("wWindow", " Load"))
        self.bSave.setText(_translate("wWindow", " Save"))
        self.bCancelLoad.setText(_translate("wWindow", "Cancel"))
        self.bLoadTraffic.setText(_translate("wWindow", "load complete traffic"))
        self.wTab.setTabText(self.wTab.indexOf(self.wTraffic), _translate("wWindow", "Traffic"))
        self.wTab.setTabText(self.wTab.indexOf(self.wData), _translate("wWindow", "Data"))
        self.wGraphCursor.setText(_translate("wWindow", "TextLabel"))
        self.wGraphTimeLabel.setText(_translate("wWindow", "TextLabel"))
        self.label.setText(_translate("wWindow", "Speed"))
        self.bGraphZoom.setText(_translate("wWindow", "Zoom"))
        self.bGraphSelectorClear.setText(_translate("wWindow", "Clear All Selections"))
        self.bGraphShowPoints.setText(_translate("wWindow", "show points"))
        self.wTab.setTabText(self.wTab.indexOf(self.wGraphic), _translate("wWindow", "Graph"))
        self.mFile.setTitle(_translate("wWindow", "File"))
        self.menu.setTitle(_translate("wWindow", "?"))
        self.actionLoad.setText(_translate("wWindow", "Load ..."))
        self.actionSave.setText(_translate("wWindow", "Save ..."))
        self.actionSave_as.setText(_translate("wWindow", "Save as ..."))
        self.actionExit.setText(_translate("wWindow", "Exit"))
        self.actionAbout.setText(_translate("wWindow", "About ..."))
        self.actionClear.setText(_translate("wWindow", "Clear"))

import NTLoggerTool_qrc_rc
