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
    imgCode=fr.face_encodings(img,num_jitters=5)[0]
    #生成字符串
    strImgCode="["
    for i in imgCode:
        strImgCode+="%.7f,"%i
        pass
    strImgCode=strImgCode[0:-1]+"]"

    sql="insert into user values('%s','%s','%s','%s','%s')"%("12312341234",name,"123456",lp,strImgCode)
    try:
        ret=cursor.execute(sql)
        print("SQL:",ret)
        db.commit()
        pass
    except:
        db.rollback()
        pass
    db.close()
    pass
if __name__ == "__main__":
    #regist("辽A0AE12","罗涵泽","lhz.jpg")
    regist("苏E05EV8","王吉哲","wjz.jpg")
    pass