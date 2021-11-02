import cv2
image_girl=cv2.imread('1.jpg',0)

width,height=image_girl.shape
cunt=0
while width:
    cunt2=0
    while height:
        if image_girl[cunt,cunt2]<200:
            image_girl[cunt,cunt2]=255
        else:
            image_girl[cunt,cunt2]=100
        if cunt2==height-1:
            break
        else:
            cunt2+=1
    if cunt==width-1:
        break
    else:
        cunt+=1

cv2.imwrite('color_shift_gril.jpg',image_girl)
cv2.imshow('color shift',image_girl)


image_man=cv2.imread('2.jpg',0)
width,height=image_man.shape
cunt=0
while width:
    cunt2=0
    while height:
        if image_man[cunt,cunt2]<100:
            image_man[cunt,cunt2]=255
        else:
            image_man[cunt,cunt2]=100
        if cunt2==height-1:
            break
        else:
            cunt2+=1
    if cunt==width-1:
        break
    else:
        cunt+=1

cv2.imwrite('color_shift_man.jpg',image_man)
cv2.imshow('color shift2',image_man)
cv2.waitKey()