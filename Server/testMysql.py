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
    fd0 int,
    fd1 int,
    fd2 int,
    fd3 int,
    fd4 int,
    fd5 int,
    fd6 int,
    fd7 int,
    fd8 int,
    fd9 int,
    fd10 int,
    fd11 int,
    fd12 int,
    fd13 int,
    fd14 int,
    fd15 int,
    fd16 int,
    fd17 int,
    fd18 int,
    fd19 int,
    fd20 int,
    fd21 int,
    fd22 int,
    fd23 int,
    fd24 int,
    fd25 int,
    fd26 int,
    fd27 int,
    fd28 int,
    fd29 int,
    fd30 int,
    fd31 int,
    fd32 int,
    fd33 int,
    fd34 int,
    fd35 int,
    fd36 int,
    fd37 int,
    fd38 int,
    fd39 int,
    fd40 int,
    fd41 int,
    fd42 int,
    fd43 int,
    fd44 int,
    fd45 int,
    fd46 int,
    fd47 int,
    fd48 int,
    fd49 int,
    fd50 int,
    fd51 int,
    fd52 int,
    fd53 int,
    fd54 int,
    fd55 int,
    fd56 int,
    fd57 int,
    fd58 int,
    fd59 int,
    fd60 int,
    fd61 int,
    fd62 int,
    fd63 int,
    fd64 int,
    fd65 int,
    fd66 int,
    fd67 int,
    fd68 int,
    fd69 int,
    fd70 int,
    fd71 int,
    fd72 int,
    fd73 int,
    fd74 int,
    fd75 int,
    fd76 int,
    fd77 int,
    fd78 int,
    fd79 int,
    fd80 int,
    fd81 int,
    fd82 int,
    fd83 int,
    fd84 int,
    fd85 int,
    fd86 int,
    fd87 int,
    fd88 int,
    fd89 int,
    fd90 int,
    fd91 int,
    fd92 int,
    fd93 int,
    fd94 int,
    fd95 int,
    fd96 int,
    fd97 int,
    fd98 int,
    fd99 int,
    fd100 int,
    fd101 int,
    fd102 int,
    fd103 int,
    fd104 int,
    fd105 int,
    fd106 int,
    fd107 int,
    fd108 int,
    fd109 int,
    fd110 int,
    fd111 int,
    fd112 int,
    fd113 int,
    fd114 int,
    fd115 int,
    fd116 int,
    fd117 int,
    fd118 int,
    fd119 int,
    fd120 int,
    fd121 int,
    fd122 int,
    fd123 int,
    fd124 int,
    fd125 int,
    fd126 int,
    fd127 int)DEFAULT CHARSET=utf8;
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