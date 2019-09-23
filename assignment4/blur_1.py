import numpy as np
import cv2
import os.path
import sys

# filename = "hellstrom.jpg"

def blur_image(src, dst):
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


if len(sys.argv) == 2:
    filename = sys.argv[1]
    file_exists = os.path.exists(filename)
    if file_exists:
        src = cv2.imread(filename)
        # print(src.shape)
        # print(type(src))
        src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
        # src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        cv2.imshow('Unblurred image', src)
        src = src.astype("uint32")

        dst = src.copy()
        print(dst.shape)

        dst = blur_image(src, dst)

        dst = dst.astype ("uint8")

        cv2.imwrite ("blurred_image.jpg ", dst)
        cv2.imshow('image', dst)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
