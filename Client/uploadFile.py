import os
import socket
IP="47.93.148.239"
PORT=2222
BUFFER_SIZE=1024
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
c.sendString("Hello,World!")
