import cv2
import numpy as np

def draw_flow(img, flow, step=16):
	"""
	"""
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    # print np.sum(fx)
    # print np.sum(fy)
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(vis, lines, 0, (0, 255, 0))
    ra = np.array([])
    for (x1, y1), (x2, y2) in lines:
    	# np.append(ra, [np.linagl.norm()])
        cv2.circle(vis, (x1, y1), 1, (0, 255, 255), -1)
    print lines
    # print np.sum()
    return vis


def denseOptiFlow():
	cam = cv2.VideoCapture(1)
	ret, prev = cam.read()
	prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
	# for i in xrange(1):
	while (1):
		ret, img = cam.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
		prevgray = gray
		cv2.imshow('flow', draw_flow(gray, flow))
		ch = 0xFF & cv2.waitKey(5)



def lk():
	cap = cv2.VideoCapture(1)
	features_param = dict(maxCorners = 100,
						  qualityLevel = 0.3,
						  minDistance = 7,
						  blockSize = 7 )
	lk_params = dict( winSize = (15,15),
					  maxLevel = 2,
					  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

	color = np.random.randint(0, 255, (100,3))

	ret, old_frame = cap.read()
	old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
	p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **features_param)

	mask = np.zeros_like(old_frame)

	while(1):
		ret, frame = cap.read()
		frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

		good_new = p1[st==1]
		good_old = p0[st==1]

		for i, (new, old) in enumerate(zip(good_new, good_old)):
			a, b = new.ravel()
			c, d = old.ravel()
			mask = cv2.line(mask, (a,b), (c,d), color[i].tolist(), 2)
			frame = cv2.circle(frame, (a,b), 5, color[i].tolist(), -1)
		img = cv2.add(frame, mask)

		cv2.imshow('frame', img)
		k = cv2.waitKey(30) & 0xFF
		if k == 27:
			break

		old_gray = frame_gray.copy()
		p0 = good_new.reshape(-1, 1, 2)

	cv2.destroyAllWindows()
	cap.release()




