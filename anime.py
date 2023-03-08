def asia(line:list):
    hg = [" ", ".", "/", "?", ">", "%", "#","#","#"]
    a = ""
    for i in line:
        c = i[0]
        c = int(c/36.42857142857143)
        a+= hg[c]
    
    return a


a = ["안녕하세요.","선문대학교","컴퓨터 공학부", "학생입니다."]
for i in a: print(i, )

print('안녕하세요.')
print('선문대학교')
print("컴퓨터공학부")
print("학생입니다.")

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
    
    

