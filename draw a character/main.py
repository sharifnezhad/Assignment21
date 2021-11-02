import numpy as np
import cv2
width=height=200
a=np.zeros((width,height),dtype=np.uint8)
a[::]=255
count=0
for i in range(width,0,-10):
    for j in range(count,5+count):
        a[i:i+10,j:j+10]=0
    count+=5
    if i==100:
        break
count+=5
for i in range(100,width,10):
    for j in range(count,5+count):
        a[i:i+10,j:j+10]=0
    count+=5
a[150:160,30:90]=0
cv2.imshow('amir',a)
cv2.waitKey()