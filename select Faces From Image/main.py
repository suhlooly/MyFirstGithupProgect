
import os
import cv2
img = cv2.imread('myphoto.jpg') #Path of an image
face_cascade=cv2.CascadeClassifier('haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascades\\haarcascade_eye.xml')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray)
for(x,y,w,h) in face:
    sho=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    roi_gray=gray[y:y+h,x:x+w]
    roi_color=sho[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

shos=cv2.resize(img,(500,600))
cv2.imshow("img",shos)
cv2.waitKey(0)
cv2.destroyAllWindows()

