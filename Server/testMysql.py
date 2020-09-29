# -*- coding: UTF-8 -*-
import pymysql
IP="localhost"
user="root"
password="SmartParking"
dbname="SmartParking"

db=pymysql.connect(IP,user,password,dbname,charset='utf8')
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
print(data)
#创建表
sql=''' Create Table user(
    tel CHAR(11) PRIMARY KEY NOT NULL,
    name VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    licenseplate VARCHAR(9) NOT NULL,
    facedata VARCHAR(2000)
)DEFAULT CHARSET=utf8;
'''
ret=cursor.execute(sql)
print(ret)
#创建记录表
sql=''' Create Table info(
    licenseplate VARCHAR(9) NOT NULL,
    starttime DATETIME NOT NULL,
    endtime DATETIME
    )DEFAULT CHARSET=utf8;
'''
ret=cursor.execute(sql)
print(ret)
db.close()