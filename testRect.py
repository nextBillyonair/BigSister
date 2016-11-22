import Rectangle
import cv2
import numpy as np


img = np.zeros((1000,1000,3))

# inter = Rectangle.intersection(a, b)
# unio  = Rectangle.union(a, b)
# lst = [ (400, 316, 89, 77), (526, 411, 83, 68)]#,  (488, 393, 46, 47)]
# lst = [(76, 191, 289, 143), (244, 345, 157, 123), (41, 261, 65, 185), (115, 321, 113, 140), (403, 311, 100, 75), (536, 410, 78, 69), (505, 414, 39, 25), (488, 381, 44, 31)]
lst = [(399, 317, 214, 164), (230, 192, 165, 139), (310, 340, 102, 45), (328, 370, 64, 68), (50, 266, 20, 100)]
print lst
n = Rectangle.draw_rectangles(img, lst)
rectangles = lst
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

o = Rectangle.draw_rectangles(img, rectangles, color=(255,0,0))

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