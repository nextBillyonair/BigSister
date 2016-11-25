import cv2
import numpy

"""
Module with methods designed to manipulate Rectangular tuples (x, y, w, h).
"""


def draw_rectangles(frame, rect, color = (0, 255, 0), thickness = 1):
    """
    Draws rectangles onto frame.
    """
    if rect is None: return frame
    tmp = frame.copy()
    for r in rect:
    	if r is None: continue
        (x, y, w, h) = r
        cv2.rectangle(tmp, (x, y), (x + w, y + h), color, thickness) 
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

# END OF FILE
