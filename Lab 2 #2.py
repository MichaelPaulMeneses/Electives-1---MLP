import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vecteezy_hello-neon-light-title-animation-on-wall-great-for_23960299.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()