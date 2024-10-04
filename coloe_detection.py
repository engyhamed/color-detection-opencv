import cv2
from PIL import Image
import numpy as np 
from util_fun import get_limits
color =[0,255,255]
video=cv2.VideoCapture("output3.avi")
fps=int(video.get(cv2.CAP_PROP_FPS))
print(fps)
st=1
while st:
    st,frame=video.read()
    if st==0:
        print("there is no vedio ")
        break
    hsvv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    ll,ul=get_limits(color)
    mask=cv2.inRange(hsvv,ll,ul)
    c,h=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in c:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("live",frame)
    k= cv2.waitKey(1)& 0xff
    if k==ord("q"):
        break
video.release()
cv2.destroyAllWindows() 

