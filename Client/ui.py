# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ImgView import ImgView
import cv2
import time
import uploadFile
import bluetooth
count=0
class Ui_Form(object):
    def setupUi(self, Form):
        self.c=uploadFile.Client()
        self.serCar=bluetooth.BlueTooth(bluetooth.PORT_CAR,9600)
        self.serSW=bluetooth.BlueTooth(bluetooth.PORT_SW,9600)

        Form.setObjectName("Form")
        Form.resize(925, 732)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 350))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 900))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 900))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #按钮存车
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        #添加事件
        self.pushButton.clicked.connect(self.parking)

        #按钮取车
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        # 添加事件
        self.pushButton_2.clicked.connect(self.getCar)

        self.verticalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        #self.imgLP = QtWidgets.QLabel(self.frame)
        self.cameraLP=cv2.VideoCapture(1)
        self.imgLP=ImgView(self.cameraLP,self.frame)
        self.imgLP.player()

        self.imgLP.setObjectName("imgLP")
        self.gridLayout_2.addWidget(self.imgLP, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        #self.imgFace = QtWidgets.QLabel(self.frame)
        self.cameraFace = cv2.VideoCapture(2)
        self.imgFace=ImgView(self.cameraFace,self.frame)
        self.imgFace.player()

        self.imgFace.setObjectName("imgFace")
        self.gridLayout_2.addWidget(self.imgFace, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "云边融合智能停车场系统"))
        self.pushButton.setText(_translate("Form", "停  车"))
        self.pushButton_2.setText(_translate("Form", "取  车"))
        self.label_2.setText(_translate("Form", "人脸"))
        self.imgLP.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "车牌"))
        self.imgFace.setText(_translate("Form", "TextLabel"))
        pass

    def parking(self):
        print("存车")
        cv2.imwrite("tmp.jpg",self.imgLP.frame)
        ret=self.c.sendFile("tmp.jpg",False)
        if ret!="NULL":
            count+=1
            if count==1:
                self.textBrowser.append("您的车【"+ret+"】将停到 9号车位.停车时间"+time.ctime())
                self.serSW.send("1".encode())
                time.sleep(1)
                self.serCar.send()
                pass
            elif count==2:
                self.textBrowser.append("您的车【"+ret+"】将停到18号车位.停车时间"+time.ctime())
                self.serSW.send("3".encode())
                time.sleep(1)
                self.serCar.send()
                pass
            pass
        pass

    def getCar(self):
        print("取车")
        cv2.imwrite("tmp.jpg",self.imgFace.frame)
        ret=self.c.sendFile("tmp.jpg",True)
        if ret!="NULL":
            count+=1
            if count==1:
                self.textBrowser.append("您的车【"+ret+"】正在搬运中，请稍等.停车时间"+time.ctime())
                self.serSW.send("1".encode())
                time.sleep(1)
                self.serCar.send()
                pass
            elif count==2:
                self.textBrowser.append("您的车【"+ret+"】将停到18号车位.停车时间"+time.ctime())
                self.serSW.send("3".encode())
                time.sleep(1)
                self.serCar.send()
                pass
            pass
        pass
    pass
