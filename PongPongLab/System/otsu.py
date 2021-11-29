import cv2
import numpy as np
from matplotlib import pyplot as plt

input_img1 = "./Open/t01/5.jpg"

src=cv2.imread(input_img1)

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)
cv2.imshow(input_img1, dst)
cv2.waitKey(0)
cv2.destroyAllWindows()