import cv2

img = cv2.imread('faces/1614543532_9-p-lyudi-na-belom-fone-10.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('eyes.xml')
results = faces.detectMultiScale(gray,scaleFactor=8, minNeighbors=1)

for (x,y,w,h) in results:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
cv2.imshow('res',img)
cv2.waitKey(0)