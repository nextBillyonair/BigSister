import numpy as np
import cv2
import os
from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep

class RPICamera:
    """
    This is a testing class for the RPI camera, to work in a similiar
    manner to the classes in camera.py, except it will only work on 
    a RPI camera, and hence will not be included in the camera file
    for dependency issues.
    """


    def __init__(self):
        self.camera = PiCamera()
        self.raw = PiRGBArray(self.camera)
        

    def rotate(self, rot):
        self.camera.rotation = rot

    def capture(self, filename = 'test.jpg'):
        self.camera.capture(filename)

    def fetch(self):
        self.camera.capture(self.raw, format="bgr")
        img = self.raw.array
        self.raw.truncate(0)
        return img

    def resolution(self, res):
        self.camera.resolution = res
        self.raw = PiRGBArray(self.camera, size=res)

    def framerate(self, fr):
        self.camera.framerate = fr
