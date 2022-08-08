import cv2

cap = cv2.VideoCapture("Resources/helloworld.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    # if we press q it will close.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

