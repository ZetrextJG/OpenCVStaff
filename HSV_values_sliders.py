import cv2
import numpy as np

img = cv2.imread('samples/sample.png')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Image", img)
cv2.imshow("HSV", hsv_img)

def nothing(a):
    print(a)


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue min", 'TrackBars', 0, 255, nothing)
cv2.createTrackbar("Hue max", 'TrackBars', 255, 255, nothing)
cv2.createTrackbar("Sat min", 'TrackBars', 0, 255, nothing)
cv2.createTrackbar("Sat max", 'TrackBars', 255, 255, nothing)
cv2.createTrackbar("Val min", 'TrackBars', 0, 255, nothing)
cv2.createTrackbar("Val max", 'TrackBars', 255, 255, nothing)


while True:
    h_min = cv2.getTrackbarPos("Hue min", 'TrackBars')
    h_max = cv2.getTrackbarPos("Hue max", 'TrackBars')
    s_min = cv2.getTrackbarPos("Sat min", 'TrackBars')
    s_max = cv2.getTrackbarPos("Sat max", 'TrackBars')
    v_min = cv2.getTrackbarPos("Val min", 'TrackBars')
    v_max = cv2.getTrackbarPos("Val max", 'TrackBars')
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv_img, lower, upper)
    cv2.imshow("Mask", mask)
    cv2.waitKey(1)


# RED
# Watosci
# Hue min = 15
# Hue max = 255
# Sat min = 114
# Sat max = 255
# Val min = 105
# Val max = 255

# BETTER RED
# Watosci
# Hue min = 156
# Hue max = 177
# Sat min = 131
# Sat max = 255
# Val min = 119
# Val max = 255



# GREEN
# Watosci
# Hue min = 50
# Hue max = 255
# Sat min = 139
# Sat max = 255
# Val min = 74
# Val max = 255

# BETTER GREEN
# Watosci
# Hue min = 55
# Hue max = 80
# Sat min = 32
# Sat max = 255
# Val min = 101
# Val max = 255

# FACE
# Watosci
# Hue min = 0
# Hue max = 12
# Sat min = 31
# Sat max = 255
# Val min = 65
# Val max = 255
