import cv2 
import numpy as np
from Camera import WebCamera
import scipy.ndimage.filters as sci
import OpticalFlow
import ImageProcessing
import MotionDetect
import Rectangle
import Gradients
import ImageIO
import SaveLoad


def main():
	cam = WebCamera(1)
	opti = OpticalFlow.Dense_Optical_Flow()
	md = MotionDetect.MotionDetect()

	ppl = 0
	prev = cam.fetch()
	xd = list()
	yd = list()
	# seg = list() # JUST FOR NOW

	for i in xrange(200):

		curr = cam.fetch()

		rect = md.detect_motion(prev, curr)
		img = Rectangle.draw_rectangles(curr, rect)

		if len(rect) > 0 or i == 0:
			flow = opti.dense_opti_flow(prev, curr)
			x, y = opti.get_fx_fy(flow)
			mx = np.sum(x)
			my = np.sum(y)
			xd.append(mx)
			yd.append(my)
			ret = opti.draw_flow(curr, flow)

		else:
			if len(xd) != 0:
				# seg.append({"x":xd, "y": yd})
				# xd = list()
				# yd = list()

				# IDEA: Check flow for each rect sep, see
				# print np.sum(xd)
				# print xd
				# datax = sci.gaussian_filter1d(xd, 1)

				# datay = sci.gaussian_filter1d(yd, 0.5)
				x = np.sum(xd)
				print x
				xd = list()
				yd = list()
				if x < -150:
					print "LEFT"
					ppl -= 1
				elif x > 150:
					print "RIGHT"
					ppl += 1
				else: 
					print "NO MOTION"
				x = None

			# DO WORK HERE COUNT!!!!

		cv2.imwrite("../Results/Motion.jpg", img)
		cv2.imwrite("../Results/OpticalFlow.jpg", ret)
		prev = curr

	if len(xd) != 0:
		# seg.append({"x":xd, "y": yd})
		# xd = list()
		# yd = list()
		x = np.sum(xd)
		print x
		xd = list()
		yd = list()
		if x < -150:
			print "LEFT"
			ppl -= 1
		elif x > 150:
			print "RIGHT"
			ppl += 1
		else: 
			print "NO MOTION"
		x = None

	

	# for item in seg:
		# for i in xrange(len(item["x"])):
			# print i, item["x"][i], item["y"][i]
		# print "\n"


	print ppl

# Update with if main thing
main()