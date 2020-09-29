# -*- coding: UTF-8 -*-
import os
import socket
import time
import threading
import dealPL
import dealPL2
import dealFace
IP='0.0.0.0'
PORT=2222
BUFFER_SIZE=1024
FLAG_HEADSIZE_RECV=3
FLAG_HEAD_RECV=1
FLAG_FILE_RECV=2
class Server:
    def __init__(self):
        #self.imgPath="."+os.path.sep+"Server"+os.path.sep+"upload"+os.path.sep
        self.c = dealPL.CardPredictor()
        self.c.train_svm()
        
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((IP,PORT))
        self.socket.listen(1)
        self.isExit=False
        print("Server is running! Waiting for client!")
        pass
    def __del__(self):
        self.clientSocket.close()
        self.socket.close()
        pass
    def run(self):
        self.clientSocket,self.clientAddr=self.socket.accept()
        print("Connect Addr:",self.clientAddr)
        self.linkTime=int(time.time())
        while(not self.isExit):
            print("等待新的文件")
            temp=self.clientSocket.recv(3)
            if not temp:
                time.sleep(0.1)
                continue
            sizeInfo=int(temp.decode())
            #发送头信息大小接受完成标志
            self.clientSocket.send(str(FLAG_HEADSIZE_RECV).encode())
            print("head size:",sizeInfo)

            fileInfo=self.clientSocket.recv(sizeInfo)
            if not fileInfo:
                time.sleep(1)
                continue
            infoList=fileInfo.decode().split("|")
            print(infoList)

            imgType=""#face or LP
            fileName=""
            fileSize=0
            if len(infoList)==3:
                #接收到头信息
                imgType=str(infoList[0])
                fileName=str(infoList[1])
                fileSize=int(infoList[2])
                #发送头信息接受完成标志
                self.clientSocket.send(str(FLAG_HEAD_RECV).encode())
                
                buffer=b''
                totalData=b''
                size=0
                #准备接受数据
                buffer=self.clientSocket.recv(BUFFER_SIZE)
                size+=BUFFER_SIZE
                totalData+=buffer
                while(len(totalData)<fileSize):
                    buffer=self.clientSocket.recv(BUFFER_SIZE)
                    size+=BUFFER_SIZE
                    totalData+=buffer
                    pass#end while(len(totalData)<fileSize):

                with open(fileName,"wb") as target:
                    target.write(totalData)
                    pass
                print("接收完毕")

                #发送接收完毕标志
                self.clientSocket.send(str(FLAG_FILE_RECV).encode())
                if imgType=="Face":
                    print("将处理 FACE")
                    ret=dealFace.find("","","",fileName)
                    #ret=dealFace.deal(fileName)
                    print(ret)
                    self.clientSocket.send(str(ret).encode("utf-8"))
                    pass#end if imgType=="Face":
                elif imgType=="LP":
                    print("将处理 LP")
                    try:
                        r, roi, color = self.c.predict(fileName)
                        pass
                    except BaseException:
                        pass

                    print("结果：",r)
                    lp=""
                    for i in range(len(r)):
                        if i>7:
                            break
                        lp=lp+r[i]
                        pass
                    if len(r)>6:
                        self.clientSocket.send(lp.encode("utf-8"))
                        pass
                    else:
                        self.clientSocket.send("NULL".encode("utf-8"))
                        pass
                    pass#end elif imgType=="LP":
                pass#end if len(infoList)==3:
            pass
        pass
    pass

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server=Server()
        pass
    def __del__(self):
        pass
    #执行myThread.start()时会调用该函数
    def run(self):
        print("socketThread执行")
        self.server.run()
        print("socketThread退出")
        pass
    pass
if __name__ == "__main__":
    socketThread=myThread()
    socketThread.start()
    a=input("input 'q' exit:")
    socketThread.server.isExit=True
    socketThread.join()
    pass