import cv2
import numpy
import wget
import os

def detectFaces(image, gray):
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_upperbody.xml')
    faces = face_cascade.detectMultiScale(gray, 1.5, 2)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
    return image


url = "http://polaris.acm.jhu.edu/motion/thread2/lastimage.jpg?time=1474063328843"
url2 = "http://polaris.acm.jhu.edu/motion/thread1/lastimage.jpg?time=1474064133272"

for x in range(100):
    filename = wget.download(url, "lastimage.jpg")
    file2 = wget.download(url2, "lastimage2.jpg")
    os.rename(filename, "lastimage.jpg")
    os.rename(file2, "lastimage2.jpg")
    img = cv2.imread("lastimage.jpg")
    img2 = cv2.imread("lastimage2.jpg")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img = detectFaces(img, imgGray)
    img2 = detectFaces(img2, img2Gray)
    cv2.namedWindow("Bookcase Cam", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Computer Cam", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Bookcase Cam", 500, 500)
    cv2.resizeWindow("Computer Cam", 500, 500)
    cv2.imshow("Bookcase Cam", img)
    cv2.imshow("Computer Cam", img2)
    cv2.waitKey(1000)
    
