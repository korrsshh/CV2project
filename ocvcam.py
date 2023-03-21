import cv2

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    faces = cv2.CascadeClassifier('faces.xml')
    results = faces.detectMultiScale(gray,scaleFactor=8, minNeighbors=3)

    for (x,y,w,h) in results:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
    cv2.imshow('zalupa',img)
