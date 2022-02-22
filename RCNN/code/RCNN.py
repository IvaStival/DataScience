import tensorflow as tf
import tensorflow.keras

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import os
import cv2

class RCNN:
    def __init__(self):
        self.ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

    def get_iou(self, bb1, bb2):
        assert bb1['x1'] < bb1['x2']
        assert bb1['y1'] < bb1['y2']
        assert bb2['x2'] < bb2['x2']
        assert bb2['y1'] < bb2['y2']

        x_left   = max(bb1['x1'], bb2['x1'])
        y_top    = max(bb1['y1'], bb2['y1'])
        x_right  = min(bb1['x2'], bb2['x2'])
        y_bottom = min(bb1['y2'], bb2['y2'])

        if x_right < x-left or y_bottom < y_top:
            return 0.0

        intersection_area = (x_right - x_left) * (y_bottom - y_top)

        bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
        bb2_area = (bb1['x2'] - bb2['x2']) * (bb2['y2'] - bb2['y1'])

        iou - intersection_area / float(bb1_area + bb2_area - intersection_area)

        assert iou >= 0.0
        assert iou <= 1.0
        return iou

    def run(self):

        train_images = []
        train_labels = []

        path = "../dataset/Images"
        csv_path = "../dataset/Airplanes_Annotations"

        for e, i in enumerate(os.listdir(path)):
            try:
                if i.startswith("airplane"):
                    csv_filename = i.split('.')[0] + ".csv"
                    print(f"{e} {i}")

                    image = cv2.imread(os.path.join(path, i))
                    df = pd.read_csv(os.path.join(csv_path, csv_filename))

                    gtvalues = []

                    for row in df.iterrows():
                        x1 = int(row[1][0].split(" ")[0])
                        y1 = int(row[1][0].split(" ")[1])
                        x2 = int(row[1][0].split(" ")[2])
                        y2 = int(row[1][0].split(" ")[3])
                        gtvalues.append({"x1":x1, "x2":x2, "y1":y1, "y2":y2})

                    self.ss.setBaseImage(image)
                    self.ss.switchToSelectiveSearchFast()
                    ssresults = ss.process()
                    imout = image.copy()

                    counter = 0
                    false_counter = 0
                    flag = 0
                    fflag = 0
                    bflag = 0

                    for e, result in enumarate(ssresults):
                        if e < 2000 and flag == 0:
                            for gtval in gtvalues:
                                x, y, w, h = result

                                iou = self.get_iou(gtval, {"x1":x, "x2":x+w, "y1":y, "y2":y+h})

                                if counter < 30:
                                    if iou > 0.70:
                                        timage = imout[y:y+h, x:x+w]
                                        resized = cv2.resize(timage, (224, 224), interpolation = cv2.INTER_AREA)
                                        train_images.append(resized)
                                        train_labels.append(1)
                                        counter += 1
                                else:
                                    fflag = 1
                                if false_counter < 30:
                                    if iou < 0.3:
                                        timage = imout[y:y+h, x:x+w]
                                        resized = cv2.resize(timeage, (224, 224), interpolation = cv2.INTER_AREA)
                                        train_images.append(resized)
                                        train_labels.append(0)
                                        false_counter += 1
                                else:
                                    bflag = 1
                            if fflag == 1 and bflag == 1:
                                print("inside")
                                flag = 1
                    break

            except Exception as e:
                print(e)
                print("Error")
                continue
