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
	Method to threshold using a threshold value that is 
	the mean of neighbourhood area.
	"""
	gray = ImageIO.grayscale(img)
	gray = cv2.medianBlur(img, 5)
	meanThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
	return meanThresh	


def otsu(img):
	"""
	Method to threshold via a OTSU binarization
	"""
	gray = ImageIO.grayscale(img)
	gray = cv2.GaussianBlur(img, (5,5), 0)
	ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return th


def fft_ra(ra):
	"""
	Fast Fourier Transform in 1-D.
	"""
	f = np.fft.rfft(ra)
	fshift = np.fft.fftshift(f)
	return fshift


def fft_img(img):
	"""
	Fast Fourier Transform in 2-D.
	"""
	gray = ImageIO.grayscale(img)
	f = np.fft.fft2(gray)
	fshift = np.fft.fftshift(f)
	return fshift


def fshift_to_mag(fs):
	"""
	Takes a FFT result and returns the Mag Spec.
	"""
	magnitude_spectrum = 20 * np.log(np.abs(fs))
	return magnitude_spectrum


def ifft_ra(ra):
	"""
	Inverse Fast Fourier Transform in 2-D.
	"""
	f_ishift = np.fft.ifftshift(ra)
	inv = np.fft.ift(f_ishift)
	return inv


def ifft_img(fshift):
	"""
	Inverse Fast Fourier Transform in 2-D.
	"""
	f_ishift = np.fft.ifftshift(fshift)
	img_back = np.fft.ifft2(f_ishift)
	img_back = np.abs(img_back)
	return img_back




