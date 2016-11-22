import cv2 
import numpy as np
from Camera import WebCamera
import OpticalFlow
import ImageProcessing
import MotionDetect
import Rectangle


def Farneback():
	cam = WebCamera(0)

	opti = OpticalFlow.Dense_Optical_Flow()
	md = MotionDetect.MotionDetect()

	prev = cam.fetch()
	xd = np.zeros(200)
	yd = np.zeros(200)
	for i in xrange(200):

		curr = cam.fetch()

		diff, th, rect = md.intermediate_steps(prev, curr)
		img = Rectangle.draw_rectangles(curr, rect)
		cv2.imshow("Diff", diff)
		cv2.imshow("Th", th)
		cv2.imshow("Motion", img)
		# cv2.waitKey(20)
		if len(rect) > 0:
			flow = opti.dense_opti_flow(prev, curr)

			x, y = opti.get_fx_fy(flow)
			mx = np.mean(x)
			my = np.mean(y)
			print i, mx, my
			xd.itemset(i, mx)
			yd.itemset(i, my)

			cv2.imshow("Ret", opti.draw_flow(curr, flow))
		else:
			print i, 0, 0
		cv2.waitKey(20)

		prev = curr

	cv2.destroyAllWindows()	

Farneback()