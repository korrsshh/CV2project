import cv2
import numpy as np
import random
size = (900,900)
photo = np.zeros((size[0],size[1],3), dtype = 'uint8')
#BGR
photo[:]=119,201,105
c = 0
while True:
    c+=1
    b,g,r = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    x1,y1 = random.randint(0,size[1]-51),random.randint(0,size[0]-51)
    x2,y2 = x1+50, y1+50
    photo[y1:y2,x1:x2]=b,g,r
    cv2.rectangle(photo,(x1,y1),(x2,y2),(0,0,0),thickness=3)
    cv2.rectangle(photo, (0, size[0]-10), (146+len(str(c))*21, size[0]-45), (0,0,0), thickness=cv2.FILLED)
    cv2.putText(photo,f'Count: {c}',(0,size[0]-20),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),thickness = 2)
    cv2.imshow("ZALUPA", photo)
    cv2.waitKey(30)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break