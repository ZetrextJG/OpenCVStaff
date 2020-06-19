import numpy as np
import cv2

def show(name, image):
    transform = False
    for x in image.shape:
        if x > 720:
            transform = True
            break

    if transform:
        resizedImage = cv2.resize(image, (round(image.shape[1] / 2), round(image.shape[0] / 2)))
        cv2.imshow(name, resizedImage)
    else:
        cv2.imshow(name, image)

def calc_distance(p1, p2):
    distance = ( (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2)
    return round(distance)
    


def getMessures(cnt):
    peri = cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
    objCor = len(approx)

    if objCor == 4:
        height = calc_distance(approx[0][0], approx[1][0])
        width = calc_distance(approx[1][0], approx[2][0])
        print(height, width)
        return (height, width, approx)

    else:
        return False


image = cv2.imread("samples/Image.jpg")

figures = []

biggest = (0, 0)


for i in [0, 1]:
    canny = cv2.Canny(cv2.GaussianBlur(image, (7, 7), i), 0, 255)

    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        x = cv2.contourArea(cnt)
        if x > 100:
            figures.append((x, cnt))
            if x > biggest[0]:
                biggest = (x, cnt)

figures.remove(biggest)
cv2.drawContours(image, biggest[1], -1, (255, 0, 0), 3)

result = getMessures(biggest[1])
if result:
    A4_HEIGHT = result[0]
    A4_WIDTH = result[1]

    A4_REL_HEIGTH = 297
    A4_REL_WIDTH = 210

    for element in figures:
        figure = element[1]
        res = getMessures(figure)
        if res:
            obj_height = res[0]
            obj_width = res[1]
            obj_rel_height = round((obj_height / A4_HEIGHT) * A4_REL_HEIGTH, 2)
            obj_rel_width = round((obj_width / A4_WIDTH) * A4_REL_WIDTH, 2)
            points = res[2]
            p1 = tuple(points[0][0])
            p2 = tuple(points[1][0])
            p4 = tuple(points[3][0])

            cv2.arrowedLine(image, p1, p2, (0, 0, 0), thickness=5, tipLength=0.1)
            cv2.putText(image, str(obj_rel_height), (p2[0] - 100, p2[1] - 80), cv2.FONT_HERSHEY_COMPLEX, 1, (217, 37, 214), 3)

            cv2.arrowedLine(image, p1, p4, (0, 0, 0), thickness=5, tipLength=0.1)
            cv2.putText(image, str(obj_rel_width), (p4[0] - 60, p4[1] - 40), cv2.FONT_HERSHEY_COMPLEX, 1, (217, 37, 214), 3)



show("Image", image)


# cv2.imshow("Image", image)
# cv2.imshow("Canny", canny)
cv2.waitKey(0)