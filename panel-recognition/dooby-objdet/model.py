import cv2
import numpy as np
# import tensorflow as tf
# import matplotlib.pyplot as plt
import os
import joblib


my_model_path = os.path.join(os.getcwd(), "model.h5")
config_path = os.path.join(
    os.getcwd(), 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
weights_path = os.path.join(os.getcwd(), 'frozen_inference_graph.pb')
coco_names = os.path.join(os.getcwd(), "coco.names")


def detect_traffic_light(img):

    traffic_class = 0
    tl_classes = ["None", "RED", "GREEN", "YELLOW"]

    font = cv2.FONT_HERSHEY_SIMPLEX
    cimg = img
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # color range
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([90, 255, 255])
    # lower_yellow = np.array([15,100,100])
    # upper_yellow = np.array([35,255,255])
    lower_yellow = np.array([15, 150, 150])
    upper_yellow = np.array([35, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    maskg = cv2.inRange(hsv, lower_green, upper_green)
    masky = cv2.inRange(hsv, lower_yellow, upper_yellow)
    maskr = cv2.add(mask1, mask2)

    size = img.shape
    # print size

    # hough circle detect
    r_circles = cv2.HoughCircles(maskr, cv2.HOUGH_GRADIENT, 1, 80,
                                 param1=50, param2=10, minRadius=0, maxRadius=30)

    g_circles = cv2.HoughCircles(maskg, cv2.HOUGH_GRADIENT, 1, 60,
                                 param1=50, param2=10, minRadius=0, maxRadius=30)

    y_circles = cv2.HoughCircles(masky, cv2.HOUGH_GRADIENT, 1, 30,
                                 param1=50, param2=5, minRadius=0, maxRadius=30)

    # traffic light detect
    r = 5
    bound = 4.0 / 10
    if r_circles is not None:
        r_circles = np.uint16(np.around(r_circles))

        for i in r_circles[0, :]:
            if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound:
                continue

            h, s = 0.0, 0.0
            for m in range(-r, r):
                for n in range(-r, r):

                    if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                        continue
                    h += maskr[i[1]+m, i[0]+n]
                    s += 1
            if h / s > 50:
                cv2.circle(cimg, (i[0], i[1]), i[2]+10, (0, 255, 0), 2)
                cv2.circle(maskr, (i[0], i[1]), i[2]+30, (255, 255, 255), 2)
                cv2.putText(cimg, 'RED', (i[0], i[1]),
                            font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        traffic_class = 1
        return traffic_class, maskg, maskr, masky

    if g_circles is not None:
        g_circles = np.uint16(np.around(g_circles))

        for i in g_circles[0, :]:
            if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound:
                continue

            h, s = 0.0, 0.0
            for m in range(-r, r):
                for n in range(-r, r):

                    if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                        continue
                    h += maskg[i[1]+m, i[0]+n]
                    s += 1
            if h / s > 100:
                cv2.circle(cimg, (i[0], i[1]), i[2]+10, (0, 255, 0), 2)
                cv2.circle(maskg, (i[0], i[1]), i[2]+30, (255, 255, 255), 2)
                cv2.putText(cimg, 'GREEN',
                            (i[0], i[1]), font, 1, (255, 0, 0), 3, cv2.LINE_AA)
        traffic_class = 2
        return traffic_class, maskg, maskr, masky

    if y_circles is not None:
        y_circles = np.uint16(np.around(y_circles))

        for i in y_circles[0, :]:
            if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound:
                continue

            h, s = 0.0, 0.0
            for m in range(-r, r):
                for n in range(-r, r):

                    if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                        continue
                    h += masky[i[1]+m, i[0]+n]
                    s += 1
            if h / s > 50:
                cv2.circle(cimg, (i[0], i[1]), i[2]+10, (0, 255, 0), 2)
                cv2.circle(masky, (i[0], i[1]), i[2]+30, (255, 255, 255), 2)
                cv2.putText(cimg, 'YELLOW',
                            (i[0], i[1]), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        traffic_class = 3
        return  traffic_class


with open(coco_names, "r") as f:
    class_names = f.readlines()
    for i in range(len(class_names)):
        class_names[i] = class_names[i].strip('\n\t ')

net = cv2.dnn_DetectionModel(weights_path, config_path)
img_height = 180
img_width = 180
net.setInputSize(img_height, img_width)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))

net.setInputSwapRB(True)

# model = tf.keras.models.load_model(my_model_path)
# with joblib
model = joblib.load("model.pkl")


def ssd_mobile_net(img):
    class_ids, confs, bbox = net.detect(img, confThreshold=0.5)
    if len(class_ids) > 0:
        # Model predicted a value
        # print(class_names[class_ids[0]-1])
        return class_names[class_ids[0]-1]
    return None


class_to_name = {
    0: "stop sign",
    1: "no turn sign",
    2: "no parking sign",
    3: "roundabout sign",
    4: "80 speed limit",
    5: "40 speed limit"
}


def predict(img):
    # First use ssd_mobile_net model
    class_name = ssd_mobile_net(img)
    if class_name == None:
        # Run our model
        resized = cv2.resize(img, (img_height, img_width),
                             interpolation=cv2.INTER_AREA)
        # print(resized.shape)
        reshaped = resized.reshape((1, img_height, img_width, 3))
        class_id = np.argmax(model.predict(reshaped))
        print(class_id)
        #return class_to_name[class_id]
    # elif class_name == 'traffic light':
    #     # Detect traffic light color
    #     color = detect_traffic_light(img)
    #     # print(color)
    #     return class_name, color
    # elif class_name == "stop sign":
    #     # process stop sign
    #     # print(class_name)
    #     return class_name
    # elif class_name == "street sign":
    #     # Process street sign
    #     # print(class_name)
    #     return class_name
    # elif class_name == "roundabout":
    #     # Process roundabout
    #     # print(class_name)
    #     return class_name
    # else:
        return class_name
