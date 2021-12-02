import numpy as np
import cv2
import time
import datetime as dt

class BeanCount:
    def __init__(self, path: str):
        # Hidden or Open
        self.path = path
        self.image_path_list = []
        self.

    def getImagePath(self):
        option = [int(i) for i in input("input number of target __.jpg(if you want './Open/t01/5.jpg' ~ './Open/t30/3.jpg', input: 1 2 3)").split()]
        test_l = [f"/t{i:02d}" for i in range(1, 31)]
        image_l = [f"/{i}.jpg" for i in range(1,6)]

        test_path_l = [self.path+i for i in test_l]
        for i in option:
            self.image_path_list.extend([j+image_l[i-1] for j in test_path_l])

    def get_above_area(img_path, res_l):
        src=cv2.imread(img_path)
        rc = (975, 909, 2555, 999)
        src = src[rc[1]:rc[1]+rc[3], rc[0]:rc[0]+rc[2]]
        dst = src
        src_hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

            # dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
        dst1 = cv2.inRange(src_hsv, (16, 13, 0), (80, 250, 255))
        dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)

        kernel = np.ones((6, 6), np.uint8)
        closing = cv2.morphologyEx(dst2, cv2.MORPH_CLOSE,kernel, iterations = 15)
        bg = cv2.dilate(closing, kernel, iterations = 1)
        dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
        ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)
        res_l.append(sum(sum(fg)))

    def fittingModel(self, x, y):
        x = res_l_5
        y = [int(i) for i in count]

        linear_model=np.polyfit(x,y,3)
        linear_model_fn=np.poly1d(linear_model)

        return linear_model_fn

    def exportingOutput():
        f = open("./01/Out/Kong_01.txt", 'w')
        f.write("Team  PongPongLab\n")
        date = "Date  " + f"{d.month}-{d.day}-{d.hour}-{d.minute}-{d.second}"+"\n"
        f.write(date)
        t = "Time  "+str(round(time.time() - start,2))+"\n"
        f.write(t)
        c = "Cases "+str(len(res_l_5))+"\n"
        f.write(c)
        for i in range(len(y_new)):
            data = y_new[i]
            f_d = str(f2_l[i][1:])+"  "+str(round(data,3))+"\n"
            f.write(f_d)
        f.close()