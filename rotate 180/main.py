import cv2
image=cv2.imread('3.jpg')
image2=cv2.rotate(image,cv2.ROTATE_180)


cv2.imwrite('img.jpg',image2)
cv2.imshow('rotate 180',image2)
cv2.waitKey()