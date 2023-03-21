import cv2
img = cv2.imread('images/im2.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img,cv2.COLOR_LAB2RGB)

r,g,b=cv2.split(img)
img = cv2.merge([b,g,r])
cv2.imshow(' ',img)
cv2.waitKey(0)