# -*- coding: UTF-8 -*-
import face_recognition as fr
import cv2
import os
img1=fr.load_image_file("lhz.jpg")
data1=fr.face_encodings(img1,num_jitters=10)


img2=fr.load_image_file("tmp.jpg")
data2=fr.face_encodings(img2,num_jitters=10)

print(fr.compare_faces(data1,data2[0]))

