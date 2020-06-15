import cv2
import numpy as np


webcam = cv2.VideoCapture("http://192.168.0.5:4747/mjpegfeed")


### RED
# lower = np.array([15, 114, 105])
# upper = np.array([255, 255, 255]) 

### GREEN
# lower = np.array([50, 139, 74]) 
# upper = np.array([255, 255, 255]) 

### FACE
# lower = np.array([0, 31, 65])
# upper = np.array([12, 255, 255])

### B RED
# lower = np.array([156, 131, 119])
# upper = np.array([177, 255, 255])

### B GREEN
lower = np.array([55, 32, 101])
upper = np.array([80, 255, 255])

ret, frame = webcam.read()

maskImg = np.zeros(frame.shape, frame.dtype)
maskImg[:,:] = (10, 255, 10)

overlay = np.zeros(frame.shape, frame.dtype)

while True:
    ret, frame = webcam.read()
    frame = cv2.flip(frame, 1)

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, lower, upper)

    colorMask = cv2.bitwise_and(maskImg, maskImg, mask = mask)
    cv2.addWeighted(colorMask, 1, overlay, 1, 0, overlay)
    cv2.addWeighted(overlay, 1, frame, 1, 0, frame)
    cv2.imshow("Paint", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows



### COMMENTS

# cv2.imwrite("samples//sample.png", frame)
# cv2.addWeighted(redMask, 1, frame, 1, 0, frame)
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Mask", mask)
# side2side = np.concatenate((gray, mask), axis = 1)
# cv2.imshow("Side 2 Side", side2side)
# merge = cv2.addWeighted(frame, 0.4, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), 0.1, 0)
# cv2.imshow("Obraz", frame)


