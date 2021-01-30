import cv2
from utils import *

cap = cv2.VideoCapture(0)

while True:
    # capture the frame
    _, img = cap.read()

    # display the frame
    # img = face_focus(img)
    cv2.imshow('img', aschier(img))

    # stop if escape is pressed
    if cv2.waitKey(30) & 0xff == 27:
        break

cap.release()