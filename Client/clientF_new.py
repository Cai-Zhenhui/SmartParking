# -*- coding: UTF-8 -*-
import cv2
import os
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import uploadFile
import tkinter as tk
c=uploadFile.Client()
camera=cv2.VideoCapture(1)
camera2=cv2.VideoCapture(0)
cascader=cv2.CascadeClassifier("Client"+os.path.sep+"haarcascade_frontalface_default.xml")

def car_stop(T1):
    ret,frame=camera.read()
    cv2.imwrite("tmp.jpg",frame)
    w,h=frame.shape[:2]
    ret=c.sendFile("tmp.jpg",False)
    if ret!="NULL":
        #w,h=frame.shape[:2]
        #draw=ImageDraw.Draw(img)
        #ttf = ImageFont.load_default()
        #draw.text((int(w/2), int(h/2)),ret+" 当前时间"+time.ctime(),(255, 0, 0),font=ttf)
        #cv2.putText(frame, ret+" 当前时间"+time.ctime(), (int(w/2), int(h/2)), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, ))
        res = ret + "当前时间: " + time.ctime()
        T1.delete('1.0', 'end')
        T1.insert(1.0, res)
        #print(ret+" 当前时间"+time.ctime())
        '''
        if ret.find("8")!=-1 or ret.find("5")!=-1 or ret.find("V")!=-1:
            #苏E 05EV8
            cv2.putText(frame, "苏E05EV8 当前时间"+time.ctime(), (int(w/2), h), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, ))
            pass
        elif ret.find("A")!=-1 or ret.find("1")!=-1 or ret.find("2")!=-1:
            cv2.putText(frame, "辽A0AE12 当前时间"+time.ctime(), (int(w/2), h), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, ))
            pass'''
    #cv2.imshow("camera",np.array(img))
    else:
        T1.delete('1.0', 'end')
        T1.insert(1.0, "car")

    cv2.imshow("camera",frame)
    

def car_get(T1):
    ret,frame2=camera2.read()
    #检测到用户输入 准备人脸识别取车
    '''
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rect=cascader.detectMultiScale(gray,1.3,5)
    for x,y,w,h in rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
        pass'''
    cv2.imwrite("tmp.jpg",frame2)
    ret=c.sendFile("tmp.jpg",True)
    if ret!="NULL":
            
    #w,h=frame.shape[:2]
    #draw=ImageDraw.Draw(img)
    #ttf = ImageFont.load_default()
    #draw.text((int(w/2), int(h/2)),"已找到你的汽车："+ret,(255, 0, 0),font=ttf)
    #cv2.putText(frame, "已找到你的汽车："+ret, (int(w/2), int(h/2)), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0))
    #绘制结果
    #print("已找到你的汽车："+ret)
        res = "已找到你的汽车："+ret
        T1.delete('1.0', 'end')
        T1.insert(1.0, res)
    else:
        T1.delete('1.0', 'end')
        T1.insert(1.0, ret)
    cv2.imshow("camera2",frame2)


root = tk.Tk()
root.title("SmartParking")
root.geometry("650x400")
Welcome = tk.Label(root, text = "欢迎使用本系统!")
Welcome.config(height = 3, fg = "red", font = ('楷体', 18, 'bold'))
Welcome.grid(row = 1, column = 0, sticky = "WN", padx = 250)
B1 = tk.Button(root, text = "存车")
B1.config(command = (lambda:car_stop(T1)))
B1.grid(row = 2, column = 0, sticky = "W", padx = 400)
B2 = tk.Button(root, text = "取车")
B2.config(command = (lambda:car_get(T1)))
B2.grid(row = 2, column = 0, sticky = "W", padx = 450)
B3 = tk.Button(root, text = "退出")
B3.config(command = (lambda:exit(0)))
B3.grid(row = 2, column = 0, sticky = "W", padx = 500)
T1 = tk.Text(root, width = 50, height = 8, fg = "blue")
T1.grid(row = 3, column = 0, sticky = "W", padx = 180)
root.mainloop()

    
camera.release()
cv2.destroyAllWindows()