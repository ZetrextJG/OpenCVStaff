import numpy as np
import cv2

webcam = cv2.VideoCapture("http://192.168.0.5:4747/mjpegfeed")

lower = np.array([50, 30, 60])
upper = np.array([80, 255, 255])

res1, image1 = webcam.read()

overlayImg = np.zeros(image1.shape, image1.dtype)

def draw_point(x, y):
    global overlayImg

    try:
        overlayImg[y, x] = 255
        overlayImg[y + 1, x] = 255
        overlayImg[y - 1, x] = 255
        overlayImg[y, x + 1] = 255
        overlayImg[y, x - 1] = 255

    except Exception as ex:
        print(ex)

while True:

    res, image = webcam.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)

    hsv_img = cv2.cvtColor(cv2.GaussianBlur(image, (7, 7), 0), 
        cv2.COLOR_BGR2HLS)

    mask = cv2.inRange(hsv_img, lower, upper)

    t_mask = cv2.bitwise_xor(mask, thresh, mask = mask) 

    coords = np.column_stack(np.where( t_mask > 0))

    if coords.any():

        # print(coords)
        pos = coords.mean(axis = 0)

        draw_point(int(pos[1]), int(pos[0]))
        # cv2.drawMarker(image, (int(pos[1]), int(pos[0])), (255, 0, 0))



    # cv2.imshow("Gray", gray)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Tresh", tresh)
    # cv2.imshow("Fillped", cv2.flip(image, 2))
    cv2.imshow("Image", image)

    cv2.imshow("Better Mask", t_mask)

    cv2.imshow("Lines", overlayImg)

    cv2.waitKey(1)
    