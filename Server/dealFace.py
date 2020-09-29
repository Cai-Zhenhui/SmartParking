# -*- coding: UTF-8 -*-
import face_recognition as fr
import pymysql
IP="localhost"
user="root"
password="SmartParking"
dbname="SmartParking"

def deal(fileName):
    img=fr.load_image_file(fileName)
    ret=fr.face_locations(img)
    return ret
    pass
def regist(lp,name,fileName):
    db=pymysql.connect(IP,user,password,dbname,charset='utf8')
    cursor=db.cursor()
    img=fr.load_image_file(fileName)
    imgCode=fr.face_encodings(img,num_jitters=5)
    sql="insert into user values(%s,%s,%s,%s,%s)"%("12312341234",name,"123456",lp,str(imgCode[0]))
    ret=cursor.execute(sql)
    print("SQL:",ret)
    db.close()
    pass
if __name__ == "__main__":
    lp=input()
    name=input()
    fileName=input()
    regist(lp,name,fileName))
    pass