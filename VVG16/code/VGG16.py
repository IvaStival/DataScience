import tensorflow.keras, os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import zipfile

'''Most unique thing about VGG16 is that instead of having a large number of hyper-parameter
they focused on having convolution layers of 3x3 filter with a stride 1 and always used same
padding and maxpool layer of 2x2 filter of stride 2. It follows this arrangement of convolution
and max pool layers consistently throughout the whole architecture. In the end it has
2 FC(fully connected layers) followed by a softmax for output. The 16 in VGG16 refers to it has
16 layers that have weights. This network is a pretty large network and it has about
138 million (approx) parameters.'''

class VGG16:
    def __init__(self, unzip=False):
        self.path = os.getcwd().split("code")[0]
        self.dataset_name = "dogs-vs-cats"

        self.unzip = unzip
    def unzipDataSet(self,zipfile_name, directory):
        with zipfile.ZipFile(f"{self.path}/dataset/{self.dataset_name}/{zipfile_name}", "r") as z:
            z.extractall(f"{self.path}/dataset/images/{directory}")

    def createDataFrameFromDirectory(self, directory):
        list_of_files = [os.path.join(f"{self.path}/dataset/images/{directory}", file) for file in os.listdir(f"{self.path}/dataset/images/{directory}")]

        df = pd.DataFrame({"Path" : list_of_files})
        df["animal"] = np.where(df["Path"].str.contains("dog"), "dog", "cat")

        return df



    def setModel(self):
        model = Sequential()

        model.add(Conv2D(input_shape = (224,224, 3), filters=64, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(Conv2D(filters=64, kernel_size=(3,3), padding="same", activation="relu"))

        model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))

        model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))

        model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))

        model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))

        model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))

        model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))

        model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))

        model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))

        model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))

        model.add(Flatten())
        model.add(Dense(units=4096, activation="relu"))
        model.add(Dense(units=4096, activation="relu"))
        model.add(Dense(units=2, activation="softmax"))

        return model

    def run(self):
        if self.unzip:
            self.unzipDataSet("train.zip", "train")
            self.unzipDataSet("test1.zip", "test")

        df_train = self.createDataFrameFromDirectory("train/train")
        df_test = self.createDataFrameFromDirectory("test/test1")

        X_Train, X_Test = train_test_split(df_train, test_size=0.3)

        print(X_Train.shape)

        tr_datagen = ImageDataGenerator(rescale = 1./255,
                                        shear_range = 0.2,
                                        zoom_range = 0.2,
                                        rotation_range=40,
                                        width_shift_range=0.2,
                                        height_shift_range=0.2,
                                        horizontal_flip=True,
                                        fill_mode='nearest')

        ts_datagen = ImageDataGenerator(rescale = 1./255)

        train_set = tr_datagen.flow_from_dataframe(dataframe=X_Train, x_col="Path", y_col="animal", class_mode="categorical", target_size=(224,224), batch_size=128)
        test_set  = ts_datagen.flow_from_dataframe(dataframe=X_Test,  x_col="Path", y_col="animal", class_mode="categorical", target_size=(224,224), batch_size=128)

        opt = Adam(lr=0.001)
        model = self.setModel()

        model.compile(optimizer = opt, loss=categorical_crossentropy, metrics=["accuracy"])

        model.summary()

        checkpoint = ModelCheckpoint(f"{self.path}/models/vgg16_1.h5", monitor="accuracy", verbose=1, save_best_only=True, save_weights_only=False, mode="auto", save_freq=1)
        early = EarlyStopping(monitor="val_accuracy", min_delta=0, patience=20, verbose=1, mode="auto")

        hist = model.fit_generator(steps_per_epoch=100, generator=train_set, validation_data=test_set, validation_steps=10, epochs=10, callbacks=[checkpoint, early])
