import os
import socket
class Client:
    def Client(selt):
        IP_PORT=("47.93.148.239",2222)
        sk=socket.socket()
        sk.connect(IP_PORT)
        #self.currentDir=os.path.dirname(os.path.abspath(__file__))
        pass

    def sendFile(selt,filePath):
        #path=os.path.join(self.currentDir,path)
        fileName=os.path.basename(filePath)
        fileSize=os.stat(filePath).st_size
        fileInfo="post|%s|%s"%(fileName,fileSize)
        print(fileInfo)
        pass
    pass

c=Client()
c.sendFile(".\\uploadFile.py")