import numpy as np
from numba import jit
import cv2
import blur_package

blur = blur_package.blur

src = cv2.imread("beatles.jpg")
# src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)

dst = src.copy()

face_cascade = cv2.CascadeClassifier ("haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale (src, scaleFactor =1.025, minNeighbors =5, minSize =(30, 30))

faces = face_cascade.detectMultiScale(src, 1.1, 2, 0, (30, 30))

print ("Found {} faces !".format(len(faces)))

if len(faces) != 0:
    for (x, y, w, h) in faces:

        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face = dst[y:y+h, x:x+w]

        face = blur(face, face)

        dst[y:y+face.shape[0], x:x+face.shape[0]] = face


cv2.imwrite("blurred_faces.jpg", dst)