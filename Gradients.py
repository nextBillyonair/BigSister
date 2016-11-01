"""
Gradients.py
"""
import cv2
import numpy as np
from ImageIO import grayscale

# Gradient Methods
def sobelx(img, ksize=5):
    gray = grayscale(img)
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
    return sx


def sobely(img, ksize=5):
    gray = grayscale(img)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
    return sy


def laplacian(img):
    gray = grayscale(img)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    return lap


def gradient_magnitude(img, ksize=5):
    gray = grayscale(img)
    x = sobelx(gray, ksize=ksize)
    y = sobely(gray, ksize=ksize)
    grad = np.absolute(np.sqrt(abs(x**2) + abs(y**2))/np.sqrt(2))
    val = np.amax(grad)
    grad = np.array((grad*255)/val, dtype=np.uint8)
    return grad


def canny(img, t1 = 100, t2 = 200, method = True):
    edges = cv2.Canny(img, t1, t2, L2gradient=method)
    return edges

    
