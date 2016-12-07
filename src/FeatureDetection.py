import cv2
import numpy
import ImageIO


"""
Module to implement feature detectors and descriptors
"""


def harris_corner_detector(img, blockSize = 2, ksize = 3, k = 0.04):
	"""
	Harris Corner Detection.
	"""
	gray = ImageIO.grayscale(img)
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray, blockSize, ksize, k)
	dst = cv2.dilate(dst, None)
	return dst


def harris_subpixel(img, blockSize = 2, ksize = 3, k = 0.04):
	"""
	Harris Corner detection with Sub-pixel Accuracy.
	"""
	dst = harris_corner_detector(img, blockSize, ksize, k)
	ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
	dst = np.uint8(dst)
	ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
	corners = cv2.cornerSubPix(gray, np.float32(centroids), (5,5), (-1, -1), criteria)
	return corners


def good_corners(img, numFeatures = 25):
	"""
	Finds corners via Shi-Tomasi Good Features To Track.
	Returns corners.
	"""
	gray = ImageIO.grayscale(img)
	corners = cv2.goodFeautresToTrack(gray, numFeatures, 0.01, 10)
	corners = np.int0(corners)
	return corners


def ravel_corners(corners):
	"""
	Ravels the coordinates to corners from good_corners.
	Coordinates in (x, y) format.
	"""
	pos = list()
	for i in corners:
		x, y = i.ravel()
		pos.append((x, y))
	return pos


def feature_detection(img):
	"""
	Feature Detection via ORB: Oriented FAST and Rotated BRIEF
	"""
	cv2.ocl.setUseOpenCL(False)
	orb = cv2.ORB_create()
	keypoints = orb.detect(img, None)
	keypoints, descriptors = orb.compute(img, keypoints)
	return keypoints, descriptors


def draw_keypoints(img, kp, color = (0, 255, 0), flags = 0):
	"""
	Draws the keypoints onto an image.
	"""
	tmp = cv2.drawKeypoints(img, kp, color = color, flags = flags)
	return tmp


def feature_match_bf_img(img1, img2):
	"""
	Brute-force feature matching between two images.
	Returns matches, keypoints of image 1, 
		    keypoints of image 2, descriptors of 1, 
		    descriptors of 2
	"""
	gray1 = ImageIO.grayscale(img1)
	gray2 = ImageIO.grayscale(img2)
	cv2.ocl.setUseOpenCL(False)
	orb = cv2.ORB()
	kp1, des1 = orb.detectAndCompute(gray1, None)
	kp2, des2 = orb.detectAndCompute(gray2, None)
	matches = feature_match_bf(kp1, des1, kp2, des2)[0]
	return matches, kp1, kp2, des1, des2


def feature_match_bf(kp1, des1, kp2, des2):
	"""
	Feature matching Brute Force with given kps and descriptors.
	"""
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
	matches = bf.match(des1, des2)
	matches = sorted(matches, key = lambda x:x.distance)
	return matches, kp1, kp2, des1, des2


def draw_matches(img1, kp1, img2, kp2, matches, numMatch = 10, flags = 2):
	"""
	Draws the matches between two images.
	"""
	img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:numMatch], flags = flags)
	return img3


# END OF FILE