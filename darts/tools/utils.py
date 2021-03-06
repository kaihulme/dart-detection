import os
import math
import cv2 as cv
import numpy as np
from skimage.feature.peak import peak_local_max


def threshold(frame, threshold):
    """
    Set values in frame below threshold to 0.
    """
    frame_copy = np.copy(frame)
    frame_copy[frame_copy < threshold] = 0
    return frame_copy


def threshold_abs(frame, threshold):
    """
    Set values in frame below threshold to 0 and above to 255.
    """
    frame_copy = np.copy(frame)
    frame_copy[frame_copy < threshold] = 0
    frame_copy[frame_copy >= threshold] = 255
    return frame_copy


def normalise(frame):
    """
    MinMax normalisation of frame between 0-255
    """
    frame_copy = np.copy(frame)
    min = np.min(frame_copy)
    max = np.max(frame_copy)
    if (max - min != 0) : frame_copy = (frame - min) / (max - min) * 255
    return frame_copy


def localmaxima(frame, min_dist):
    centres = peak_local_max(frame, min_dist)
    return centres


def radtodeg(frame):
    """
    Convert a matrix of radian angles to degrees.
    """
    pi = math.pi
    rows, cols = frame.shape
    deg_frame = np.zeros((rows, cols))
    for y in range(rows):
        for x in range(cols):
            rad = frame[y][x]
            deg = (rad if rad >= 0 else 2*pi + rad) * 360 / 2*pi
            deg_frame[y][x] = deg
    return deg_frame