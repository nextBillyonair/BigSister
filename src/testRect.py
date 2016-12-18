import Rectangle
import cv2
import numpy as np
from Rectangle import Box


img = np.zeros((700,700, 3), dtype = np.uint8)
print img.dtype
# inter = Rectangle.intersection(a, b)
# unio  = Rectangle.union(a, b)
# lst = [ (400, 316, 89, 77), (526, 411, 83, 68)]#,  (488, 393, 46, 47)]
# lst = [(76, 191, 289, 143), (244, 345, 157, 123), (41, 261, 65, 185), (115, 321, 113, 140), (403, 311, 100, 75), (536, 410, 78, 69), (505, 414, 39, 25), (488, 381, 44, 31)]
lst = [(332, 325, 139, 154),(293, 188, 151, 134),(223, 216, 62, 199),(304, 323, 52, 107),(221, 415, 82, 64)]
for i in xrange(len(lst)):
	lst[i] = Box(lst[i])
	print i
print lst
n = Rectangle.draw_rectangles(img, lst)
rectangles = [(304, 323, 167, 156),(293, 188, 151, 134),(221, 216, 82, 263)]
for i in xrange(len(rectangles)):
	rectangles[i] = Box(rectangles[i])

"""
for i in xrange(len(rectangles)):
	# if i >= len(rectangles): break
	for j in xrange(i+1, len(rectangles)):
		print j, rectangles
		# if j >= len(rectangles): break
		a = rectangles[i]
		b = rectangles[j]
		inter = Rectangle.intersection(a, b)
		print inter
		if inter is None:
			continue
		else:
			rectangles[i] = Rectangle.union(a, b)
			rectangles[j] = None
"""

o = Rectangle.draw_rectangles(img, rectangles)

"""
n = Rectangle.draw_rectangles(img, [a])
n = Rectangle.draw_rectangles(n, [b], (255, 0, 0))
o = Rectangle.draw_rectangles(img, [inter], (0, 0, 255))
o = Rectangle.draw_rectangles(o, [unio], (100, 100, 255))
print n
"""
cv2.namedWindow("n", cv2.WINDOW_NORMAL)
cv2.namedWindow("o", cv2.WINDOW_NORMAL)
cv2.namedWindow("add", cv2.WINDOW_NORMAL)
cv2.imshow("n", n)
cv2.imshow("o", o)
cv2.imshow("add", o + n)
# cv2.imshow("o", o)
# cv2.imshow("add", n + o)
cv2.waitKey(0)
cv2.destroyAllWindows()