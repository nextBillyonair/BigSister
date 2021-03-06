import cv2
import numpy as np 
from Rectangle import *

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
		   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

def match_template(template, image, method = 3):
	global methods
	method = eval(methods[method])
	res = cv2.matchTemplate(image, template, method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc
	x, y = top_left
	w, h = template.shape[::-2]
	return Box((x, y, w, h))


def draw_match(image, rect, color=255, thickness=3):
	tmp = image.copy()
	x, y, w, h = rect.get_box()
	top_left = (x, y)
	bottom_right = (x + w, y + h)
	cv2.rectangle(tmp, top_left, bottom_right, color, thickness)
	return tmp


def get_method_codes():
	global methods
	d = {}
	for i in xrange(len(methods)):
		d[i] = methods[i]
	return d


def get_window(img, box):
	x, y, w, h = box.get_box()
	patch = img[y:y+h, x:x+w].copy() #Find Coord
	return patch


def distance(box_1, box_2):
	x1, y1, w1, h1 = box_1.get_box()
	x2, y2, w2, h2 = box_2.get_box()
	v1 = np.array([x1, y1, w1, h1])
	v2 = np.array([x2, y2, w2, h2])
	return np.linalg.norm(v1- v2)


def match_rects(rects_1, rects_2):
	lst = []
	if rects_1 is None or rects_2 is None:
		return lst
	for i in xrange(len(rects_1)):
		index = -1
		min_val = -1
		for j in xrange(len(rects_2)):
			v = Box(rects_1[i].intersection(rects_2[j])).area()
			if index is -1 or v > min_val:
				index = j
				min_val = v
		lst.append((i, index))
	return lst
