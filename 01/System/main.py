import numpy as np
import cv2

class BeanCount:
    def __init__(self, path: str):
        # Hidden or Open
        self.path = path
        self.image_path_list = []

    def getImagePath(self):
        option = [int(i) for i in input("input number of target __.jpg(if you want './Open/t01/5.jpg' ~ './Open/t30/3.jpg', input: 1 2 3)").split()]
        test_l = [f"/t{i:02d}" for i in range(1, 31)]
        image_l = [f"/{i}.jpg" for i in range(1,6)]

        test_path_l = [self.path+i for i in test_l]
        for i in option:
            self.image_path_list.extend([i+image_l[i-1] for i in test_path_l])