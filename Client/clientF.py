# -*- coding: UTF-8 -*-
import cv2
import os
import time
import uploadFile
c=uploadFile.Client()
camera=cv2.VideoCapture(0)
cascader=cv2.CascadeClassifier("Client"+os.path.sep+"haarcascade_frontalface_default.xml")
while True:
    ret,frame=camera.read()
    if not ret:
        break
    choose=cv2.waitKey(1)
    if choose==ord('q'):
        break
    elif choose==ord('g'):
        #检测到用户输入 准备人脸识别取车
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rect=cascader.detectMultiScale(gray,1.3,5)
        for x,y,w,h in rect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
            pass
        pass#end elif choose==ord('g'):
    cv2.imwrite("tmp.jpg",frame)
    
    print("结果：",c.sendFile("tmp.jpg",True))
    time.sleep(1)
    cv2.imshow("camera",frame)
    pass