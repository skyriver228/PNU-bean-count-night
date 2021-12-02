import numpy as np
import cv2

class BeanCount:
    def __init__(self, path: str):
        # Hidden or Open
        self.path = path
        self.image_path_list = self.getImagePath(path)

    def getImagePath(self):
        option = int(input("input number of target"))
        test_l = [f"/t{i:02d}" for i in range(10, 31)]
        image_l = [f"/{i}.jpg" for i in range(1,6)]

        test_path_l = [self.path+i for i in test_l]
        f_l_5 = [i+image_l[4] for i in test_path_l]