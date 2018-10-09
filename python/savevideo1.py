import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.open(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('a.avi',fourcc, 20.0,(640,480))

while(True):
    ret,frame = cap.read(-1)
    if ret == True:
		#frame = cv2.flip(frame,0)

		out.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    k = cv2.waitKey(60)& 0xff
    if k == 27:
        break

cvReleaseCapture(cap)
cap.release()
cv2.destroyAllWindows()
sleep(60)





