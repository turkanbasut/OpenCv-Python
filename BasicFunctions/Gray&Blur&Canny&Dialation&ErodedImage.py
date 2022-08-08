import cv2
import os
import numpy as np

path = "Your path reference"

if os.path.exists(path):
    img = cv2.imread(path)
    kernel = np.ones((5, 5), np.uint8)
    imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imBlur = cv2.GaussianBlur(imGray, (7, 7), 0)
    imCanny = cv2.Canny(img, 100, 100)
    imDialation = cv2.dilate(imCanny, kernel, iterations=1)
    imEroded = cv2.erode(imDialation, kernel, iterations=1)

    cv2.imshow("Gray Image", imGray)
    cv2.imshow("Blur Image", imBlur)
    cv2.imshow("Canny Image", imCanny)
    cv2.imshow("Dialation Image", imDialation)
    cv2.imshow("Eroded Image", imEroded)
    cv2.waitKey(0)
else:
    print("Path does not exist:", path)
