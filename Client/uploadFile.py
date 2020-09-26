import os
import socket
IP="47.93.148.239"
PORT=2222
BUFFER_SIZE=1024
FLAG_HEAD_RECV=1
FLAG_FILE_RECV=2
class Client:
    def __init__(self):
        self.socket=socket.socket()
        self.socket.connect((IP,PORT))
        self.currentDir=os.path.dirname(os.path.abspath(__file__))
        pass
    def __del__(self):
        self.socket.close()
    pass
    def sendFile(self,filePath):
        path=os.path.join(self.currentDir,filePath)
        fileName=os.path.basename(path)
        fileSize=os.stat(path).st_size
        fileInfo="post|%s|%s"%(fileName,fileSize)
        print(fileInfo)

        #发送文件信息
        self.socket.send(fileInfo)
        tempBuffer=self.socket.recv(BUFFER_SIZE)
        print(tempBuffer)
        if int(tempBuffer)!=FLAG_HEAD_RECV:
            print("ERROR")
            pass
        #发送文件实体
        with open(path,"rb") as target:
            data=target.read(BUFFER_SIZE)
            self.socket.send(data)
            while(not data):
                data=target.read(BUFFER_SIZE)
                self.socket.send(data)
                pass
            pass
        pass
    def sendString(self,str):
        data=input(">:")
        self.socket.send(data.encode())
        data=self.socket.recv(BUFFER_SIZE)
        print(data)
        pass
    pass

c=Client()
c.sendFile("."+os.path.sep+"uploadFile.py")
#c.sendString("Hello,World!")
