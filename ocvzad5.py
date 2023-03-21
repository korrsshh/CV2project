import cv2
import numpy as np

photo = cv2.imread('images/im2.png')
img = np.zeros((photo.shape[:2]),dtype = 'uint8')

circle = cv2.circle(img.copy(),(200,300),120,255,-1)
squre = cv2.rectangle(img.copy(),(25,25),(250,350),255,-1)

img = cv2.bitwise_and(photo,photo,mask=circle)

cv2.imshow('res',img)

cv2.waitKey(0)