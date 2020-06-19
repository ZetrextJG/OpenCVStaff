import numpy as np
import cv2


webcam = cv2.VideoCapture(0)

webcam.set(cv2.CAP_PROP_XI_HEIGHT, 1280)

webcam.set(cv2.CAP_PROP_XI_WIDTH, 720)

standard = 0.5

webcam.set(cv2.CAP_PROP_GAIN, standard)


def change_gain(a):
    global webcam
    webcam.set(cv2.CAP_PROP_GAIN, float(a / 100))


# webcam.set(cv2.CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ, 50)

### http://192.168.0.5:4747/mjpegfeed

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 240)
cv2.createTrackbar("Gain", "TrackBar", int(webcam.get(cv2.CAP_PROP_GAIN) * 100), 100, change_gain)



while True:
    result, frame = webcam.read()

    ### REVERS
    frame = cv2.flip(frame, 2)

    ### FRAME OVERLAY
    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 5)


    ### SHOWIING THE IMAGE
    cv2.imshow("Video", frame)

    ### UPDATING THE TRACKERS


    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.imwrite("samples/fast_sample.png", frame)
        break
