import shutil

import numpy as np
import pandas as pd
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
import keras
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import cv2
from mtcnn.mtcnn import MTCNN
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
# from keras.utils import to_categorical
from tensorflow.keras.utils import to_categorical
from keras.models import Sequential
import tensorflow as tf
from keras.layers import Dense,Conv2D,Flatten,MaxPooling2D,Dropout,Reshape
from keras.models import load_model
import sys
import os
import cv2
import numpy as np  # linear algebra
import cv2 # opencv
import matplotlib.pyplot as plt # image plotting
# keras
from keras import Sequential
from keras.layers import Flatten, Dense
from keras.applications.vgg19 import VGG19
from keras.applications.vgg19 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
# import face_recognition
#
# from keras.utils import plot_model


def train1():
    data = pd.read_csv("train.csv")
    l1 = []
    l2 = []

    for img,ClassId,EncodedPixels in tqdm(data.values):
        image=cv2.imread("train_images/{}".format(img),cv2.IMREAD_COLOR)
        # image=cv2.resize(image,(60,60))
        image = cv2.resize(image, (120 ,120))
        l1.append(image)
        l2.append(ClassId)
    encoder = LabelEncoder()

    x= np.array(l1)
    x= x/255

    encoder = LabelEncoder()
    y = encoder.fit_transform(l2)
    y = to_categorical(y)

    #y=np.array(l2)
    #y=y.reshape(7095,1)

    # x=x.reshape(7095,10800)
    #
    # x=np.hstack((x,y))

    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,shuffle=True)

    # model = Sequential()
    # model.add(Reshape((60, 60, 3), input_shape=(10800,)))
    # model.add(tf.keras.layers.Conv2D(input_shape=(60, 60, 3), filters=16, kernel_size=(3, 3), activation='relu'))
    # model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
    # model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
    # model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
    # model.add(tf.keras.layers.GlobalAveragePooling2D())
    # model.add(tf.keras.layers.Dense(4, activation='softmax'))
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(120, 120, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(4, 4)))
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(256, activation="relu"))
    model.add(Dense(4, activation="softmax"))

    model.summary()

    model.compile(loss=keras.losses.categorical_crossentropy,
                 optimizer=keras.optimizers.Adam(),
                 metrics=["accuracy"])


    early_stopping = tf.keras.callbacks.EarlyStopping(patience=5,min_delta=0.001,restore_best_weights=True)

    history = model.fit(X_train,y_train,epochs=15,validation_data=(X_test,y_test),batch_size=128,
                    verbose=1, callbacks=[early_stopping])

    model.save("WWW.h5")

def test1(filename):
    L1=[]
    model = load_model('WWW.h5')  # 选取自己的.h模型名称
    image=cv2.imread(filename,cv2.IMREAD_COLOR)
    image = cv2.resize(image, (120, 120))
    L1.append(image)
    x = np.array(L1)
    x = x / 255
    y=model(x)
    z=max(y[0])
    L2=[]
    L2.append(y[0][0])
    L2.append(y[0][1])
    L2.append(y[0][2])
    L2.append(y[0][3])
    for inx ,data in enumerate (L2):
        if data==z:
            result=inx


    print(y)
    h="result_lable={}---------------lable0_prediction:{},lable1_prediction:{},lable2_prediction:{},lable3_prediction:{}".format(result,y[0][0],y[0][1],y[0][2],y[0][3])

    return h


