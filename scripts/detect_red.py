#!/usr/bin/env python
"""  Brief demo of image processing using OpenCV Python bindings. 

Author: Nathan Sprague
Version: 3/24/2015
"""
import cv2
import numpy as np


def find_reddest_pixel(img):
    """ Return the pixel location of the reddest pixel in the image.

       Redness is defined as: redness = (r - g) + (r - b)

       Arguments:
            img - height x width x 3 numpy array of uint8 values.

       Returns:
            A tuple (x,y) containg the position of the reddest pixel.
    """
    # HINTS/ADVICE-------------
    # Use a nested for loop here.
    #
    # BE CAREFUL DOING ARITHMETIC WITH UNSIGNED INTEGERS: 
    # >>> a = np.array([2], dtype='uint8')
    # >>> b = np.array([3], dtype='uint8')
    # >>> a - b
    #     array([255], dtype=uint8)
    #
    # Reminder:
    # numpy arrays have a "shape" attribute that stores the layout:
    #    img.shape[0] - rows
    #    img.shape[1] - columns
    #    img.shape[2] - color channels

    max = 0
    img2 = np.array(img, dtype='int')
    for rows in range(0,img.shape[0]):
        for cols in range (0, img.shape[1]):
            r = img2[rows, cols, 2]
            b = img2[rows, cols, 0]
            g = img2[rows, cols, 1]
            redness = (r - g) + (r - b)
            if (redness > max):
                max = redness
                x = cols
                y = rows

    return (x, y)


def find_reddest_pixel_fast(img):
    """ Return the pixel location of the reddest pixel in the image.

       Redness is defined as: redness = (r - g) + (r - b)

       Arguments:
            img - height x width x 3 numpy array of uint8 values.

       Returns:
            A tuple (x,y) containg the position of the reddest pixel.
    """
    r = np.array(img[:,:,2], dtype='int')
    b = np.array(img[:,:,0], dtype='int')
    g = np.array(img[:,:,1], dtype='int')

    new = (r - g) + (r - b)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(new[:,:])

    return max_loc

def camera_loop():
    """
    Find and mark the reddest pixel in the video stream.
    """
    width = 320
    height = 240

    # Tell OpenCV which camera to use:
    capture = cv2.VideoCapture(0)

    # Set up image capture to grab the correct size:
    capture.set(3, width)
    capture.set(4, height)


    while True:
        # Grab the image from the camera.
        success, img = capture.read()

        # Find the most-red pixel:
        red_pixel = find_reddest_pixel_fast(img)

        # Draw a circle on the red pixel.
        # http://docs.opencv.org/modules/core/doc/drawing_functions.html
        cv2.circle(img, red_pixel, 5, (0, 255, 0), -1)

        cv2.imshow("Image", img)
        c = cv2.waitKey(33)

if __name__ == "__main__":
    camera_loop()
