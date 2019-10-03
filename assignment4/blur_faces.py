import numpy as np
from numba import jit
import cv2
from blur_package import blur

def blur_sub_section(dst, sub_sec):
    """
    This function uses the blur_package to blur a sub section of a image. And
    then place that subsection back in the output image.

    Paramters:
        dst - original output image
        sub_sec - sub section of a image
    Return:
        Returns the processed image dst. 'dst' should have sub sections blurred
    """

    sub_sec = blur(sub_sec, sub_sec)

    dst[y:y+sub_sec.shape[0], x:x+sub_sec.shape[1], :] = sub_sec

    return dst



src = cv2.imread("blurred_faces.jpg")
dst = src.copy()

face_cascade = cv2.CascadeClassifier ("haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale (src, scaleFactor =1.025, minNeighbors =5, minSize =(30, 30))

faces = face_cascade.detectMultiScale(src, 1.1, 2, 0, (30, 30))

print ("Found {} faces !".format(len(faces)))
if len(faces) != 0:
    for (x, y, h, w) in faces:

        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face = dst[y:y+h, x:x+w, :]

        dst = blur_sub_section(dst, face)
        # for i in range(20):



cv2.imwrite("blurred_faces.jpg", dst)