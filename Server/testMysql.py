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
db.close