import cv2
import numpy as np
import ImageIO


class MotionDetect:
    """
    Class for Detecting Motion in an image, given a template.
    """
    
    
    def __init__(self, img_in):
        """
        Constructor
        """
        self.first_img = ImageIO.grayscale(img_in)

        
    def detectMotion(self, frame, window = (21, 21), min_area = 1500):
        """
        Method to Detect Motion
        """
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, window, 0)
        diff = cv2.absdiff(self.first_img, gray)
        thresh = cv2.threshold(diff, 45, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations = 2)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

        cnts = sorted(cnts, reverse=True, key=len)
        
        rectangles = list()
        
        for item in cnts:
            if cv2.contourArea(item) < min_area:
                continue

            rectangles.append(cv2.boundingRect(item))

        return rectangles


    def isMotion(self, frame):
        """
        Method to see if there is motion in a given frame.
        Takes an image and returns the following:
        False, -1 if no motion
        True, rects if motion (returns rectangles to help user avoid duplicate method calls)
        """
        rects = self.detectMotion(frame)
        if len(rects) == 0:
            return False, -1
        return True, rects


    def drawRectangles(self, frame, rect):
        """
        Draws rectangles onto frame.
        """
        for r in rect:
            (x, y, w, h) = r
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        return frame

    
    def setFrame(self, frame):
        """
        Sets the template image used.
        """
        self.first_img = ImageIO.grayscale(frame)

        
# END OF FILE
