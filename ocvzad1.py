import cv2
import numpy as np

img = cv2.imread('images/im2.png')
img = cv2.GaussianBlur(img, (3,3),0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img,100,100)


karnel = np.ones((5,5),np.uint8)
img = cv2.dilate(img, karnel,iterations = 1)

img = cv2.erode(img,karnel, iterations = 1)

new_img = cv2.resize(img, (img.shape[1]//1,img.shape[0]//1))
cv2.imshow('ZALUPA', new_img)
cv2.waitKey(0)


