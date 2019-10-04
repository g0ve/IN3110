import numpy as np
import cv2
import os.path
import sys
import time

# filename = "hellstrom.jpg"

def blur_image(src, dst):
    """
    This function blurs a given image. This is done by looping trought the image
    array, and find the average value of all the neighbors to the chossen element.

    Paramters:
        src - This is the source image. This is the image we want to blur.
        dst - This is a copy of our source image. In this image array is
                we do changes on.
    Return:
        Returns the processed image dst. 'dst' should be a blurred image of src. Type: ndarray
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
    print(src.shape)

    cv2.imshow('Source image', src)

    src = src.astype("uint32")
    dst = src.copy()

    start = time.time()
    dst = blur_image(src, dst)
    print ('{:.3f} sec'.format(time.time()- start))

    dst = dst.astype ("uint8")

    cv2.imwrite (outputFile, dst)
    cv2.imshow('Blurred image', dst)
    cv2.waitKey(5000)
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
