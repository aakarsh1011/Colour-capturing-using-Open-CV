import cv2 as cv
import numpy as np

device = cv.VideoCapture(0)
while True:
    ret,frame = device.read()

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_range_blue = np.array([110,50,50])
    upper_range_blue = np.array([130,225,225])
    mask1 = cv.inRange(hsv,lower_range_blue,upper_range_blue)


    lower_range_red = np.array([150,70,50])
    upper_range_red = np.array([180,225,150])
    mask2 = cv.inRange(hsv,lower_range_red,upper_range_red)


    lower_range_green = np.array([45,100,50])
    upper_range_green = np.array([75,225,225])
    mask3 = cv.inRange(hsv,lower_range_green,upper_range_green)



    cv.imshow('show',frame)


    result1 = cv.bitwise_and(frame,frame,mask = mask1)
    result2 = cv.bitwise_and(frame,frame,mask = mask2)
    result3 = cv.bitwise_and(frame,frame,mask = mask3)


    cv.imshow('blue', result1)
    cv.imshow('red', result2)
    cv.imshow('green', result3)


    if cv.waitKey(1)==13:
        break

device.release()
cv.destroyAllWindows()
