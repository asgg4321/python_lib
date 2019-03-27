# -*- coding: utf-8 -*-
# @Author    : Wing
# @Time      : 2019/3/21 23:09
# @File      : VideoCapture.py
import cv2
import numpy as np
cascPath = "../xml/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

def detect(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return image

capture = cv2.VideoCapture(0)

while True:
    ret,frame = capture.read()
    frame = detect(frame)
    cv2.imshow('capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
    