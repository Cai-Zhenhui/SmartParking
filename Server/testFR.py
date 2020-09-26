import face_recognition as fr
import cv2
img=fr.load_image_file("test.bmp")
print(fr.face_locations(img))
print(fr.face_encodings(img))
