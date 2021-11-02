import cv2
import numpy as np
image=cv2.imread('Ali_Ansarian.jpg',0)
count=0
for i in range(300,-10,-10):
    for j in range(count,10+count):
        image[i:i+10,j:j+20]=0
    count+=10
cv2.imwrite('AliAnsarian.jpg',image)
cv2.imshow('ali ansariuan',image)
cv2.waitKey()