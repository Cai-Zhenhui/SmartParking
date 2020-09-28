# -*- coding: UTF-8 -*-
import face_recognition as fr
def deal(fileName):
    img=fr.load_image_file(fileName)
    ret=fr.face_locations(img)
    return ret
    pass
if __name__ == "__main__":

    pass