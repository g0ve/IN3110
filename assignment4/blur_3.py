import numpy as np
import cv2
import os.path
import sys
import time
from numba import jit


# filename = "hellstrom.jpg"
@jit(nopython=True)
def blur_image_python(src, dst):
    """
    This function is a copy of blur_1.py. But this time I use numba @jit to
    optimize the function from blur_1.py.

    Paramters:
        src - This is the source image. This is the image we want to blur.
        dst - This is a copy of our source image. In this image array is
                we do changes on.
    Return:
        Returns the processed image dst. 'dst' should be a blurred image of src.
    """
    (h, w, c) = src.shape

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

def main(inputFile, outputFile):
    """
    This is the main function. This function reads an image, call blur_image function.
    And then opens the blurred image with CV2. But before that it resize the source
    image and changes the type to uint32. After the image is processed it changes
    dst type to uint8.

    This also track the time used by the program.

    Paramters:
        inputFile - This is the source image you want to blur
        outputFile - This is the filename where you want to save the processed image.

    """

    src = cv2.imread(inputFile)
    src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)

    cv2.imshow('Unblurred image', src)

    src = src.astype("uint32")
    dst = src.copy()

    start = time.time()
    dst = blur_image_python(src, dst)
    print ('{:.3f} sec'.format(time.time()- start))

    dst = dst.astype ("uint8")

    cv2.imwrite (outputFile, dst)
    cv2.imshow('image', dst)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    print("__main__ is running")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file_exists = os.path.exists(filename)
    if file_exists:
        main(filename, "blurred_image.jpg")
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
