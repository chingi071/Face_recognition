# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 971, 781))
        self.stackedWidget.setObjectName("stackedWidget")
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.PhotoButton = QtWidgets.QPushButton(self.MainPage)
        self.PhotoButton.setGeometry(QtCore.QRect(80, 450, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PhotoButton.setFont(font)
        self.PhotoButton.setObjectName("PhotoButton")
        self.LoadButton = QtWidgets.QPushButton(self.MainPage)
        self.LoadButton.setGeometry(QtCore.QRect(350, 450, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LoadButton.setFont(font)
        self.LoadButton.setObjectName("LoadButton")
        self.Step1_label = QtWidgets.QLabel(self.MainPage)
        self.Step1_label.setGeometry(QtCore.QRect(20, 140, 811, 61))
        self.Step1_label.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Step1_label.setFont(font)
        self.Step1_label.setObjectName("Step1_label")
        self.main_label = QtWidgets.QLabel(self.MainPage)
        self.main_label.setGeometry(QtCore.QRect(260, 10, 571, 101))
        self.main_label.setMinimumSize(QtCore.QSize(570, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        self.Step2_label = QtWidgets.QLabel(self.MainPage)
        self.Step2_label.setGeometry(QtCore.QRect(20, 340, 800, 61))
        self.Step2_label.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Step2_label.setFont(font)
        self.Step2_label.setObjectName("Step2_label")
        self.DBSetButton = QtWidgets.QPushButton(self.MainPage)
        self.DBSetButton.setGeometry(QtCore.QRect(80, 220, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DBSetButton.setFont(font)
        self.DBSetButton.setObjectName("DBSetButton")
        self.Step3_label = QtWidgets.QLabel(self.MainPage)
        self.Step3_label.setGeometry(QtCore.QRect(20, 570, 800, 61))
        self.Step3_label.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Step3_label.setFont(font)
        self.Step3_label.setObjectName("Step3_label")
        self.RecogButton = QtWidgets.QPushButton(self.MainPage)
        self.RecogButton.setGeometry(QtCore.QRect(80, 660, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RecogButton.setFont(font)
        self.RecogButton.setObjectName("RecogButton")
        self.Developer_label = QtWidgets.QLabel(self.MainPage)
        self.Developer_label.setGeometry(QtCore.QRect(620, 690, 341, 71))
        self.Developer_label.setMinimumSize(QtCore.QSize(241, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Developer_label.setFont(font)
        self.Developer_label.setObjectName("Developer_label")
        self.stackedWidget.addWidget(self.MainPage)
        self.DBpage = QtWidgets.QWidget()
        self.DBpage.setObjectName("DBpage")
        self.layoutWidget_2 = QtWidgets.QWidget(self.DBpage)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 330, 901, 72))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DBPath = QtWidgets.QLabel(self.layoutWidget_2)
        self.DBPath.setMinimumSize(QtCore.QSize(150, 70))
        self.DBPath.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DBPath.setFont(font)
        self.DBPath.setObjectName("DBPath")
        self.horizontalLayout_2.addWidget(self.DBPath)
        self.DBtext = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.DBtext.setMinimumSize(QtCore.QSize(0, 60))
        self.DBtext.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DBtext.setFont(font)
        self.DBtext.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DBtext.setObjectName("DBtext")
        self.horizontalLayout_2.addWidget(self.DBtext)
        self.BrowseButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.BrowseButton.setMinimumSize(QtCore.QSize(120, 70))
        self.BrowseButton.setMaximumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseButton.setFont(font)
        self.BrowseButton.setObjectName("BrowseButton")
        self.horizontalLayout_2.addWidget(self.BrowseButton)
        self.DBSaveButton = QtWidgets.QPushButton(self.DBpage)
        self.DBSaveButton.setGeometry(QtCore.QRect(470, 630, 150, 70))
        self.DBSaveButton.setMinimumSize(QtCore.QSize(150, 70))
        self.DBSaveButton.setMaximumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DBSaveButton.setFont(font)
        self.DBSaveButton.setObjectName("DBSaveButton")
        self.DBBackButton = QtWidgets.QPushButton(self.DBpage)
        self.DBBackButton.setGeometry(QtCore.QRect(680, 630, 150, 70))
        self.DBBackButton.setMinimumSize(QtCore.QSize(150, 70))
        self.DBBackButton.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DBBackButton.setFont(font)
        self.DBBackButton.setObjectName("DBBackButton")
        self.DBSet_label = QtWidgets.QLabel(self.DBpage)
        self.DBSet_label.setGeometry(QtCore.QRect(50, 150, 571, 101))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.DBSet_label.setFont(font)
        self.DBSet_label.setObjectName("DBSet_label")
        self.Step1_label_1 = QtWidgets.QLabel(self.DBpage)
        self.Step1_label_1.setGeometry(QtCore.QRect(30, 30, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Step1_label_1.setFont(font)
        self.Step1_label_1.setObjectName("Step1_label_1")
        self.stackedWidget.addWidget(self.DBpage)
        self.CameraPage = QtWidgets.QWidget()
        self.CameraPage.setObjectName("CameraPage")
        self.CameraWidget = QtWidgets.QStackedWidget(self.CameraPage)
        self.CameraWidget.setGeometry(QtCore.QRect(20, 100, 931, 451))
        self.CameraWidget.setObjectName("CameraWidget")
        self.CameraViewPage = QtWidgets.QWidget()
        self.CameraViewPage.setObjectName("CameraViewPage")
        self.CameraView = QCameraViewfinder(self.CameraViewPage)
        self.CameraView.setGeometry(QtCore.QRect(140, 30, 671, 391))
        self.CameraView.setMaximumSize(QtCore.QSize(1000, 1000))
        self.CameraView.setObjectName("CameraView")
        self.CameraWidget.addWidget(self.CameraViewPage)
        self.CapturedImagePage = QtWidgets.QWidget()
        self.CapturedImagePage.setObjectName("CapturedImagePage")
        self.CapturedImage = QtWidgets.QLabel(self.CapturedImagePage)
        self.CapturedImage.setGeometry(QtCore.QRect(140, 30, 671, 391))
        self.CapturedImage.setMinimumSize(QtCore.QSize(0, 0))
        self.CapturedImage.setMaximumSize(QtCore.QSize(1000, 1000))
        self.CapturedImage.setText("")
        self.CapturedImage.setObjectName("CapturedImage")
        self.CameraWidget.addWidget(self.CapturedImagePage)
        self.ChooseImagePage = QtWidgets.QWidget()
        self.ChooseImagePage.setObjectName("ChooseImagePage")
        self.ChooseImage = QtWidgets.QLabel(self.ChooseImagePage)
        self.ChooseImage.setGeometry(QtCore.QRect(220, 20, 541, 411))
        self.ChooseImage.setText("")
        self.ChooseImage.setObjectName("ChooseImage")
        self.CameraWidget.addWidget(self.ChooseImagePage)
        self.layoutWidget = QtWidgets.QWidget(self.CameraPage)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 570, 901, 74))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.NameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.NameLabel.setMinimumSize(QtCore.QSize(120, 70))
        self.NameLabel.setMaximumSize(QtCore.QSize(150, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.horizontalLayout_3.addWidget(self.NameLabel)
        self.Nametext = QtWidgets.QTextEdit(self.layoutWidget)
        self.Nametext.setMinimumSize(QtCore.QSize(300, 60))
        self.Nametext.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Nametext.setFont(font)
        self.Nametext.setObjectName("Nametext")
        self.horizontalLayout_3.addWidget(self.Nametext)
        self.NameWarn = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.NameWarn.setFont(font)
        self.NameWarn.setText("")
        self.NameWarn.setObjectName("NameWarn")
        self.horizontalLayout_3.addWidget(self.NameWarn)
        self.layoutWidget1 = QtWidgets.QWidget(self.CameraPage)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 680, 911, 72))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonWidget = QtWidgets.QStackedWidget(self.layoutWidget1)
        self.ButtonWidget.setMinimumSize(QtCore.QSize(300, 70))
        self.ButtonWidget.setObjectName("ButtonWidget")
        self.PhotoPage = QtWidgets.QWidget()
        self.PhotoPage.setObjectName("PhotoPage")
        self.CaptureButton = QtWidgets.QPushButton(self.PhotoPage)
        self.CaptureButton.setGeometry(QtCore.QRect(0, 0, 300, 70))
        self.CaptureButton.setMinimumSize(QtCore.QSize(300, 70))
        self.CaptureButton.setMaximumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CaptureButton.setFont(font)
        self.CaptureButton.setObjectName("CaptureButton")
        self.ButtonWidget.addWidget(self.PhotoPage)
        self.LoadPage = QtWidgets.QWidget()
        self.LoadPage.setObjectName("LoadPage")
        self.ChooseButton = QtWidgets.QPushButton(self.LoadPage)
        self.ChooseButton.setGeometry(QtCore.QRect(0, 0, 300, 70))
        self.ChooseButton.setMinimumSize(QtCore.QSize(300, 70))
        self.ChooseButton.setMaximumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ChooseButton.setFont(font)
        self.ChooseButton.setObjectName("ChooseButton")
        self.ButtonWidget.addWidget(self.LoadPage)
        self.horizontalLayout.addWidget(self.ButtonWidget)
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SaveButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.SaveButton.setMinimumSize(QtCore.QSize(230, 70))
        self.SaveButton.setMaximumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        spacerItem1 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.BackButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.BackButton.setMinimumSize(QtCore.QSize(120, 70))
        self.BackButton.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.horizontalLayout.addWidget(self.BackButton)
        self.Step2_label_2 = QtWidgets.QLabel(self.CameraPage)
        self.Step2_label_2.setGeometry(QtCore.QRect(30, 30, 831, 61))
        self.Step2_label_2.setMinimumSize(QtCore.QSize(800, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Step2_label_2.setFont(font)
        self.Step2_label_2.setObjectName("Step2_label_2")
        self.stackedWidget.addWidget(self.CameraPage)
        self.RecogPage = QtWidgets.QWidget()
        self.RecogPage.setObjectName("RecogPage")
        self.Step3_label_2 = QtWidgets.QLabel(self.RecogPage)
        self.Step3_label_2.setGeometry(QtCore.QRect(30, 30, 800, 61))
        self.Step3_label_2.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Step3_label_2.setFont(font)
        self.Step3_label_2.setObjectName("Step3_label_2")
        self.RecogBackButton = QtWidgets.QPushButton(self.RecogPage)
        self.RecogBackButton.setGeometry(QtCore.QRect(780, 630, 150, 70))
        self.RecogBackButton.setMinimumSize(QtCore.QSize(150, 70))
        self.RecogBackButton.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RecogBackButton.setFont(font)
        self.RecogBackButton.setObjectName("RecogBackButton")
        self.RecogName_label = QtWidgets.QLabel(self.RecogPage)
        self.RecogName_label.setGeometry(QtCore.QRect(190, 580, 361, 121))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.RecogName_label.setFont(font)
        self.RecogName_label.setText("")
        self.RecogName_label.setObjectName("RecogName_label")
        self.RecogStartButton = QtWidgets.QPushButton(self.RecogPage)
        self.RecogStartButton.setGeometry(QtCore.QRect(589, 630, 171, 70))
        self.RecogStartButton.setMinimumSize(QtCore.QSize(150, 70))
        self.RecogStartButton.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RecogStartButton.setFont(font)
        self.RecogStartButton.setObjectName("RecogStartButton")
        self.RecogWidget = QtWidgets.QStackedWidget(self.RecogPage)
        self.RecogWidget.setGeometry(QtCore.QRect(10, 100, 931, 451))
        self.RecogWidget.setObjectName("RecogWidget")
        self.RecogViewPage = QtWidgets.QWidget()
        self.RecogViewPage.setObjectName("RecogViewPage")
        self.RecogView = QCameraViewfinder(self.RecogViewPage)
        self.RecogView.setGeometry(QtCore.QRect(140, 30, 671, 391))
        self.RecogView.setMaximumSize(QtCore.QSize(1000, 1000))
        self.RecogView.setObjectName("RecogView")
        self.RecogWidget.addWidget(self.RecogViewPage)
        self.RecogImagePage = QtWidgets.QWidget()
        self.RecogImagePage.setObjectName("RecogImagePage")
        self.RecogImage = QtWidgets.QLabel(self.RecogImagePage)
        self.RecogImage.setGeometry(QtCore.QRect(140, 30, 671, 391))
        self.RecogImage.setMinimumSize(QtCore.QSize(0, 0))
        self.RecogImage.setMaximumSize(QtCore.QSize(1000, 1000))
        self.RecogImage.setText("")
        self.RecogImage.setObjectName("RecogImage")
        self.RecogWidget.addWidget(self.RecogImagePage)
        self.stackedWidget.addWidget(self.RecogPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.CameraWidget.setCurrentIndex(2)
        self.ButtonWidget.setCurrentIndex(0)
        self.RecogWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PhotoButton.setText(_translate("MainWindow", "Take a picture"))
        self.LoadButton.setText(_translate("MainWindow", "Load picture"))
        self.Step1_label.setText(_translate("MainWindow", "Step 1：Set up the database\n"
""))
        self.main_label.setText(_translate("MainWindow", "Hello！Face Recognition"))
        self.Step2_label.setText(_translate("MainWindow", "Step 2：Create personal information"))
        self.DBSetButton.setText(_translate("MainWindow", "Setting"))
        self.Step3_label.setText(_translate("MainWindow", "Step 3：Recognition"))
        self.RecogButton.setText(_translate("MainWindow", "Recognition"))
        self.Developer_label.setText(_translate("MainWindow", "Developer： Ching I Lee"))
        self.DBPath.setText(_translate("MainWindow", "Database path："))
        self.BrowseButton.setText(_translate("MainWindow", "browse"))
        self.DBSaveButton.setText(_translate("MainWindow", "Save"))
        self.DBBackButton.setText(_translate("MainWindow", "Back"))
        self.DBSet_label.setText(_translate("MainWindow", "Please select the database path to save."))
        self.Step1_label_1.setText(_translate("MainWindow", "Step 1：Database settings"))
        self.NameLabel.setText(_translate("MainWindow", "Your name："))
        self.CaptureButton.setText(_translate("MainWindow", "Take a picture"))
        self.ChooseButton.setText(_translate("MainWindow", "Choose picture"))
        self.SaveButton.setText(_translate("MainWindow", "Save picture"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        self.Step2_label_2.setText(_translate("MainWindow", "Step 2：Create personal information"))
        self.Step3_label_2.setText(_translate("MainWindow", "Step 3：Recognition"))
        self.RecogBackButton.setText(_translate("MainWindow", "Back"))
        self.RecogStartButton.setText(_translate("MainWindow", "Recognition"))
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
