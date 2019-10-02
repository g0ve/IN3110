import numpy as np
import cv2
import os.path
import sys
import time

# filename = "hellstrom.jpg"
"""
a = [ 1, 2, 3,
     4, 5, 6,
     7, 8, 9 ]
"""
def blur_image(src, dst):
    src = np.pad(src, 1, mode="edge")[:,:,1:4]

    dst = (src[1:-1, 1:-1, :] #5
    + src[1:-1, 0:-2, :] #2
    + src[1:-1, 2: , :] #8
    + src[0:-2, 1:-1, :] #4
    + src[2: , 1:-1, :]#6
    + src[0:-2, 0:-2, :] #1
    + src[2: , 0:-2, :]#9
    + src[0:-2, 2: , :] #7
    + src[2: , 2: , :])/9 #3


    return dst



def main(inputFile, outputFile):

    src = cv2.imread(inputFile)
    src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('Unblurred image', src)

    src = src.astype("uint32")
    dst = src.copy()


    dst = blur_image(src, dst)


    dst = dst.astype ("uint8")

    cv2.imwrite ("blurred_image.jpg ", dst)
    cv2.imshow('image', dst)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    start = time.time()
    print("__main__ is running")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file_exists = os.path.exists(filename)
    if file_exists:
        main(filename, "blurred_image.jpg")
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
    print ('{:.3f} sec'.format(time.time()- start))
