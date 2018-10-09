# Take each frame
# Convert BGR to HSV
# define range of blue color in HSV
# Threshold the HSV image to get only blue colors
# Bitwise-AND mask and original image
#How to find HSV values to track?
'''>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
>>> print hsv_green
[[[ 60 255 255]]]'''

import numpy as np 
import cv2

cap =cv2.VideoCapture(0)

while(1):
	# Take each frame
	 _, frame = cap.read()

	# Convert BGR to HSV
	 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define range of blue color in HSV

	 lower_blue = np.array([110,50,50])
	 upper_blue = np.array([130,255,255])

	# Threshold the HSV image to get only blue colors

	 mask = cv2.inRange(hsv,lower_blue,upper_blue)

	# Bitwise-AND mask and original image
	 res = cv2.bitwise_and(frame,frame, mask= mask)

	 cv2.imshow('frame',frame)
	 cv2.imshow('mask',mask)
	 cv2.imshow('res',res)

	 k = cv2.waitKey(5)& 0xff

	 if k == 27:
		break

cv2.destroyAllWindows()


'''import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while(1):

	_,frame = cap.read()

	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	mask = cv2.inRange(hsv,lower_blue,upper_blue)

	res = cv2.bitwise_and(frame,frame,mask= mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	k = cv2.waitKey(5)& 0xff
	if k == 27:
		break

cv2.destroyAllWindows() '''