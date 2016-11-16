import cv2
import numpy as np
import ImageIO

"""
Module Containing methods for Image Processing
"""

def threshold(img, threshold = 127, invert=False):
	"""
	Method to quickly compute the binary image.
	"""
	gray = ImageIO.grayscale(img)
	if invert:
		ret, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)
		return thresh
	ret, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
	return thresh


def adaptiveGaussian(img):
	"""
	Method to threshold using a threshold value that is 
	the weighted sum of neighbourhood values where 
	weights are a gaussian window.
	"""
	gray = ImageIO.grayscale(img)
	gray = cv2.medianBlur(img, 5)
	gaussThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	return gaussThresh


def adaptiveMean(img):
	"""
	Method to threshold using a  threshold value that is 
	the mean of neighbourhood area.
	"""
	gray = ImageIO.grayscale(img)
	gray = cv2.medianBlur(img, 5)
	meanThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
	return meanThresh	


def otsu(img):
	gray = ImageIO.grayscale(img)