def test2(filename):
    mask_det_label = {0: "Mask", 1: "No Mask"}
    mask_det_label_colour = {0: (0, 255, 0), 1: (255, 0, 0)}
    pad_y = 1  # padding for result text

    model = load_model("wface.h5")
    faceCascade = cv2.CascadeClassifier(
        r'./venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    main_img = cv2.imread(filename)
    gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    x = np.array(gray)
    return_faces = faceCascade.detectMultiScale(x)
    print(return_faces)
    for i in range(len(return_faces)):
        L1 = []
        (x, y, w, h) = return_faces[i]
        cropped_face = main_img[y: y + h, x: x + w]
        cropped_face = cv2.resize(cropped_face, (256, 256))
        L1.append(cropped_face)
        kk=np.array(L1)

        mask_result = model(kk)  # make model prediction
        print(mask_result)
        print_label = mask_det_label[arg(mask_result)]  # get mask/no mask based on prediction
        label_colour = mask_det_label_colour[arg(mask_result)]  # green for mask, red for no mask

        # Print result
        (t_w, t_h), _ = cv2.getTextSize(
            print_label, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1
        )  # getting the text size

        cv2.rectangle(
            main_img,
            (x, y + pad_y),
            (x + t_w, y - t_h - pad_y - 6),
            label_colour,
            -1,
        )  # draw rectangle

        cv2.putText(
            main_img,
            print_label,
            (x, y - 6),
            cv2.FONT_HERSHEY_DUPLEX,
            0.4,
            (255, 255, 255),  # white
            1,
        )  # print text

        cv2.rectangle(
            main_img,
            (x, y),
            (x + w, y + h),
            label_colour,
            1,
        )  # draw bounding box on face

    plt.figure(figsize=(10, 10))
    plt.imshow(main_img)  # display image
    cv2.imwrite(  'wudawudawdua.jpg', main_img)
def test3():
    input_dir = './inputimages/images'
    output_dir = './chakan'
    mask_det_label = {0: "Mask", 1: "No Mask"}
    mask_det_label_colour = {0: (0, 255, 0), 1: (255, 0, 0)}
    pad_y = 1  # padding for result text

    model = load_model("wface.h5")
    faceCascade = cv2.CascadeClassifier(
        r'./venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)  # 递归删除一个目录以及目录内的所有内容   # 能删除该文件夹和文件夹下所有文件

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    index = 1
    for (path, dirnames, filenames) in os.walk(input_dir):
        for filename in filenames:
            if filename.endswith('.png'):
                print('Being processed picture %s' % index)
                img_path = path + '/' + filename
                # 从文件读取图片
                main_img = cv2.imread(img_path)
                # 转为灰度图片
                gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
                x = np.array(gray)
                return_faces = faceCascade.detectMultiScale(x)
                print(return_faces)
                for i in range(len(return_faces)):
                    L1 = []
                    (x, y, w, h) = return_faces[i]
                    cropped_face = main_img[y: y + h, x: x + w]
                    cropped_face = cv2.resize(cropped_face, (256, 256))
                    L1.append(cropped_face)
                    kk = np.array(L1)

                    mask_result = model(kk)  # make model prediction
                    print(mask_result)
                    print_label = mask_det_label[arg(mask_result)]  # get mask/no mask based on prediction
                    label_colour = mask_det_label_colour[arg(mask_result)]  # green for mask, red for no mask

                    # Print result
                    (t_w, t_h), _ = cv2.getTextSize(
                        print_label, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1
                    )  # getting the text size

                    cv2.rectangle(
                        main_img,
                        (x, y + pad_y),
                        (x + t_w, y - t_h - pad_y - 6),
                        label_colour,
                        -1,
                    )  # draw rectangle

                    cv2.putText(
                        main_img,
                        print_label,
                        (x, y - 6),
                        cv2.FONT_HERSHEY_DUPLEX,
                        0.4,
                        (255, 255, 255),  # white
                        1,
                    )  # print text

                    cv2.rectangle(
                        main_img,
                        (x, y),
                        (x + w, y + h),
                        label_colour,
                        1,
                    )  # draw bounding box on face

                plt.figure(figsize=(10, 10))
                plt.imshow(main_img)  # display image





                cv2.imwrite(output_dir + '/' + str(index) + '.jpg', main_img)
                index += 1





def face():
    # -*- codeing: utf-8 -*-

    input_dir = './inputimages/images'
    output_dir = './outputimages'
    size = 60  # 指定图像大小
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)  # 递归删除一个目录以及目录内的所有内容   # 能删除该文件夹和文件夹下所有文件

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    faceCascade = cv2.CascadeClassifier(
        r'./venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')

    # 使用dlib自带的frontal_face_detector作为我们的特征提取器
    # detector = dlib.get_frontal_face_detector()

    index = 1
    for (path, dirnames, filenames) in os.walk(input_dir):
        for filename in filenames:
            if filename.endswith('.png'):
                print('Being processed picture %s' % index)
                img_path = path + '/' + filename
                # 从文件读取图片
                image = cv2.imread(img_path)
                # 转为灰度图片
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                x = np.array(gray)
                faces = faceCascade.detectMultiScale(x)
                # 使用detector进行人脸检测 dets为返回的结果
                # dets = face_recognition.api.face_locations(gray_img, 1)

                # 使用enumerate 函数遍历序列中的元素以及它们的下标
                # 下标i即为人脸序号
                # left：人脸左边距离图片左边界的距离 ；right：人脸右边距离图片左边界的距离
                # top：人脸上边距离图片上边界的距离 ；bottom：人脸下边距离图片上边界的距离
                for (x, y, w, h) in (faces):
                    # x
                    # y
                    # x+w
                    # y+h
                    #
                    # x1 = d.top() if d.top() > 0 else 0
                    # y1 = d.bottom() if d.bottom() > 0 else 0
                    # x2 = d.left() if d.left() > 0 else 0
                    # y2 = d.right() if d.right() > 0 else 0
                    # img[y:y+h,x:x+w]
                    face = image[y:y+h, x:x+w]
                    # 调整图片的尺寸
                    # face = cv2.resize(face, (size, size))
                    # cv2.imshow('image', face)
                    # 保存图片
                    cv2.imwrite(output_dir + '/' + str(index) + '.jpg', face)
                    index += 1


def arg(tensor):
    if tensor[0][1] > tensor[0][0]:

        return 1
    else:
        return 0

def train2():
    print("d")

if __name__ == '__main__':
    h=test1("test.jpg")
    print(h)



