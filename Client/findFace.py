import cv2
import os
camera=cv2.VideoCapture(0)
cascader=cv2.CascadeClassifier("Client"+os.path.sep+"haarcascade_frontalface_default.xml")
while True:
    ret,frame=camera.read()
    if not ret:
        break
    if cv2.waitKey(10)==ord('q'):
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rect=cascader.detectMultiScale(gray,1.3,5)
    for x,y,w,h in rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
        pass
    cv2.imshow("camera",frame)
    pass