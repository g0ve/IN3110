import numpy as np
from numba import jit
import cv2
import os.path
import sys

# filename = "hellstrom.jpg"
@jit
def blur(src, dst):
    (h, w, c) = src.shape
    #Skifte på imagene.

    for x in range(h-1):
        for y in range(w-1):
            for z in range(c):
                if x != 0 or y != 0:
                    dst[x, y, z] = (src[x, y, z]
                    + src[x-1, y, z]
                    + src[x+1, y, z]
                    + src[x, y-1, z]
                    + src[x, y+1, z]
                    + src[x-1, y-1, z]
                    + src[x-1, y+1, z]
                    + src[x+1, y-1, z]
                    + src[x+1, y+1, z]) / 9
                if x == 0:
                    dst[x, y, z] = (src[x, y, z]
                    + src[x, y, z]
                    + src[x+1, y, z]
                    + src[x, y-1, z]
                    + src[x, y+1, z]
                    + src[x, y-1, z]
                    + src[x, y+1, z]
                    + src[x+1, y-1, z]
                    + src[x+1, y+1, z]) / 9
                if y == 0:
                    dst[x, y, z] = (src[x, y, z]
                    + src[x-1, y, z]
                    + src[x+1, y, z]
                    + src[x, y, z]
                    + src[x, y+1, z]
                    + src[x-1, y, z]
                    + src[x-1, y+1, z]
                    + src[x+1, y, z]
                    + src[x+1, y+1, z]) / 9
    return dst

def blur_image(input_filename, output_filename=None):
    file_exists = False
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file_exists = os.path.exists(filename)
    if file_exists:
        src = cv2.imread(inputFile)

        src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)

        src = src.astype("uint32")
        dst = src.copy()

        dst = blur(src, dst)

        dst = dst.astype ("uint8")

        if output_filename != None:
            cv2.imwrite (output_filename, dst)
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
    return dst


