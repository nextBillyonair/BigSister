import cv2 
import numpy as np
from Camera import WebCamera
import scipy.ndimage.filters as sci
import OpticalFlow
import ImageProcessing
import MotionDetect
import Rectangle
import ImageIO
import SaveLoad
import Templating


def main():
	cam = WebCamera(1)
	opti = OpticalFlow.Dense_Optical_Flow()
	md = MotionDetect.MotionDetect()
	rect_new = []
	rect_old = []
	ppl = 0
	prev = cam.fetch()
	xd = list()

	for i in xrange(50):
		print i
		curr = cam.fetch()

		rect_new = md.detect_motion(prev, curr)
		img = Rectangle.draw_rectangles(curr, rect_new)

		if len(rect_new) > 0 or i == 0:
			flow = opti.dense_opti_flow(prev, curr)
			x, y = opti.get_fx_fy(flow)
			matches = Templating.match_rects(rect_new, rect_old)
			print matches
			mx = np.mean(x)
			xd.append(mx)
			ret = opti.draw_flow(curr, flow)

		else:
			if len(xd) != 0:
				x = np.mean(xd)
				print x
				xd = list()
				# yd = list()
				if x < -0.2:
					print "LEFT"
					ppl -= 1
				elif x > 0.2:
					print "RIGHT"
					ppl += 1
				else: 
					print "NO MOTION"
				x = None

			# DO WORK HERE COUNT!!!!
		rect_old = rect_new
		cv2.imwrite("../Results/Motion.jpg", img)
		cv2.imwrite("../Results/OpticalFlow.jpg", ret)
		prev = curr

	if len(xd) != 0:
		x = np.sum(xd)
		print x
		xd = list()
		if x < -150:
			print "LEFT"
			ppl -= 1
		elif x > 150:
			print "RIGHT"
			ppl += 1
		else: 
			print "NO MOTION"
		x = None

	print ppl

if __name__ == '__main__':
	main()