# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layouts/base_project_main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_EMG = QtGui.QWidget()
        self.tab_EMG.setObjectName(_fromUtf8("tab_EMG"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_EMG)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayoutGraphStatus = QtGui.QVBoxLayout()
        self.verticalLayoutGraphStatus.setObjectName(_fromUtf8("verticalLayoutGraphStatus"))
        self.verticalLayoutGraph = QtGui.QVBoxLayout()
        self.verticalLayoutGraph.setObjectName(_fromUtf8("verticalLayoutGraph"))
        self.label_replace = QtGui.QLabel(self.tab_EMG)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_replace.sizePolicy().hasHeightForWidth())
        self.label_replace.setSizePolicy(sizePolicy)
        self.label_replace.setObjectName(_fromUtf8("label_replace"))
        self.verticalLayoutGraph.addWidget(self.label_replace)
        self.verticalLayoutGraphStatus.addLayout(self.verticalLayoutGraph)
        self.lbl_status = QtGui.QLabel(self.tab_EMG)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.verticalLayoutGraphStatus.addWidget(self.lbl_status)
        self.horizontalLayout_2.addLayout(self.verticalLayoutGraphStatus)
        self.label_replace.raise_()
        self.tabWidget.addTab(self.tab_EMG, _fromUtf8(""))
        self.tab_features = QtGui.QWidget()
        self.tab_features.setObjectName(_fromUtf8("tab_features"))
        self.tabWidget.addTab(self.tab_features, _fromUtf8(""))
        self.tab_classification = QtGui.QWidget()
        self.tab_classification.setObjectName(_fromUtf8("tab_classification"))
        self.tabWidget.addTab(self.tab_classification, _fromUtf8(""))
        self.tab_settings = QtGui.QWidget()
        self.tab_settings.setObjectName(_fromUtf8("tab_settings"))
        self.tabWidget.addTab(self.tab_settings, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuFunctions = QtGui.QMenu(self.menubar)
        self.menuFunctions.setObjectName(_fromUtf8("menuFunctions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayoutOptions = QtGui.QVBoxLayout()
        self.verticalLayoutOptions.setObjectName(_fromUtf8("verticalLayoutOptions"))
        self.lbl_options = QtGui.QLabel(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_options.sizePolicy().hasHeightForWidth())
        self.lbl_options.setSizePolicy(sizePolicy)
        self.lbl_options.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lbl_options.setObjectName(_fromUtf8("lbl_options"))
        self.verticalLayoutOptions.addWidget(self.lbl_options)
        self.verticalLayoutThreshould = QtGui.QVBoxLayout()
        self.verticalLayoutThreshould.setObjectName(_fromUtf8("verticalLayoutThreshould"))
        self.lbl_status_opt = QtGui.QLabel(self.dockWidgetContents)
        self.lbl_status_opt.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status_opt.setObjectName(_fromUtf8("lbl_status_opt"))
        self.verticalLayoutThreshould.addWidget(self.lbl_status_opt)
        self.label_acquiring_status = QtGui.QLabel(self.dockWidgetContents)
        self.label_acquiring_status.setObjectName(_fromUtf8("label_acquiring_status"))
        self.verticalLayoutThreshould.addWidget(self.label_acquiring_status)
        self.label_plotting_status = QtGui.QLabel(self.dockWidgetContents)
        self.label_plotting_status.setObjectName(_fromUtf8("label_plotting_status"))
        self.verticalLayoutThreshould.addWidget(self.label_plotting_status)
        self.label_processing_status = QtGui.QLabel(self.dockWidgetContents)
        self.label_processing_status.setObjectName(_fromUtf8("label_processing_status"))
        self.verticalLayoutThreshould.addWidget(self.label_processing_status)
        self.label_classification_status = QtGui.QLabel(self.dockWidgetContents)
        self.label_classification_status.setObjectName(_fromUtf8("label_classification_status"))
        self.verticalLayoutThreshould.addWidget(self.label_classification_status)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayoutThreshould.addItem(spacerItem)
        self.verticalLayoutCheckBoxes = QtGui.QVBoxLayout()
        self.verticalLayoutCheckBoxes.setObjectName(_fromUtf8("verticalLayoutCheckBoxes"))
        self.label_channels = QtGui.QLabel(self.dockWidgetContents)
        self.label_channels.setObjectName(_fromUtf8("label_channels"))
        self.verticalLayoutCheckBoxes.addWidget(self.label_channels)
        self.cb_ch1 = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_ch1.setObjectName(_fromUtf8("cb_ch1"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch1)
        self.cb_ch3 = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_ch3.setObjectName(_fromUtf8("cb_ch3"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch3)
        self.cb_ch4 = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_ch4.setObjectName(_fromUtf8("cb_ch4"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch4)
        self.cb_ch2 = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_ch2.setObjectName(_fromUtf8("cb_ch2"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch2)
        self.verticalLayoutThreshould.addLayout(self.verticalLayoutCheckBoxes)
        self.verticalLayoutOptions.addLayout(self.verticalLayoutThreshould)
        self.verticalLayout.addLayout(self.verticalLayoutOptions)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionSimples = QtGui.QAction(MainWindow)
        self.actionSimples.setObjectName(_fromUtf8("actionSimples"))
        self.actionIn_Plotter = QtGui.QAction(MainWindow)
        self.actionIn_Plotter.setObjectName(_fromUtf8("actionIn_Plotter"))
        self.actionThread = QtGui.QAction(MainWindow)
        self.actionThread.setObjectName(_fromUtf8("actionThread"))
        self.actionDesativado = QtGui.QAction(MainWindow)
        self.actionDesativado.setObjectName(_fromUtf8("actionDesativado"))
        self.actionStartAcquisition = QtGui.QAction(MainWindow)
        self.actionStartAcquisition.setCheckable(False)
        self.actionStartAcquisition.setObjectName(_fromUtf8("actionStartAcquisition"))
        self.actionStart_Recording = QtGui.QAction(MainWindow)
        self.actionStart_Recording.setObjectName(_fromUtf8("actionStart_Recording"))
        self.actionStop_Recording = QtGui.QAction(MainWindow)
        self.actionStop_Recording.setObjectName(_fromUtf8("actionStop_Recording"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuArquivo.addAction(self.actionStart_Recording)
        self.menuArquivo.addAction(self.actionStop_Recording)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFunctions.addAction(self.actionStartAcquisition)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuFunctions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Main", None))
        self.label_replace.setText(_translate("MainWindow", "Here will be the chart", None))
        self.lbl_status.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_EMG), _translate("MainWindow", "EMG", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_features), _translate("MainWindow", "Features", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_classification), _translate("MainWindow", "Classification", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("MainWindow", "Settings", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuFunctions.setTitle(_translate("MainWindow", "Functions", None))
        self.lbl_options.setText(_translate("MainWindow", "Options:", None))
        self.lbl_status_opt.setText(_translate("MainWindow", "Status:", None))
        self.label_acquiring_status.setText(_translate("MainWindow", "Acquiring: Off", None))
        self.label_plotting_status.setText(_translate("MainWindow", "Plotting: Off", None))
        self.label_processing_status.setText(_translate("MainWindow", "Processing: Off", None))
        self.label_classification_status.setText(_translate("MainWindow", "Classification: Off", None))
        self.label_channels.setText(_translate("MainWindow", "Channels:", None))
        self.cb_ch1.setText(_translate("MainWindow", "CH1", None))
        self.cb_ch3.setText(_translate("MainWindow", "CH2", None))
        self.cb_ch4.setText(_translate("MainWindow", "CH3", None))
        self.cb_ch2.setText(_translate("MainWindow", "CH4", None))
        self.actionSimples.setText(_translate("MainWindow", "Processamento", None))
        self.actionIn_Plotter.setText(_translate("MainWindow", "In Plotter", None))
        self.actionThread.setText(_translate("MainWindow", "Thread", None))
        self.actionDesativado.setText(_translate("MainWindow", "Desativado", None))
        self.actionStartAcquisition.setText(_translate("MainWindow", "Start Acquisition", None))
        self.actionStart_Recording.setText(_translate("MainWindow", "Start Recording", None))
        self.actionStop_Recording.setText(_translate("MainWindow", "Stop Recording", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

