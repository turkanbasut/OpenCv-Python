import cv2
import numpy as np

# This is a numpey function , not opencv function.

img = cv2.imread("Resources/alice.png")
image = cv2.imread("Resources/hatter.png")

# For this function to work correctly, it is important that the png sizes are equal.

hor = np.hstack((img, image))
ver = np.vstack((img, image))

cv2.imshow("Horizontal", hor)
cv2.imshow("Vertical", ver)
cv2.waitKey(0)

# With this method we can not resize he image it will come it is so
# if we want to stack two more images on right hand side it will take up whole space or it go out the frame
# So the other issue is the images do not have the same number of channels
# which means they are not RGB bot of them or maybe one of them is grey one of them is Rgb
# Then it will not work so both of them have to have the same number of channel because we are talking abaout matrices
