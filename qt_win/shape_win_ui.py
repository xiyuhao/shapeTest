# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:/gitHubDesktop/shapeTest/qt_win/shape_win.ui'
#
# Created: Thu Sep 21 21:06:55 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_shapeToolWin(object):
    def setupUi(self, shapeToolWin):
        shapeToolWin.setObjectName("shapeToolWin")
        shapeToolWin.resize(701, 458)
        self.centralwidget = QtGui.QWidget(shapeToolWin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.shapeToolGroupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.shapeToolGroupBox.setFont(font)
        self.shapeToolGroupBox.setObjectName("shapeToolGroupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.shapeToolGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.shapeToolListWidget = QtGui.QListWidget(self.shapeToolGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shapeToolListWidget.sizePolicy().hasHeightForWidth())
        self.shapeToolListWidget.setSizePolicy(sizePolicy)
        self.shapeToolListWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.shapeToolListWidget.setFont(font)
        self.shapeToolListWidget.setObjectName("shapeToolListWidget")
        QtGui.QListWidgetItem(self.shapeToolListWidget)
        QtGui.QListWidgetItem(self.shapeToolListWidget)
        QtGui.QListWidgetItem(self.shapeToolListWidget)
        QtGui.QListWidgetItem(self.shapeToolListWidget)
        QtGui.QListWidgetItem(self.shapeToolListWidget)
        QtGui.QListWidgetItem(self.shapeToolListWidget)
        self.horizontalLayout.addWidget(self.shapeToolListWidget)
        self.shapeToolStackedWidget = QtGui.QStackedWidget(self.shapeToolGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shapeToolStackedWidget.sizePolicy().hasHeightForWidth())
        self.shapeToolStackedWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.shapeToolStackedWidget.setFont(font)
        self.shapeToolStackedWidget.setObjectName("shapeToolStackedWidget")
        self.blendShapeTargetPage = QtGui.QWidget()
        self.blendShapeTargetPage.setObjectName("blendShapeTargetPage")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.blendShapeTargetPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.blendShapeTargetPage)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.blendShapeTargetNameTreeWidget = QtGui.QTreeWidget(self.blendShapeTargetPage)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.blendShapeTargetNameTreeWidget.setFont(font)
        self.blendShapeTargetNameTreeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.blendShapeTargetNameTreeWidget.setObjectName("blendShapeTargetNameTreeWidget")
        self.horizontalLayout_4.addWidget(self.blendShapeTargetNameTreeWidget)
        self.blendShapeTargetSelectPushButton = QtGui.QPushButton(self.blendShapeTargetPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blendShapeTargetSelectPushButton.sizePolicy().hasHeightForWidth())
        self.blendShapeTargetSelectPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.blendShapeTargetSelectPushButton.setFont(font)
        self.blendShapeTargetSelectPushButton.setObjectName("blendShapeTargetSelectPushButton")
        self.horizontalLayout_4.addWidget(self.blendShapeTargetSelectPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.blendShapeTargetLinkPushButton = QtGui.QPushButton(self.blendShapeTargetPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blendShapeTargetLinkPushButton.sizePolicy().hasHeightForWidth())
        self.blendShapeTargetLinkPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.blendShapeTargetLinkPushButton.setFont(font)
        self.blendShapeTargetLinkPushButton.setObjectName("blendShapeTargetLinkPushButton")
        self.horizontalLayout_2.addWidget(self.blendShapeTargetLinkPushButton)
        self.blendShapeTargetNoPushButton = QtGui.QPushButton(self.blendShapeTargetPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blendShapeTargetNoPushButton.sizePolicy().hasHeightForWidth())
        self.blendShapeTargetNoPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.blendShapeTargetNoPushButton.setFont(font)
        self.blendShapeTargetNoPushButton.setObjectName("blendShapeTargetNoPushButton")
        self.horizontalLayout_2.addWidget(self.blendShapeTargetNoPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.shapeToolStackedWidget.addWidget(self.blendShapeTargetPage)
        self.blendShapeImportPage = QtGui.QWidget()
        self.blendShapeImportPage.setObjectName("blendShapeImportPage")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.blendShapeImportPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(self.blendShapeImportPage)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.blendShapeImportPushButton = QtGui.QPushButton(self.blendShapeImportPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blendShapeImportPushButton.sizePolicy().hasHeightForWidth())
        self.blendShapeImportPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.blendShapeImportPushButton.setFont(font)
        self.blendShapeImportPushButton.setObjectName("blendShapeImportPushButton")
        self.horizontalLayout_3.addWidget(self.blendShapeImportPushButton)
        self.blendShapeExportPushButton = QtGui.QPushButton(self.blendShapeImportPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blendShapeExportPushButton.sizePolicy().hasHeightForWidth())
        self.blendShapeExportPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.blendShapeExportPushButton.setFont(font)
        self.blendShapeExportPushButton.setObjectName("blendShapeExportPushButton")
        self.horizontalLayout_3.addWidget(self.blendShapeExportPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.shapeToolStackedWidget.addWidget(self.blendShapeImportPage)
        self.blendShapeSplitPage = QtGui.QWidget()
        self.blendShapeSplitPage.setObjectName("blendShapeSplitPage")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.blendShapeSplitPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtGui.QLabel(self.blendShapeSplitPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitShapeCreatePushButton = QtGui.QPushButton(self.blendShapeSplitPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitShapeCreatePushButton.sizePolicy().hasHeightForWidth())
        self.splitShapeCreatePushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.splitShapeCreatePushButton.setFont(font)
        self.splitShapeCreatePushButton.setObjectName("splitShapeCreatePushButton")
        self.horizontalLayout_5.addWidget(self.splitShapeCreatePushButton)
        self.splitShapeSplitPushButton = QtGui.QPushButton(self.blendShapeSplitPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitShapeSplitPushButton.sizePolicy().hasHeightForWidth())
        self.splitShapeSplitPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.splitShapeSplitPushButton.setFont(font)
        self.splitShapeSplitPushButton.setObjectName("splitShapeSplitPushButton")
        self.horizontalLayout_5.addWidget(self.splitShapeSplitPushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.shapeToolStackedWidget.addWidget(self.blendShapeSplitPage)
        self.blendShapeUVPage = QtGui.QWidget()
        self.blendShapeUVPage.setObjectName("blendShapeUVPage")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.blendShapeUVPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtGui.QLabel(self.blendShapeUVPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.uvBlendShapeCreatePushButton = QtGui.QPushButton(self.blendShapeUVPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uvBlendShapeCreatePushButton.sizePolicy().hasHeightForWidth())
        self.uvBlendShapeCreatePushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.uvBlendShapeCreatePushButton.setFont(font)
        self.uvBlendShapeCreatePushButton.setObjectName("uvBlendShapeCreatePushButton")
        self.verticalLayout_5.addWidget(self.uvBlendShapeCreatePushButton)
        self.shapeToolStackedWidget.addWidget(self.blendShapeUVPage)
        self.blendShapeCalculatePage = QtGui.QWidget()
        self.blendShapeCalculatePage.setObjectName("blendShapeCalculatePage")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.blendShapeCalculatePage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtGui.QLabel(self.blendShapeCalculatePage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.calculateShapeTopPushButton = QtGui.QPushButton(self.blendShapeCalculatePage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculateShapeTopPushButton.sizePolicy().hasHeightForWidth())
        self.calculateShapeTopPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.calculateShapeTopPushButton.setFont(font)
        self.calculateShapeTopPushButton.setObjectName("calculateShapeTopPushButton")
        self.horizontalLayout_6.addWidget(self.calculateShapeTopPushButton)
        self.calculateShapeBottomPushButton = QtGui.QPushButton(self.blendShapeCalculatePage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculateShapeBottomPushButton.sizePolicy().hasHeightForWidth())
        self.calculateShapeBottomPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.calculateShapeBottomPushButton.setFont(font)
        self.calculateShapeBottomPushButton.setObjectName("calculateShapeBottomPushButton")
        self.horizontalLayout_6.addWidget(self.calculateShapeBottomPushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.shapeToolStackedWidget.addWidget(self.blendShapeCalculatePage)
        self.blendShapeOtherPage = QtGui.QWidget()
        self.blendShapeOtherPage.setObjectName("blendShapeOtherPage")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.blendShapeOtherPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtGui.QLabel(self.blendShapeOtherPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.otherShapeTransmitPushButton = QtGui.QPushButton(self.blendShapeOtherPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otherShapeTransmitPushButton.sizePolicy().hasHeightForWidth())
        self.otherShapeTransmitPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.otherShapeTransmitPushButton.setFont(font)
        self.otherShapeTransmitPushButton.setObjectName("otherShapeTransmitPushButton")
        self.gridLayout.addWidget(self.otherShapeTransmitPushButton, 0, 0, 1, 1)
        self.otherShapeMirroPushButton = QtGui.QPushButton(self.blendShapeOtherPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otherShapeMirroPushButton.sizePolicy().hasHeightForWidth())
        self.otherShapeMirroPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.otherShapeMirroPushButton.setFont(font)
        self.otherShapeMirroPushButton.setObjectName("otherShapeMirroPushButton")
        self.gridLayout.addWidget(self.otherShapeMirroPushButton, 0, 1, 1, 1)
        self.otherShapeCopyPushButton = QtGui.QPushButton(self.blendShapeOtherPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otherShapeCopyPushButton.sizePolicy().hasHeightForWidth())
        self.otherShapeCopyPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.otherShapeCopyPushButton.setFont(font)
        self.otherShapeCopyPushButton.setObjectName("otherShapeCopyPushButton")
        self.gridLayout.addWidget(self.otherShapeCopyPushButton, 1, 0, 1, 1)
        self.otherShapeReversePushButton = QtGui.QPushButton(self.blendShapeOtherPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otherShapeReversePushButton.sizePolicy().hasHeightForWidth())
        self.otherShapeReversePushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.otherShapeReversePushButton.setFont(font)
        self.otherShapeReversePushButton.setObjectName("otherShapeReversePushButton")
        self.gridLayout.addWidget(self.otherShapeReversePushButton, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.shapeToolStackedWidget.addWidget(self.blendShapeOtherPage)
        self.horizontalLayout.addWidget(self.shapeToolStackedWidget)
        self.verticalLayout.addWidget(self.shapeToolGroupBox)
        shapeToolWin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(shapeToolWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 23))
        self.menubar.setObjectName("menubar")
        shapeToolWin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(shapeToolWin)
        self.statusbar.setObjectName("statusbar")
        shapeToolWin.setStatusBar(self.statusbar)

        self.retranslateUi(shapeToolWin)
        self.shapeToolStackedWidget.setCurrentIndex(4)
        QtCore.QObject.connect(self.shapeToolListWidget, QtCore.SIGNAL("currentRowChanged(int)"), self.shapeToolStackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(shapeToolWin)

    def retranslateUi(self, shapeToolWin):
        shapeToolWin.setWindowTitle(QtGui.QApplication.translate("shapeToolWin", "Shape Tool Window", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("shapeToolWin", "                Some Tool For Maya Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.shapeToolGroupBox.setTitle(QtGui.QApplication.translate("shapeToolWin", "Shape Tool", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.shapeToolListWidget.isSortingEnabled()
        self.shapeToolListWidget.setSortingEnabled(False)
        self.shapeToolListWidget.item(0).setText(QtGui.QApplication.translate("shapeToolWin", "BlendShape Target", None, QtGui.QApplication.UnicodeUTF8))
        self.shapeToolListWidget.item(1).setText(QtGui.QApplication.translate("shapeToolWin", "BlendShape Import/Export", None, QtGui.QApplication.UnicodeUTF8))
        self.shapeToolListWidget.item(2).setText(QtGui.QApplication.translate("shapeToolWin", "Split Shap", None, QtGui.QApplication.UnicodeUTF8))
        self.shapeToolListWidget.item(3).setText(QtGui.QApplication.translate("shapeToolWin", "UV BlendShape", None, QtGui.QApplication.UnicodeUTF8))
        self.shapeToolListWidget.item(4).setText(QtGui.QApplication.translate("shapeToolWin", "Calculate Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.shapeToolListWidget.item(5).setText(QtGui.QApplication.translate("shapeToolWin", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.shapeToolListWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(QtGui.QApplication.translate("shapeToolWin", "If you delete the targets for blendShape , this tool can help you to find it", None, QtGui.QApplication.UnicodeUTF8))
        self.blendShapeTargetNameTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("shapeToolWin", "BlendShape Node", None, QtGui.QApplication.UnicodeUTF8))
        self.blendShapeTargetSelectPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.blendShapeTargetLinkPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Link", None, QtGui.QApplication.UnicodeUTF8))
        self.blendShapeTargetNoPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("shapeToolWin", "Import the targets shape or export", None, QtGui.QApplication.UnicodeUTF8))
        self.blendShapeImportPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.blendShapeExportPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("shapeToolWin", "Split Shape for skin weight", None, QtGui.QApplication.UnicodeUTF8))
        self.splitShapeCreatePushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.splitShapeSplitPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Split", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("shapeToolWin", "Create UV blendShape", None, QtGui.QApplication.UnicodeUTF8))
        self.uvBlendShapeCreatePushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("shapeToolWin", "Calculate the real shape", None, QtGui.QApplication.UnicodeUTF8))
        self.calculateShapeTopPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Top", None, QtGui.QApplication.UnicodeUTF8))
        self.calculateShapeBottomPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("shapeToolWin", "Other shape tool", None, QtGui.QApplication.UnicodeUTF8))
        self.otherShapeTransmitPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Transmit", None, QtGui.QApplication.UnicodeUTF8))
        self.otherShapeMirroPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.otherShapeCopyPushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.otherShapeReversePushButton.setText(QtGui.QApplication.translate("shapeToolWin", "Reverse", None, QtGui.QApplication.UnicodeUTF8))

