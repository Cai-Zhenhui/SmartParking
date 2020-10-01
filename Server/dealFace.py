# -*- coding: UTF-8 -*-
import face_recognition as fr
import numpy as np
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
def find(tel,lp,name,fileName):
    img=fr.load_image_file(fileName)
    targetImgCode=fr.face_encodings(img,num_jitters=10)
    if len(targetImgCode)<1:
        return "NULL"#没有人脸
        pass
    #targetImgCode=targetImgCode[0]
    db=pymysql.connect(IP,user,password,dbname,charset='utf8')
    cursor=db.cursor()
    sql="select * from user"
    ret=""
    try:
        ret=cursor.execute(sql)
        print("SQL:",ret)
        ret=cursor.fetchall()
        pass
    except:
        print("查询异常")
        db.close()
        return "NULL"
        pass
    
    #对比
    for row in ret:
        imgCode=np.array(eval(row[4]))
        print(eval(row[4]))
        if fr.compare_faces(targetImgCode,imgCode,0.5)[0]:
            #找到了
            db.close()
            return row[3]
            pass
        pass#end for
    db.close()
    return "NULL"
    pass
def regist(tel,lp,name,fileName):
    db=pymysql.connect(IP,user,password,dbname,charset='utf8')
    cursor=db.cursor()
    img=fr.load_image_file(fileName)
    imgCode=fr.face_encodings(img,num_jitters=10)[0]
    #生成字符串
    strImgCode="["
    for i in imgCode:
        strImgCode+="%f,"%i
        pass
    strImgCode=strImgCode[0:-1]+"]"

    sql="insert into user values('%s','%s','%s','%s','%s')"%(tel,name,"123456",lp,strImgCode)
    print(sql)
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
    #regist("12312341234","辽A0AE12","罗涵泽","lhz.jpg")
    regist("12312341234","辽A0AE12","李政祎","lzy.jpg")
    regist("12312340000","苏E05EV8","王吉哲","wjz.jpg")
    pass