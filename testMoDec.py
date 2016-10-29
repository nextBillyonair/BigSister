import cv2
import numpy as np
from Camera import WebCamera, URLCamera
from cvaux import *
from MotionDetect import MotionDetect

url = "http://polaris.acm.jhu.edu/motion/thread2/lastimage.jpg?time=1474063328843"
url2 = "http://polaris.acm.jhu.edu/motion/thread1/lastimage.jpg?time=1474064133272"

#cam1 = URLCamera(url)
#cam2 = URLCamera(url2, 2)
cam3 = WebCamera()
##md1 = MotionDetect(cam1.fetch())
#md2 = MotionDetect(cam2.fetch())
#cam1.download()
#cam2.download()

md3 = MotionDetect(cam3.fetch())

while True:
    img = cam3.fetch()
    k = cv2.waitKey(0)
    cv2.imshow("Good?", img)
    if k & 0xFF == ord("q"):
        break

md3.setFrame(img)

try:
    for x in range(1000):
        #img = cam1.fetch()
        #img2 = cam2.fetch()
        img3 = cam3.fetch()
        
        #rec1 = md1.detectMotion(img)
        #rec2 = md2.detectMotion(img2)
        rec3 = md3.detectMotion(img3)

        #img = md1.drawRectangles(img, rec1)
        #img2 = md2.drawRectangles(img2, rec2)
        img3 = md3.drawRectangles(img3, rec3)

        #show(img, "Bookcase Cam", 1)
        #show(img2, "Computer Cam", 1)
        show(img3, "Web Cam", 1)

except KeyboardInterrupt:
    print "Keyboard Interrupt...\nDestroying All Windows..."
    destroyWindows()
