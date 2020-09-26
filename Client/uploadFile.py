import os
import socket
class Client:
    def __init__(self):
        #self.IP_PORT=("47.93.148.239",2222)
        #self.socket=socket.socket()
        #self.socket.connect(self.IP_PORT)
        self.currentDir=os.path.dirname(os.path.abspath(__file__))
        pass
    def sendFile(self,filePath):
        path=os.path.join(self.currentDir,filePath)
        fileName=os.path.basename(filePath)
        fileSize=os.stat(filePath).st_size
        fileInfo="post|%s|%s"%(fileName,fileSize)
        print(fileInfo)
        pass
    pass

c=Client()
c.sendFile("."+os.path.sep+"uploadFile.py")