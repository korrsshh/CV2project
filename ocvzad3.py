import cv2
import numpy as np

img = cv2.imread('images/im2.png')
new_img = np.zeros(img.shape,dtype = 'uint8')
# img = cv2.flip(img,0)
#
# def rotate(img_param, angle):
#     height, wigth = img_param.shape[:2]
#     point = (wigth//2,height//2)
#     mat = cv2.getRotationMatrix2D(point,angle,1)
#     return cv2.warpAffine(img_param, mat,(wigth,height))
#
# def transform(img_param,x,y):
#     mat = np.float32([[1,0,x],[0,1,y]])
#     return cv2.warpAffine(img_param,mat,(img_param.shape[1],img_param.shape[0]))

# img = rotate(img,11)
# img = transform(img,30,200)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img,(5,5),0)
img = cv2.Canny(img,100,140)
con,hir = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img,con,-1,(255,11,200),1)
cv2.imshow('kal',new_img)
cv2.waitKey(0)