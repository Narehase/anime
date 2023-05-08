def asia(line:list):
    hg = [" ", ".", "/", "?", ">", "%", "#","#","#"]
    a = ""
    for i in line:
        c = i[0]
        c = int(c/36.42857142857143)
        a+= hg[c]
    
    return a

import numpy as np
import cv2
import os
v = cv2.VideoCapture("bb.mp4")
_,f = v.read()
while _:
    _,f = v.read()
    f = cv2.resize(f, (50,30))
    for i in f:        
        a = asia(i)
        print(a)
    os.system("cls")
    
    

