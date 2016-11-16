import cv2
import numpy as np

"""
Auxillary Computer Vision Functions Module
"""

def grayscale(img):
    """
    Returns a grayscale version of img
    Needs an image
    Returns: Grayscale image
    """
    if img is None:
        print "Image is None"
        raise Exception
    if len(img.shape) > 2:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def show(img, name="IMAGE", wait=0):
    """
    Displays an Image onto the screen and waits for user to close
    Needs: image to display; 
    Optionals: string name of window, def is IMAGE;
    time in ms for screen to wait, def:0 - INDEFINITE
    """
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, img)
    cv2.waitKey(wait) & 0xFF


def displayImgs(imgs, titles = None, wait=0):
    """
    Displays a list of images
    Needs: list of images
    Optionals: list of titles of images
    wait time in ms ffor screen; def: 0 - INDEFINITE
        """
    if len(imgs) > 100:
        print "WARNING: DisplayImgs: List is of length " + str(len(imgs))
        print "Please reduce list size to avoid improper display"
        raise Exception
    if titles is None:
        count = 1
        for i in imgs:
            cv2.namedWindow("IMAGE" + str(count), cv2.WINDOW_NORMAL)
            cv2.imshow("IMAGE" + str(count), i)
            count += 1
    else:
        count = 0
        for i in imgs:
            cv2.namedWindow(titles[count], cv2.WINDOW_NORMAL)
            cv2.imshow(titles[count], i)
            count += 1
    cv2.waitKey(wait) & 0xFF


def destroyWindows():
    """
    Destroys all GUI windows opened
    """
    cv2.destroyAllWindows()


def toHSV(img):
    """
    Returns a hsv version of img
    Needs: image
    Returns: HSV image
    """
    if img is None:
        print "Img is None"
        raise Exception
    gray = grayscale(img)
    res = cv2.applyColorMap(gray, 9)
    return res


def toJET(img):
    """
    Returns a jet version of img
    Params: image
    Returns: JET image
    """
    if img is None:
        print "Img is None"
        raise Exception
    gray = grayscale(img)
    res = cv2.applyColorMap(gray, 2)
    return res



