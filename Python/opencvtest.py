import sys
import numpy as np
import cv2 as cv

print(cv.__version__)

# img = cv.imread("./birb.jpg")
# img = cv.imread("./birb.jpg", cv.IMREAD_GRAYSCALE)
""" img = cv.imread("./birb.jpg", cv.IMREAD_REDUCED_COLOR_2)

if img is None:
    sys.exit("Could not read the image")

cv.imshow("Display window", img)
k = cv.waitKey(0)  # wait for user input. -> terminate display.

if k == ord("s"):
    cv.imwrite("birb.png", img)  # save the file as birb.png
 """

unitSize = 75
numberOfUnit = 8
imgSize = unitSize * numberOfUnit

img = np.zeros((imgSize, imgSize, 3), np.uint8)

# cv.rectangle(img, (100, 0), (200, 100), (0, 255, 0), -1)
for i in range(numberOfUnit):
    for j in range(numberOfUnit):
        if (i+j) % 2 == 0:
            cv.rectangle(img, (i*unitSize, j*unitSize),
                         ((i+1)*unitSize, (j+1)*unitSize), (255, 255, 255), -1)

cv.imshow("Chessboard", img)
k = cv.waitKey(0)
