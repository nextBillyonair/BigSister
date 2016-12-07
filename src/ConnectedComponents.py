import numpy as np 
import cv2
import ImageIO

class ConnectedComponents:
	"""
	Class for Connected Components
	"""

	def __init__(self, connectivity = 4):
		self.num_labels = None
		self.label_img = None
		self.stats = None
		self.centers = None
		self.connectivity = connectivity


	def connected_components(self, img, connectivity = 4):
		th = self.threshold(img)
		output = cv2.connectedComponentsWithStats(binary_img, connectivity, cv2.CV_32S)
		self.num_labels = output[0] 
		self.label_img = output[1]
		self.stats = output[2]
		self.centers = output[3]
		self.connectivity = connectivity


	def threshold(self, img):
		img = ImageIO.grayscale(img)
		ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
		return thresh


	def get_bounding_rect_for_label(self, index):
		return self.stats[index][0:4]

	def get_bounding_rects(self):
		return self.stats[:,0:4]

	def get_area_for_label(self, index):
		return self.stats[index][4]

	def get_areas(self):
		return self.stats[:,4]

	def get_num_labels(self):
		return self.num_labels

	def get_label_img(self):
		return self.label_img

	def get_stats(self):
		return self.stats

	def get_centers(self):
		return self.centers

	def get_stat_for_index(self, index):
		return self.stats[index]

	def get_center_for_index(self, index):
		return self.centers[index]

	def set_connectivity(self, connect):
		if connect == 4 or connect == 8:
			self.connectivity = connect
		else:
			raise Exception


