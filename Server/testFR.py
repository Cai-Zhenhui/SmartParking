import face_recognition as fr
import cv2
img=cv2.imread("test.bmp")
print(fr.face_locations(img))
print(fr.face_encodings(img))
