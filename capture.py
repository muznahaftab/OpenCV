import cv2
import numpy as np

#Creating an object. 0 for selecting camera
vid = cv2.VideoCapture(0)

while True:
	#capturing frame
	ret,frame = vid.read()
	#showing the frame
	cv2.imshow('Video output', frame)
	#exit on pressing the escape key
	if cv2.waitKey(1) & 0xFF == 27:
		break

#shutdown the camera
vid.release()
cv2.destroyAllWindows()  
