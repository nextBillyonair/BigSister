import cv2
import numpy as np

"""
Two classes for optical flow analysis.
"""

class Dense_Optical_Flow:
	"""
	Module to implement self-contained Farneback Optical Flow
	I prefer this class.
	"""


	def __init__(self):
		"""
		Noting to init.
		"""
		pass


	def dense_opti_flow(self, old_frame, new_frame):
		"""
		Given an old frame and new frame, in color, finds the Optical Flow
		via Farneback method. Returns the flow.
		"""
		prevgray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
		flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
		return flow


	def draw_flow(self, frame, flow, step = 16):
		"""
		Given a color frame and the flow, with optional step size (for overlay grid),
		draws the flow onto a copy of frame, returning the flow-overlayed frame.
		"""
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		h, w = frame.shape[:2]
		y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2, -1).astype(int)
		fx, fy = flow[y,x].T
		lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
		lines = np.int32(lines + 0.5)
		vis = frame.copy()
		cv2.polylines(vis, lines, 0, (0, 255, 0))
		for (x1, y1), (x2, y2) in lines:
			cv2.circle(vis, (x1, y1), 1, (0, 255, 255), -1)
		return vis


	def get_fx_fy(self, flow, step = 16):
		"""
		Given a flow and optional step size, returns the derivatives (i.e. f_x and f_y) for each pixel in step size
		Used to simplify interpretation of the flow.
		"""
		h, w = flow.shape[:2]
		y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2, -1).astype(int)
		fx, fy = flow[y, x].T
		return fx, fy




class Lucas_Kanade_Optical_Flow:
	"""
	Class to implement the Lucas-Kanade Optical Flow.
	"""

	def __init__(self, features = None, lk = None):
		"""
		Init LK.
		Sets the params for feature detection and Lucas-Kanade Optical Flow Algorithm.
		Also creates a random color array.
		"""
		# params for the ShiTomasi corner detection
		if features is None:
			self.features_param = dict( maxCorners = 500, qualityLevel = 0.3, minDistance = 7, blockSize = 7 )
		else:
			self.features_param = features

		# params for lucas kanade optical flow
		if lk is None:
			self.lk_params = dict( winSize = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03) )
		else:
			self.lk_params = lk

		# random colors
		self.color = np.random.randint(0, 255, (100, 3))


	def find_flow(self, old_frame, new_frame):
		"""
		Given an old and new frame, in color,
		Finds features in old, then finds the opti-flow via LK between old and new.
		Only selects the good points in old and new lists.
		Returns good new points and good old points, can be later used to draw flow, etc.
		"""
		# take the first frame and find corners
		old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
				
		p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **self.features_param)

		# mask for drawing flow
		frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
		
		# Calcs the Optical Flow between old and new gray images
		p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **self.lk_params)

		# Selects the good points in flow
		good_new = p1[st==1]
		good_old = p0[st==1]

		return good_new, good_old


	def draw_flow(self, frame, new, old):
		"""
		Draws the flow.
		Given frame in color.
		Given new and old points from flow calculation.
		Draws flow between old and new points.
		Returns flow-img
		"""
		mask = np.zeros_like(frame)
		for i, (new, old) in enumerate(zip(new, old)):
			a, b = new.ravel()
			c, d = old.ravel()
			mask = cv2.line(mask, (a,b), (c,d), self.color[i].tolist(), 2)
			frame = cv2.circle(frame, (a,b), 5, self.color[i].tolist(), -1)
		img = cv2.add(frame, mask)
		return img


	def find_features(self, frame):
		"""
		Method to find a list of features given a color frame.
		"""
		old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **self.features_param)
		return p0


	def get_feature_params(self):
		"""
		Method to get current feature params
		"""
		return self.features_param


	def set_feature_params(self, f):
		"""
		Method to reset feature params.
		"""
		self.features_param = f


	def get_lk_params(self):
		"""
		Method to get current lk params.
		"""
		return self.lk_params


	def set_lk_params(self, l):
		"""
		Resets lk params to l.
		"""
		self.lk_params = l


	def get_data_fields(self):
		"""
		Returns dictionary of current params being used for lk opti flow.
		"""
		fields = dict( lk = self.lk_params, features = self.features_param)
		return fields


	def get_distances(self, new, old):
		"""
		Method to find change in distance between old and new points.
		Returns numpy array of distance changes.
		"""
		length = new.shape[0]
		fx = np.zeros(length)
		fy = np.zeros(length)

		for i, (new, old) in enumerate(zip(new, old)):
			a, b = new.ravel() # x vals
			c, d = old.ravel() # y vals
			x = a - c
			y = b - d
			fx.itemset(i, x)
			fy.itemset(i, y)

		return fx, fy
