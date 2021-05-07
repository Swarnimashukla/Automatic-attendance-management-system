import cv2
import dlib
import os
import sys
import sqlite3

#cam = cv2.VideoCapture(1)
detector = dlib.get_frontal_face_detector()

cam = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
ret, frame = cam.read()
ret, frame = cam.read()
ret, frame = cam.read()
count=1
cv2.imwrite("./pics/framee%d.jpg" % count, frame)
    
img = cv2.imread('./pics/framee1.jpg')
dets = detector(img, 1)
if not os.path.exists('./Cropped_faces'):
    os.makedirs('./Cropped_faces')
print("detected = {}".format(len(dets)))
for i, d in enumerate(dets):
    cv2.imwrite('./Cropped_faces/face' + str(i + 1) + '.jpg', img[d.top():d.bottom(), d.left():d.right()])

