import cv2
import numpy as np
from Camera import URLCamera
from cvaux import *
from FaceDetect import FaceDetect

url = "http://polaris.acm.jhu.edu/motion/thread2/lastimage.jpg?time=1474063328843"
url2 = "http://polaris.acm.jhu.edu/motion/thread1/lastimage.jpg?time=1474064133272"

cam1 = URLCamera(url)
cam2 = URLCamera(url2, 2)
fd = FaceDetect()

try:
    for x in range(100):
        img = cam1.fetch()
        img2 = cam2.fetch()
        imgGray = grayscale(img)
        img2Gray = grayscale(img2)
        face1 = fd.detectFaces(imgGray)
        face2 = fd.detectFaces(img2Gray)
        img = fd.drawFaces(img, face1)
        img2 = fd.drawFaces(img2, face2)
        show(img, "Bookcase Cam", 1000)
        show(img2, "Computer Cam", 1000)

except KeyboardInterrupt:
    print "Keyboard Interrupt...\nDestroying All Windows..."
    destroyWindows()
