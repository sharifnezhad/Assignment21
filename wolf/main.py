import cv2
image=cv2.imread('4.jpg',0)
width,height=image.shape
print(width,height)
for i in range(width):
    for j in range(height):
        if image[i,j]<150:
            image[i,j]=0
cv2.imwrite('wolf.jpg',image)
cv2.imshow('mam',image)
cv2.waitKey()
