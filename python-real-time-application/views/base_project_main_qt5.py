# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layouts/base_project_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_EMG = QtWidgets.QWidget()
        self.tab_EMG.setObjectName("tab_EMG")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_EMG)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayoutGraphStatus = QtWidgets.QVBoxLayout()
        self.verticalLayoutGraphStatus.setObjectName("verticalLayoutGraphStatus")
        self.verticalLayoutGraph = QtWidgets.QVBoxLayout()
        self.verticalLayoutGraph.setObjectName("verticalLayoutGraph")
        self.label_replace = QtWidgets.QLabel(self.tab_EMG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_replace.sizePolicy().hasHeightForWidth())
        self.label_replace.setSizePolicy(sizePolicy)
        self.label_replace.setObjectName("label_replace")
        self.verticalLayoutGraph.addWidget(self.label_replace)
        self.verticalLayoutGraphStatus.addLayout(self.verticalLayoutGraph)
        self.lbl_status = QtWidgets.QLabel(self.tab_EMG)
        self.lbl_status.setObjectName("lbl_status")
        self.verticalLayoutGraphStatus.addWidget(self.lbl_status)
        self.horizontalLayout_2.addLayout(self.verticalLayoutGraphStatus)
        self.label_replace.raise_()
        self.tabWidget.addTab(self.tab_EMG, "")
        self.tab_features = QtWidgets.QWidget()
        self.tab_features.setObjectName("tab_features")
        self.tabWidget.addTab(self.tab_features, "")
        self.tab_classification = QtWidgets.QWidget()
        self.tab_classification.setObjectName("tab_classification")
        self.tabWidget.addTab(self.tab_classification, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFunctions = QtWidgets.QMenu(self.menubar)
        self.menuFunctions.setObjectName("menuFunctions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutOptions = QtWidgets.QVBoxLayout()
        self.verticalLayoutOptions.setObjectName("verticalLayoutOptions")
        self.lbl_options = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_options.sizePolicy().hasHeightForWidth())
        self.lbl_options.setSizePolicy(sizePolicy)
        self.lbl_options.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lbl_options.setObjectName("lbl_options")
        self.verticalLayoutOptions.addWidget(self.lbl_options)
        self.verticalLayoutThreshould = QtWidgets.QVBoxLayout()
        self.verticalLayoutThreshould.setObjectName("verticalLayoutThreshould")
        self.lbl_status_opt = QtWidgets.QLabel(self.dockWidgetContents)
        self.lbl_status_opt.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status_opt.setObjectName("lbl_status_opt")
        self.verticalLayoutThreshould.addWidget(self.lbl_status_opt)
        self.label_acquiring_status = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_acquiring_status.setObjectName("label_acquiring_status")
        self.verticalLayoutThreshould.addWidget(self.label_acquiring_status)
        self.label_plotting_status = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_plotting_status.setObjectName("label_plotting_status")
        self.verticalLayoutThreshould.addWidget(self.label_plotting_status)
        self.label_processing_status = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_processing_status.setObjectName("label_processing_status")
        self.verticalLayoutThreshould.addWidget(self.label_processing_status)
        self.label_classification_status = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_classification_status.setObjectName("label_classification_status")
        self.verticalLayoutThreshould.addWidget(self.label_classification_status)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutThreshould.addItem(spacerItem)
        self.verticalLayoutCheckBoxes = QtWidgets.QVBoxLayout()
        self.verticalLayoutCheckBoxes.setObjectName("verticalLayoutCheckBoxes")
        self.label_channels = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_channels.setObjectName("label_channels")
        self.verticalLayoutCheckBoxes.addWidget(self.label_channels)
        self.cb_ch1 = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.cb_ch1.setObjectName("cb_ch1")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch1)
        self.cb_ch3 = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.cb_ch3.setObjectName("cb_ch3")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch3)
        self.cb_ch4 = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.cb_ch4.setObjectName("cb_ch4")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch4)
        self.cb_ch2 = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.cb_ch2.setObjectName("cb_ch2")
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch2)
        self.verticalLayoutThreshould.addLayout(self.verticalLayoutCheckBoxes)
        self.verticalLayoutOptions.addLayout(self.verticalLayoutThreshould)
        self.verticalLayout.addLayout(self.verticalLayoutOptions)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionSimples = QtWidgets.QAction(MainWindow)
        self.actionSimples.setObjectName("actionSimples")
        self.actionIn_Plotter = QtWidgets.QAction(MainWindow)
        self.actionIn_Plotter.setObjectName("actionIn_Plotter")
        self.actionThread = QtWidgets.QAction(MainWindow)
        self.actionThread.setObjectName("actionThread")
        self.actionDesativado = QtWidgets.QAction(MainWindow)
        self.actionDesativado.setObjectName("actionDesativado")
        self.actionStartAcquisition = QtWidgets.QAction(MainWindow)
        self.actionStartAcquisition.setCheckable(False)
        self.actionStartAcquisition.setObjectName("actionStartAcquisition")
        self.actionStart_Recording = QtWidgets.QAction(MainWindow)
        self.actionStart_Recording.setObjectName("actionStart_Recording")
        self.actionStop_Recording = QtWidgets.QAction(MainWindow)
        self.actionStop_Recording.setObjectName("actionStop_Recording")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Main"))
        self.label_replace.setText(_translate("MainWindow", "Here will be the chart"))
        self.lbl_status.setText(_translate("MainWindow", "Status:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_EMG), _translate("MainWindow", "EMG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_features), _translate("MainWindow", "Features"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_classification), _translate("MainWindow", "Classification"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("MainWindow", "Settings"))
        self.menuArquivo.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFunctions.setTitle(_translate("MainWindow", "Functions"))
        self.lbl_options.setText(_translate("MainWindow", "Options:"))
        self.lbl_status_opt.setText(_translate("MainWindow", "Status:"))
        self.label_acquiring_status.setText(_translate("MainWindow", "Acquiring: Off"))
        self.label_plotting_status.setText(_translate("MainWindow", "Plotting: Off"))
        self.label_processing_status.setText(_translate("MainWindow", "Processing: Off"))
        self.label_classification_status.setText(_translate("MainWindow", "Classification: Off"))
        self.label_channels.setText(_translate("MainWindow", "Channels:"))
        self.cb_ch1.setText(_translate("MainWindow", "CH1"))
        self.cb_ch3.setText(_translate("MainWindow", "CH2"))
        self.cb_ch4.setText(_translate("MainWindow", "CH3"))
        self.cb_ch2.setText(_translate("MainWindow", "CH4"))
        self.actionSimples.setText(_translate("MainWindow", "Processamento"))
        self.actionIn_Plotter.setText(_translate("MainWindow", "In Plotter"))
        self.actionThread.setText(_translate("MainWindow", "Thread"))
        self.actionDesativado.setText(_translate("MainWindow", "Desativado"))
        self.actionStartAcquisition.setText(_translate("MainWindow", "Start Acquisition"))
        self.actionStart_Recording.setText(_translate("MainWindow", "Start Recording"))
        self.actionStop_Recording.setText(_translate("MainWindow", "Stop Recording"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

