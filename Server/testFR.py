import face_recognition as fr
import cv2
import os
print(os.path.abspath(os.path.curdir))
img=fr.load_image_file(os.path.abspath(os.path.curdir)+os.path.sep+"Client"+os.path.sep+"test.bmp")
print(fr.face_locations(img))
print(fr.face_encodings(img))
