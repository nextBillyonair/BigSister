import cv2
import numpy as np

"""
Class That Handles Face Detection.
Uses OpenCV's Haar Cascade Classifier to detect
faces in a given image.
"""

class FaceDetect:
    """
    Class to set up a Haar Cascade Face Detector
    """
    
    def __init__(self, haarFile = None):
        """
        Constructor Method.
        Optional haarFile, where def: haarcascades/haarcascade_frontalface_alt.xml
        """
        if haarFile is None:
            self.haar = 'haarcascades/haarcascade_frontalface_alt.xml'
        else:
            self.haar = haarFile

        self.face_cascade = cv2.CascadeClassifier(self.haar)


    def detectFaces(self, gray):
        """
        Detects Faces in a given grayscale image.
        Needs a grayscale image.
        Returns list of faces, where each face is 4-tuple of (x, y, w, h)
        """
        if gray.ndim != 2:
            gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.5, 2)
        return faces

    
    def detectAndDrawFaces(self, img, gray=None, color=(255, 0, 0), thickness = 2):
        """
        Detects and Draws Faces on image.
        Needs Color Image, and grayscale is optional.
        Color is optional; def: (255, 0, 0)
        Thickness is optional; def: 2
        Returns Color Image with Faces Drawn
        """
        if img.ndim != 3:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        if gray is None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif gray.ndim != 2:
            gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.5, 2)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
        return img


    def drawFaces(self, img, faces, color = (255, 0, 0), thickness = 2):
        """
        Draws a given set of Faces onto an image.
        Needs an image, faces
        Optional is color: (255, 0, 0), thickness = 2
        Returns image with faces drawn
        """
        if img.ndim != 3:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
        return img

    
    def getHaarFile(self):
        """
        Returns the haar file being used
        """
        return self.haar

    
    def getClassifier(self):
        """
        Returns the classifer created
        """
        return self.face_cascade
    
# END OF FILE
