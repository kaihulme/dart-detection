import os
import sys
import cv2 as cv


def readfromargs(argv, loc="test"):
    if (len(sys.argv) == 2 and sys.argv[1][-4:] == (".jpg" or ".png")):
        name = argv[1][:-4]
        ext = argv[1][-4:]
        img = read(name, loc, ext)
        if img is None:
            raise ValueError(f"ERROR: no image data in {argv[1]}")
    else:
        raise ValueError("ERROR: excpected one .JPG image as argument!")
    return img, name


def read(name, loc, ext=".jpg"):
    path = getpath(name, loc, ext)

    print("path", path)

    if (os.path.exists(path)):
        img = cv.imread(path)
    else:
        raise ValueError("ERROR: image not found!")
    return img


def getpath(name, loc, ext=".png"):
    """
    Get file path given name and folder name.
    """
    dir = os.getcwd()
    if (loc == "test") : return dir + "/darts/resources/images/test/" + name + ext
    elif (loc == "out") : return dir + "/darts/out/" + name + ext
    else: return False