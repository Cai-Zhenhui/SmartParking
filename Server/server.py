import os
import socket
import time
IP='0.0.0.0'
PORT=2222
BUFFER_SIZE=1024
FLAG_HEAD_RECV=1
FLAG_FILE_RECV=2
class Server:
    def __init__(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((IP,PORT))
        self.socket.listen(1)
        print("Server is running! Waiting for client!")
        self.clientSocket,self.clientAddr=self.socket.accept()
        print("Connect Addr:",self.clientAddr)
        self.linkTime=int(time.time())
        pass
    def __del__(self):
        self.clientSocket.close()
        self.socket.close()
        pass
    def run(self):
        while(True):
            fileInfo=self.clientSocket.recv(BUFFER_SIZE)
            if not fileInfo:
                if int(time.time())-self.linkTime>30:
                    print("timeout!")
                    break
                continue
            
            infoList=fileInfo.decode().split("|")
            print(infoList)
            fileName=""
            fileSize=0
            if len(infoList)==3:
                #接收到头信息
                fileName=str(infoList[1])
                fileSize=int(infoList[2])
                #发送头信息接受完成标志
                self.clientSocket.send(str(FLAG_HEAD_RECV).encode())
                
                data=b''
                totalData=b''
                size=0
                #准备接受数据
                data=self.clientSocket.recv(BUFFER_SIZE)
                size+=BUFFER_SIZE
                totalData+=data
                while(size<fileSize):
                    data=self.clientSocket.recv(BUFFER_SIZE)
                    print(size,end=' ')
                    size+=BUFFER_SIZE
                    totalData+=data
                    print(len(totalData))
                    pass
                #发送接收完毕标志
                self.clientSocket.send(str(FLAG_FILE_RECV).encode())
                with open(fileName,"wb") as target:
                    target.write(totalData)
                    pass
                pass
            self.clientSocket.send(('[%s] %s' % (time.ctime(), data)).encode())
            pass
        pass
    pass
if __name__ == "__main__":
    server=Server()
    server.run()
    pass