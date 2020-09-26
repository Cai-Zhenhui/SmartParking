#客户端程序 负责采集照片发送到服务器处理
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from uploadFile import *
camera=PiCamera()
camera.resolution=(640,480)
camera.framerate=60
rawCapture=PiRGBArray(camera,size=(640,480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    img=frame.array
    cv2.imshow("Frame",img)
    rawCapture.truncate(0)
    key=cv2.waitKey(10)&0xFF
    if key==ord('q'):
        break
    elif key==ord('s'):
        fileName=str(time.time())+".jpg"
        img.imwrite(fileName,img)
        c=Client()
        c.sendFile(fileName)
        pass
    pass
