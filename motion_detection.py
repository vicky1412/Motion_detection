import cv2
import time
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

video.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
while True:

    check,frame = video.read()
    print(frame)
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,1)

    cv2.imshow("image",frame)
    key = cv2.waitKey(1)

    if key ==ord('q'):
        break
video.release()