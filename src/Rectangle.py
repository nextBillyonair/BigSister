import cv2
import numpy as np

"""
Module with methods designed to manipulate Rectangular tuples (x, y, w, h).
"""


def draw_rectangles(frame, rect, thickness = 1):
	"""
	Draws rectangles onto frame.
	"""
	if rect is None: return frame
	tmp = frame.copy()
	for r in rect:
		if r is None: continue
		tmp = r.draw_rectangle(tmp, thickness)
	return tmp


def union(a, b):
	"""
	Finds the Union of two rectangles.
	"""
	if a is None or b is None: return None
	x = min(a[0], b[0])
	y = min(a[1], b[1])
	w = max(a[0] + a[2], b[0] + b[2]) - x
	h = max(a[1] + a[3], b[1] + b[3]) - y
	return (x, y, w, h)


def intersection(a, b):
	"""
	Finds the intersection of two rectangles.
	None if None.
	"""
	if a is None or b is None: return None
	x = max(a[0], b[0])
	y = max(a[1], b[1])
	w = min(a[0] + a[2], b[0] + b[2]) - x
	h = min(a[1] + a[3], b[1] + b[3]) - y
	if w < 0 or h < 0: return None
	return (x, y, w, h)


def area(a):
	"""
	Returns the area of a rectangle.
	"""
	if a is None: return 0
	(x, y, w, h) = a
	return w * h


def perimeter(a):
	"""
	Returns the perimeter of a rectangle.
	"""
	if a is None: return 0
	(x, y, w, h) = a
	return 2 * (w + h)


def aspect_ratio(a):
	"""
	Returns the ratio of the width to height of rectangle a.
	"""
	if a is None: return 0
	(x, y, w, h) = a
	return float(w) / h


class Box():

	def __init__(self, r, n = 0):
		self.rect = r
		self.color = np.random.randint(0, 255, (100, 3))
		rand = np.random.randint(0, len(self.color))
		self. color = self.color[rand].tolist()
		self.num = n

	def get_box(self):
		return self.rect

	def get_color(self):
		return self.color

	def get_id(self):
		return self.num

	def set_id(self, n):
		self.num = n

	def get_points(self):
		x, y, w, h = self.rect
		p1 = (x, y)
		p2 = (x + w, y)
		p3 = (x, y + h)
		p4 = (x + w, y + h)
		return [p1, p2, p3, p4]

	def get_x(self):
		return self.r[0]

	def get_y(self):
		return self.r[1]

	def get_w(self):
		return self.r[2]

	def get_h(self):
		return self.r[3]


	def union(self, b):
		a = self.rect
		b = b.get_box()
		if a is None or b is None: return None
		x = min(a[0], b[0])
		y = min(a[1], b[1])
		w = max(a[0] + a[2], b[0] + b[2]) - x
		h = max(a[1] + a[3], b[1] + b[3]) - y
		return (x, y, w, h)


	def intersection(self, b):
		a = self.rect
		b = b.get_box()
		if a is None or b is None: return None
		x = max(a[0], b[0])
		y = max(a[1], b[1])
		w = min(a[0] + a[2], b[0] + b[2]) - x
		h = min(a[1] + a[3], b[1] + b[3]) - y
		if w < 0 or h < 0: return None
		return (x, y, w, h)


	def area(self):
		if self.rect is None: return 0
		(x, y, w, h) = self.rect
		return w * h


	def perimeter(self):
		if self.rect is None: return 0
		(x, y, w, h) = self.rect
		return 2 * (w + h)


	def aspect_ratio(self):
		if self.rect is None: return 0
		(x, y, w, h) = self.rect
		return float(w) / h

	def draw_rectangle(self, frame, thickness = 1):
		if self.rect is None: return frame
		tmp = frame.copy()
		(x, y, w, h) = self.rect
		cv2.rectangle(tmp, (x, y), (x + w, y + h), self.color, thickness) 
		return tmp

# END OF FILE