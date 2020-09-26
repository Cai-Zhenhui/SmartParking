import os
import socket
import time
IP='0.0.0.0'
PORT=2222
BUFFER_SIZE=1024
class Server:
    def __init__(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((IP,PORT))
        self.socket.listen(1)
        print("Server is running! Waiting for client!")
        self.clientSocket,self.clientAddr=self.socket.accept()
        print("Connect Addr:",self.clientAddr)
        pass
    def __del__(self):
        self.socket.close()
        pass
    def run(self):
        while(True):
            data=self.clientSocket.recv(BUFFER_SIZE)
            if not data:
                continue
            print(data)
            self.clientSocket.send(('[%s] %s' % (time.ctime(), data)).encode())
            pass
        pass
    pass
if __name__ == "__main__":
    server=Server()
    server.run()
    pass