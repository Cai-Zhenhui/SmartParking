# -*- coding: UTF-8 -*-
import cv2
import time
import os
import tkinter as tk
from PIL import Image
import uploadFile
class Window:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("云边融合智能停车场系统")
        self.root.geometry("{}x{}".format(*self.root.maxsize()))
        
        #img=tk.PhotoImage(file="0.png")
        img=Image.open("0.png")
        img=tk.PhotoImage(img)
        print(type(img))
        #canvasLP.create_bitmap()
        #canvasLP.configure(image=img)
        #
        canvasLP=tk.Label(self.root,bg="white", height=600, width=800,image = img)
        canvasLP.grid(column=0,row=0,sticky="W")
        #a=canvasLP.create_image(0,0,anchor=tk.N,image=img)
        #canvasLP.pack()
        #print(type(a))
        canvasFace=tk.Canvas(self.root,bg="white")
        canvasFace.grid(column=0,row=1,sticky="W")
        self.root.update_idletasks()
        pass
    def run(self):
        self.root.mainloop()
        pass
    def __del__(self):
        print("end")
        pass
    pass
if __name__ == "__main__":
    win = Window()
    win.run()
    pass