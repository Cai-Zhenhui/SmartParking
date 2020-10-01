# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter,QImage,QPixmap
import threading
import cv2


class myThread(threading.Thread):
    def __init__(self,camera,label):
        threading.Thread.__init__(self)
        #self.label=label
        self.camera=camera
        self.frame=None#帧缓存
        self.frameRGB=None#RGB格式帧缓存
        self.isExist=False
        pass

    def __del__(self):
        if self.camera!=None:
            self.camera.release()
        pass

    def run(self):
        print("线程启动")
        while not self.isExist:
            ret, self.frame = self.camera.read()
            if not ret:
                self.frame = None  # 帧缓存
                self.frameRGB = None  # RGB格式帧缓存
                continue
                pass
            self.frameRGB=cv2.cvtColor(self.frame,cv2.COLOR_RGB2BGR)
            #self.frameRGB=self.frame
            #self.label.update()
            pass#end while
        print("线程结束")
        pass

    pass


class ImgView(QLabel):
    def __init__(self,camera,parent=None):
        super(ImgView,self).__init__(parent)
        print("初始化ImgView组件")
        #self.mythread=myThread(camera,self)
        self.camera=camera
        print("初始化ImgView组件完毕")
        pass
    '''
    def paintEvent(self, QPaintEvent):
        painter=QPainter(self)
        painter.begin(self)
        
        painter.end()
        pass'''
    def player(self):
        self.mythread = threading.Thread(target=self.run)
        self.mythread.start()
        pass
    def run(self):
        while self.camera.isOpened():
            ret, self.frame=self.camera.read()
            if not ret :
                continue
                pass
            frameBGR=cv2.cvtColor(self.frame,cv2.COLOR_RGB2BGR)
            img=QImage(frameBGR.data,frameBGR.shape[1],frameBGR.shape[0],QImage.Format_RGB888)
            self.setPixmap(QPixmap.fromImage(img))
            #self.clear()#触发重绘
            pass#end while
        pass
    def __del__(self):
        #通知线程退出
        print("ImgView组件开始析构")
        self.camera.release()
        self.mythread.join()
        print("ImgView组件析构完毕")
        pass
    pass
