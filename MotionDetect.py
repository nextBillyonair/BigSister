import cv2
import numpy as np
import ImageIO
import Rectangle


class MotionDetect:
    """
    Class for Detecting Motion in an image
    """
    
    
    def __init__(self):
        """
        Constructor
        """
        pass

        
    def detect_motion(self, old_frame, new_frame, window = (21, 21), min_area = 1500):
        """
        Method to Detect Motion
        """
        
        gray_old = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        gray_old = cv2.GaussianBlur(gray_old, window, 0)
        gray_new = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
        gray_new = cv2.GaussianBlur(gray_new, window, 0)
        diff = cv2.absdiff(gray_new, gray_old)
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


    def intermediate_steps(self, old_frame, new_frame, window = (21, 21), min_area = 500):
        """
        Debug method meant for returning intermediate_steps of algo.
        """
        
        gray_old = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        gray_old = cv2.GaussianBlur(gray_old, window, 0)
        gray_new = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
        gray_new = cv2.GaussianBlur(gray_new, window, 0)
        diff = cv2.absdiff(gray_new, gray_old)
        thresh = cv2.threshold(diff, 5, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations = 2)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

        cnts = sorted(cnts, reverse=True, key=len)
        
        rectangles = list()
        
        for item in cnts:
            if cv2.contourArea(item) < min_area:
                continue

            rectangles.append(cv2.boundingRect(item))
       
       	#MUST FIND ALGO TO ONLY RET OVERLAPS!!!

        return diff, thresh, rectangles


    def is_motion(self, frame):
        """
        Method to see if there is motion in a given frame.
        Takes an image and returns the following:
        False, -1 if no motion
        True, rects if motion (returns rectangles to help user avoid duplicate method calls)
        """
        rects = self.detect_motion(frame)
        if len(rects) == 0:
            return False, -1
        return True, rects
