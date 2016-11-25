import cv2 
import numpy as np
from Camera import WebCamera
import OpticalFlow
import ImageProcessing
import MotionDetect
import Rectangle
import Gradients
import ImageIO
import SaveLoad


def Farneback():
	cam = WebCamera(1)

	opti = OpticalFlow.Dense_Optical_Flow()
	md = MotionDetect.MotionDetect()

	prev = cam.fetch()
	xd = np.zeros(200)
	yd = np.zeros(200)
	for i in xrange(200):

		curr = cam.fetch()

		diff, th, rect = md.intermediate_steps(prev, curr)
		img = Rectangle.draw_rectangles(curr, rect)
		# curr
		# cv2.imshow("Diff", diff)
		# cv2.imshow("Th", th)
		# cv2.imshow("Motion", img)
		# cv2.waitKey(20)
		if len(rect) > 0 or i == 0:
			flow = opti.dense_opti_flow(prev, curr)

			x, y = opti.get_fx_fy(flow)
			mx = np.mean(x)
			my = np.mean(y)
			print i, mx, my
			xd.itemset(i, mx)
			yd.itemset(i, my)

			ret = opti.draw_flow(curr, flow)
		else:
			# continue
			print i, 0, 0
		# cv2.waitKey(20)

		grad = Gradients.gradient_magnitude(curr)
		lap = Gradients.laplacian(curr)
		cv2.imwrite("Results/Original.jpg", curr)
		cv2.imwrite("Results/Difference.jpg", diff)
		cv2.imwrite("Results/Threshold.jpg", th)
		cv2.imwrite("Results/Motion.jpg", img)
		cv2.imwrite("Results/OpticalFlow.jpg", ret)
		cv2.imwrite("Results/GradientMag.jpg", ImageIO.normalize(grad))
		cv2.imwrite("Results/Laplacian.jpg", ImageIO.normalize(lap))


		# save([curr, diff, th, rect, ret])

		prev = curr

	cv2.destroyAllWindows()	



Farneback()


