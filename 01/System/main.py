import numpy as np
import cv2
import datetime as dt

class BeanCount:
    def __init__(self, export_file_path: str):
        self.test_l = [f"/t{i:02d}" for i in range(1, 31)]
        self.image_l = [f"/{i}.jpg" for i in range(1,6)]
        self.image_path_list = []
        self.count_label_path = "./01/System/count.txt"
        self.start_time = 0
        self.end_time = 0
        self.count_res = []
        self.linear_model_fn = None
        self.export_file_path = export_file_path


    def countingBean(self):
        self.start_time = dt.datetime.now()
        o_image_path_list = self.getImagePath("./Open")
        o_image_pixel_count_list = self.get_above_area(o_image_path_list)
        self.fittingModel(o_image_pixel_count_list, self.count_label_path)
        self.modelResult()
        self.end_time = dt.datetime.now()
        self.exportingOutput()
         

    # path = "./Open" or "./Hidden"
    def getImagePath(self, path):
        image_path_list = []
        option = int(input("input number of target __.jpg(select one from 1,2,3,4,5: "))

        test_path_l = [path+i for i in self.test_l]
        image_path_list.extend([j+self.image_l[option-1] for j in test_path_l])
        return image_path_list


    def get_above_area(image_path_list):
        image_pixel_count_list = []
        for img_path in image_path_list:
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
            image_pixel_count_list.append(sum(sum(fg)))
        return image_pixel_count_list


    def fittingModel(self, x, y):
        f = open(y, 'r')
        line = f.readline()
        count = line.split()
        f.close()
        y = [int(i) for i in count]

        linear_model=np.polyfit(x,y,3)
        self.linear_model_fn=np.poly1d(linear_model)


    def modelResult(self):
        h_image_path_list = self.getImagePath(self, "./Hidden")
        h_image_pixel_count_list = self.get_above_area(h_image_path_list)
        self.count_res = self.linear_model_fn(h_image_pixel_count_list)


    def exportingOutput(self):
        f = open(self.export_file, 'w')
        f.write("Team  PongPongLab\n")

        s_t = self.start_time
        date = "Date  " + f"{s_t.month}-{s_t.day}-{s_t.hour}-{s_t.minute}-{s_t.second}"+"\n"
        f.write(date)
        
        e_t = self.end_time
        diff = s_t - e_t
        t = "Time  "+str(diff.seconds)+"\n"
        f.write(t)

        c = "Cases "+str(len(self.image_path_list))+"\n"
        f.write(c)

        res = self.count_res
        for i in range(len(res)):
            data = res[i]
            f_d = str(self.test_l[i][1:])+"  "+str(round(data,3))+"\n"
            f.write(f_d)
        f.close()

def main():
    bc = BeanCount("./01/Out/Kong_01.txt")
    bc.countingBean()

if __name__ == "__main__":
    main()