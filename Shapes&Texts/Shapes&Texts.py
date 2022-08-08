import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 250), (0, 0, 255), 3)
cv2.circle(img, (400, 50), 30, (255, 255, 0), cv2.FILLED)

# Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
cv2.putText(img, "HELLO WORLD!", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 150, 0), 1)

# Parameters:
# image: It is the image on which text is to be drawn.
# text: Text string to be drawn.

# org: It is the coordinates of the bottom-left corner of the text string in the image.
# The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).

# font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.
# fontScale: Font scale factor that is multiplied by the font-specific base size.
# color: It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the line in px.
# lineType: This is an optional parameter.It gives the type of the line to be used.

# bottomLeftOrigin: This is an optional parameter. 
# When it is true, the image data origin is at the bottom-left corner.
# Otherwise, it is at the top-left corner.
# Return Value: It returns an image.


cv2.imshow("Image", img)

cv2.waitKey(0)
