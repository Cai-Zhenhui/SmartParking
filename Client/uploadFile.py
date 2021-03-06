# -*- coding: UTF-8 -*-
import os
import socket
import time
IP="47.93.148.239"
PORT=2222
BUFFER_SIZE=1024
FLAG_HEADSIZE_RECV=3
FLAG_HEAD_RECV=1
FLAG_FILE_RECV=2
class Client:
    def __init__(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((IP,PORT))
        self.currentDir=os.path.dirname(os.path.abspath(__file__))
        #self.socket.setblocking(0)
        pass
    def __del__(self):
        self.socket.close()
    pass
    def sendFile(self,filePath,isFace):
        path=os.path.join(self.currentDir,filePath)
        fileName=os.path.basename(path)
        fileSize=os.stat(path).st_size
        #构造文件信息
        #post|name|字节大小
        if isFace:
            fileInfo="Face|%s|%s"%(fileName,fileSize)
            pass
        else:
            fileInfo="LP|%s|%s"%(fileName,fileSize)
            pass
        print(fileInfo)

        #发送文件头长度 该部分不超过3字节
        self.socket.send(("%03d"%(len(fileInfo))).encode('utf-8'))
        #接受 服务端反馈
        tempBuffer=self.socket.recv(1)
        tempTime=int(time.time())
        while not tempBuffer:
            if int(time.time())-tempTime>10:
                print("timeout!")
                #发送文件头长度 该部分不超过3字节
                self.socket.send(("%03d"%(len(fileInfo))).encode('utf-8'))
                if input()=="q":
                    return "NULL"
                continue
            tempBuffer=self.socket.recv(1)
        tempBuffer=tempBuffer.decode()
        if int(tempBuffer)!=FLAG_HEADSIZE_RECV:
            print("ERROR FLAG_HEADSIZE_RECV")
            pass

        #发送文件信息
        self.socket.send(fileInfo.encode('utf-8'))
        #接受 服务端反馈
        tempBuffer=self.socket.recv(1)
        tempTime=int(time.time())
        while not tempBuffer:
            if int(time.time())-tempTime>30:
                print("timeout!")
                return
            tempBuffer=self.socket.recv(1)
        tempBuffer=tempBuffer.decode()
        if int(tempBuffer)!=FLAG_HEAD_RECV:
            print("ERROR FLAG_HEAD_RECV")
            pass

        #收到反馈 发送文件实体
        with open(path,"rb") as target:
            data=target.read()
            self.socket.sendall(data)
            while(not data):
                data=target.read(BUFFER_SIZE)
                self.socket.send(data)
                pass
            pass
        #接受标志
        tempBuffer=self.socket.recv(1)
        tempTime=int(time.time())
        while not tempBuffer:
            if int(time.time())-tempTime>30:
                print("timeout!")
                return
            tempBuffer=self.socket.recv(1)
        tempBuffer=tempBuffer.decode()
        if int(tempBuffer)!=FLAG_FILE_RECV:
            print("ERROR FLAG_FILE_RECV")
            pass
        #接受返回信息
        tempBuffer=self.socket.recv(BUFFER_SIZE)
        tempTime=int(time.time())
        while not tempBuffer:
            if int(time.time())-tempTime>30:
                print("timeout!")
                return
            tempBuffer=self.socket.recv(BUFFER_SIZE)
        tempBuffer=tempBuffer.decode()
        #print("结果：",tempBuffer)
        return tempBuffer
        pass
    def sendString(self,str):
        data=input(">:")
        self.socket.send(data.encode())
        data=self.socket.recv(BUFFER_SIZE)
        print(data)
        pass
    pass
if __name__ == "__main__":
    c=Client()
    c.sendFile(input("input fileName:"),False)
    pass
