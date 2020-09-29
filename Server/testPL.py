# -*- coding: UTF-8 -*-
import cv2
import os
import time
import dealPL

c=dealPL.CardPredictor()
camera=cv2.VideoCapture(1)

while True:
    ret,frame=camera.read()
    if not ret:
        break
    choose=cv2.waitKey(1)
    if choose==ord('q'):
        break
    cv2.imwrite("tmp.jpg",frame)
    try:
        r, roi, color = c.predict("tmp.jpg")
        print(r)
        pass
    except BaseException:
        pass

    cv2.imshow("camera",frame)
    pass