import cv2 
import numpy as np
from Camera import WebCamera


cap = WebCamera(-1)

frame = cap.fetch()
prvs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame)
hsv[...,1] = 255

while (1) :
	frame2 = cap.fetch()
	next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

	flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

	mag, ang = cv2.cartToPolar(flow[...,0], flow[...,0])
	hsv[...,0] = ang*180/np.pi/2
	hsv[...,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
	bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

	cv2.imshow('frame2', bgr)
	k =  cv2.waitKey(30) & 0xff
	if k == 27:
		break
	elif k == ord('s'):
		cv2.imwrite('optifb.png', frame2)
		cv2.imwrite('optihsv.png', bgr)
	prvs = next

cap.destroy()
cv2.destroyAllWindows()
