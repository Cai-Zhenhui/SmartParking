# -*- coding: UTF-8 -*-
import cv2
import os
import time
import uploadFile
c=uploadFile.Client()
camera=cv2.VideoCapture(1)
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
        '''
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rect=cascader.detectMultiScale(gray,1.3,5)
        for x,y,w,h in rect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
            pass'''
        cv2.imwrite("tmp.jpg",frame)

        ret=c.sendFile("tmp.jpg",True)
        print(ret)
        input()
        pass#end elif choose==ord('g'):
    cv2.imwrite("tmp.jpg",frame)
    w,h=frame.shape[:2]
    rects=c.sendFile("tmp.jpg",False)
    if rects!="NULL":
        #cv2.addText(frame,rects,(w/2,h/2),cv.FONT_HERSHEY_COMPLEX,2.0, (100, 200, 200), 5)
        pass
    print(rects)
    cv2.imshow("camera",frame)
    pass