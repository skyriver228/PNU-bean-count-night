import sys
import numpy as np
import cv2


input_img1 = "./Open/t25/1.jpg"
src = cv2.imread(input_img1)
#src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
dst = cv2.inRange(src_hsv, (0, 20, 0), (60, 140, 255))

cnt1, _ = cv2.connectedComponents(dst)
dst2 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, None)
cnt2, _ = cv2.connectedComponents(dst2)


cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
