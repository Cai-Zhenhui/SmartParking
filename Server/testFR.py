# -*- coding: UTF-8 -*-
import face_recognition as fr
import cv2
import os
print(os.path.abspath(os.path.curdir))

img1=fr.load_image_file(input("input name:"))
print(fr.face_locations(img1))
data1=fr.face_encodings(img1)
print(data1[0:5])

img2=fr.load_image_file(input("input name:"))
print(fr.face_locations(img2))
data2=fr.face_encodings(img2)
print(data2[0:5])

print(fr.compare_faces(data1,data2))

