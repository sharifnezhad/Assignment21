import cv2
import numpy as np
width=height=800
chess_board=np.zeros((width,height),dtype=np.uint8)
color=255
for i in range(0,800,100):
    count=0
    for j in range(0,height,100):
        if  color==255:
            if count%2==0:
                chess_board[i:i+100,j:j+100]=255
        else:
            if count%2!=0:
                chess_board[i:i + 100, j:j + 100] = 255


        count+=1

    if color==255:
        color=0
    else:
        color=255
print(chess_board)
cv2.imwrite('chess-Bord.jpg',chess_board)