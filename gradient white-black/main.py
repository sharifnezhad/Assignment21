import cv2
import numpy as np
width=height=500
gradient=np.zeros((width,height),dtype=np.uint8)
gradient[::]=255
color_code=255
for i in range(width):
    color_code-=0.5
    for j in range(height):
        gradient[i,j]=color_code
cv2.imwrite('gradient.jpg',gradient)
cv2.imshow('gradient',gradient)
cv2.waitKey()