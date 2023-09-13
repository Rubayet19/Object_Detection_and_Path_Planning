import time
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO

buzzer = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
camera = PiCamera()
camera.resolution = (320, 240)  # a smaller resolution means faster processing
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(320, 240))
kernel = np.ones((2, 2), np.uint8)
time.sleep(0.1)
for still in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    GPIO.output(buzzer, False)

    image = still.array
    # create a detection area
    widthAlert = np.size(image, 1)  # get width of image
    heightAlert = np.size(image, 0)  # get height of image
    yAlert = (heightAlert / 2) + 100  # determine y coordinates for area
    cv2.line(image, (0, yAlert), (widthAlert, yAlert), (0, 0, 255), 2)  # draw a line to show area

    lower = [1, 0, 20]
    upper = [60, 40, 200]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    # use the color range to create a mask for the image and apply it to the image
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    dilation = cv2.dilate(mask, kernel, iterations=3)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
    edge = cv2.Canny(closing, 175, 175)

    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    threshold_area = 400
    centres = []

    if len(contours) != 0:

        for x in contours:
            # find the area of each contour
            area = cv2.contourArea(x)
            # find the center of each contour
            moments = cv2.moments(x)
            # weed out the contours that are less than our threshold
            if area > threshold_area:

                (x, y, w, h) = cv2.boundingRect(x)

                centerX = (x + x + w) / 2
                centerY = (y + y + h) / 2

                cv2.circle(image, (centerX, centerY), 7, (255, 255, 255), -1)

                if ((y + h) > yAlert):
                    cv2.putText(image, "ALERT!", (centerX - 20, centerY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2)
                    GPIO.output(buzzer, True)

    cv2.imshow("Display", image)

    rawCapture.truncate(0)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        GPIO.output(buzzer, False)
        break