import cv2
import numpy as np
import os
import urllib

class WebCamera:
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

        
    def download(self, filename = "tmp.jpg"):
        """
        Downloads an image from url camera
        Filename is optional; def: tmp.jpg
        Returns: filename
        """
        urllib.urlretrieve(self.urlPath, filename)
        return filename

    
    def fetch(self):
        """
        Fetches an image and only an image, i.e gets file, loads to OpenCV array
        and then deletes file, returning img only.
        """
        filename = "tmp%d.jpg" % self.num
        urllib.urlretrieve(self.urlPath, filename)
        img = cv2.imread(filename)
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

# END OF FILE
