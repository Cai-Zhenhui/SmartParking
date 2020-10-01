import serial
import threading
PORT_SW="COM4"
PORT_CAR="COM3"

class BlueTooth:
    def __init__(self,tPort,tBPS=9600,tTimeout=10):
        self.port=tPort
        self.bps=tBPS
        self.timeout=tTimeout
        try:
            self.ser=serial.Serial(self.port,self.bps,timeout=self.timeout)
            print("串口:%s 已打开!\n"%self.port)
            pass
        except Exception as e:
            print("串口:%s 打开错误!\n"%self.port,e)
            pass
        pass
    def send(self,data):
        if not self.ser.is_open:
            return -1
            pass
        result=self.ser.write(data)
        return result
        pass
    def read(self):
        data=self.ser.read(self.ser.in_waiting)
        return data
        pass
    def __del__(self):
        if self.ser.is_open:
            self.ser.close()
        pass
    pass
if __name__ == "__main__":
    b=BlueTooth(PORT_SW,9600)
    while True:
        a=input()
        if a=="q":
            break
        print(bytes([eval(a)])," re: ",b.send(a.encode()))
        
        pass
    pass