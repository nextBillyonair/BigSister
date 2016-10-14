import picamera
import cv2
import numpy


def detectFaces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    return img



camera = picamera.PiCamera()

camera.rotation = 90

#camera.resolution = (30, 30 )
cv2.namedWindow("Results", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("Results", cv2.WINDOW_NORMAL)

while True:
    #input = raw_input("Ready?")
    camera.capture('image.jpg')
    image = cv2.imread('image.jpg')
    image = detectFaces(image)
    cv2.imshow("Results", image)
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        break
print "ENDING PROGRAM"
    



"""
camera.start_preview()
while True: pass
camera.stop_preview()
"""
