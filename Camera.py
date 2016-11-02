import cv2
import numpy as np
import os
import urllib
import datetime

class URLCamera:
    """
    Class to retrieve images from a camera posted on the web, i.e. the two web
    cams in the ACM office.
    """


    def __init__(self, url, camNum = 1):
        """
        Constructor
        Needs url to webcam images
        Needs camera number if multiple cams, def: 1
        """
        self.urlPath = url
        self.num = camNum

        
    def download(self, filename = None):
        """
        Downloads an image from url camera
        Filename is optional; def: tmp.jpg
        Returns: filename
        """
        if filename is None:
            iso_time = datetime.datetime.now().isoformat()
            filename = "Cam%d-%s.png" % (self.num, iso_time)
        urllib.urlretrieve(self.urlPath, filename)
        return filename

    
    def fetch(self):
        """
        Fetches an image and only an image, i.e gets file, loads to OpenCV array
        and then deletes file, returning img only.
        """
        iso_time = datetime.datetime.now().isoformat()
        filename = "Cam%d-%s.png" % (self.num, iso_time)
        urllib.urlretrieve(self.urlPath, filename)
        img = cv2.imread(filename)
        print filename
        if img is None:
            print "File Not Found: %s" % filename
            raise Exception
        os.remove(filename)
        return img


    def getCamNum(self):
        """
        Gets the Camera Number
        """
        return self.num


    def getUrl(self):
        """
        Gets the URL path for current cam
        """
        return self.urlPath
    
    
    def setUrl(self, newUrl):
        """
        Sets the URL path for the Camera
        """
        self.urlPath = newUrl

        
    def setCamNum(self, newNum):
        """
        Sets the Camera Number
        """
        self.num = newNum


class WebCamera:
    """
    Class for setting up a web camera. 
    """


    def __init__(self, camNum = 0):
        """
        Constructor
        """
        self.cap = cv2.VideoCapture(camNum)


    def fetch(self):
        """
        Fetches a frame from camera.
        """
        ret, frame = self.cap.read()
        if not ret:
            print "Could not read from camera."
            raise Exception
        return frame


    def capture(self, filename = None):
        """
        Captures and saves an image.
        Returns the file saved to.
        """
        if filename is None:
            iso_time = datetime.datetime.now().isoformat()
            filename = "CamWeb-%s.png" % (iso_time)
        ret, frame = self.cap.read()
        cv2.imwrite(frame, filename)
        return filename
    
    
    def destroy(self):
        """
        Releases a camera from use.
        """
        self.cap.release()


    def isOpened(self):
        """
        Returns if camera is opened.
        """
        return self.cap.isOpened()


# END OF FILE
