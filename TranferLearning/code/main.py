from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

from tensorflow.keras.applications.vgg16 import VGG16

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import os
import shutil

# THE IDEA OF THIS CODE IS STUDY THE TRANSFER LEARNING.
# THIS CODE USE A VGG16 IS A PRE TRAINED WITH THE ImageNet DATASET.
# ImageNet HAS OVER 14 MILLIONS IAMGES BELONGING 1000 CLASSES.
# I WILL USE THE PRE TRAINED TO CLASSIFY CATS AND DOGS IMAGES

# REFERENCES
# https://www.kaggle.com/meetnagadia/cats-vs-dogs-classification
# https://medium.com/@1297rohit/transfer-learning-from-scratch-using-keras-339834b153b9


# THIS METHOD IS USED TO CREATE THE DEFAULT FOLDER STRUCTURE OF ImageDataGenerator
# -> new_database
#   |---> train
#       |----> cat
#       |----> dog
#   |---> test
#       |----> cat
#       |----> dog
#   |---> validation
#       |----> cat
#       |----> dog

def createNewData():
    original_dataset_dir = "../dataset/images/train/train"

    base_dir = "../dataset/images/new_database/"

    # CREATE NEW BASE FOLDER new_database
    try:
        os.mkdir(base_dir)
    except:
        pass

    # CREATE train FOLDER
    try:
        train_dir = os.path.join(base_dir, "train")
        os.mkdir(train_dir)
    except:
        pass

    # CREATE validation FOLDER
    try:
        validation_dir = os.path.join(base_dir, "validation")
        os.mkdir(validation_dir)
    except:
        pass

    # CREATE test FOLDER
    try:
        test_dir = os.path.join(base_dir, "test")
        os.mkdir(test_dir)
    except:
        pass

    # CREATE train/cat FOLDER
    try:
        train_cat_dir = os.path.join(train_dir, "cat")
        os.mkdir(train_cat_dir)
    except:
        pass

    # CREATE train/dog FOLDER
    try:
        train_dog_dir = os.path.join(train_dir, "dog")
        os.mkdir(train_dog_dir)
    except:
        pass

    # CREATE validation/cat FOLDER
    try:
        validation_cat_dir = os.path.join(validation_dir, "cat")
        os.mkdir(validation_cat_dir)
    except:
        pass

    # CREATE validation/dog FOLDER
    try:
        validation_dog_dir = os.path.join(validation_dir, "dog")
        os.mkdir(validation_dog_dir)
    except:
        pass

    # CREATE test/cat FOLDER
    try:
        test_cat_dir = os.path.join(test_dir, "cat")
        os.mkdir(test_cat_dir)
    except:
        pass

    # CREATE test/dog FOLDER
    try:
        test_dog_dir = os.path.join(test_dir, "dog")
        os.mkdir(test_dog_dir)
    except:
        pass


    # COPY THE FIRST 999 IMAGES OF CATS TO THE train/cat FOLDER
    file_names = [f"cat.{i}.jpg" for i in range(1000)]

    for file in file_names:
        ori_file = os.path.join(original_dataset_dir, file)
        dest_file = os.path.join(train_cat_dir, file)

        shutil.copyfile(ori_file, dest_file)

    # NOW COPY THE 1000 UNTIL 1499 IMAGES OF CATS TO THE validation/cat FOLDER
    file_names = [f"cat.{i}.jpg" for i in range(1000, 1500)]
    for file in file_names:
        ori_file = os.path.join(original_dataset_dir, file)
        dest_file = os.path.join(validation_cat_dir, file)

        shutil.copyfile(ori_file, dest_file)

    # NOW COPY THE 1500 UNTIL 1999 IMAGES OF CATS TO THE test/cat FOLDER
    file_names = [f"cat.{i}.jpg" for i in range(1500, 2000)]
    for file in file_names:
        ori_file = os.path.join(original_dataset_dir, file)
        dest_file = os.path.join(test_cat_dir, file)

        shutil.copyfile(ori_file, dest_file)

    # COPY THE FIRST 999 IMAGES OF DOGS TO THE train/dog FOLDER
    file_names = [f"dog.{i}.jpg" for i in range(1000)]
    for file in file_names:
        ori_file = os.path.join(original_dataset_dir, file)
        dest_file = os.path.join(train_dog_dir, file)

        shutil.copyfile(ori_file, dest_file)

    # COPY THE 1000 UNITL 1499 IMAGES OF DOGS TO THE validation/dog FOLDER
    file_names = [f"dog.{i}.jpg" for i in range(1000, 1500)]
    for file in file_names:
        ori_file = os.path.join(original_dataset_dir, file)
        dest_file = os.path.join(validation_dog_dir, file)

        shutil.copyfile(ori_file, dest_file)

    # COPY THE 1500 UNITL 1999 IMAGES OF DOGS TO THE test/dog FOLDER
    file_names = [f"dog.{i}.jpg" for i in range(1500, 2000)]
    for file in file_names:
        ori_file = os.path.join(original_dataset_dir, file)
        dest_file = os.path.join(test_dog_dir, file)

        shutil.copyfile(ori_file, dest_file)



def run():
    # HERE ImageDataGenerator IS USED TO LOAD THE DATA CORRECTLY TO USE IN MODEL AND RESIZE THE SIZE OF IMAGES
    # THESE BECAUSE THE VGG16 USE AS INPUT 224 X 224 SIZE
    trdata = ImageDataGenerator()

    # LOAD TRAIN IMAGES
    train_data = trdata.flow_from_directory(directory = "../dataset/images/new_database/train", target_size=(224,224))

    # LOAD VALIDATION IMAGES
    tsdata = ImageDataGenerator()
    test_data = tsdata.flow_from_directory(directory = "../dataset/images/new_database/validation", target_size=(224,224))

    # LOAD VGG16 MODEL AND INCLUDE ALL THE WEIGHTS (include_top = True)
    vggmodel = VGG16(weights = "imagenet", include_top = True)

    vggmodel.summary()

    # SAY TO THE VGG16 MODEL THAT WE NOT WANT THE TRAIN THE FIRST 19 LAYERS
    for layers in (vggmodel.layers)[:19]:
        print(layers)
        layers.trainable = False

    # CHANGE THE LAST LAYER THAT HAS SIZE OF 1000 TO 2 (dog or cat)
    X = vggmodel.layers[-2].output
    predictions = Dense(2, activation = "softmax")(X)

    # CREATE A NEW MODEL WITH THIS NEW SETUP
    model_final = Model(vggmodel.input, predictions)

    # MODEL COMPILE
    model_final.compile(loss = "categorical_crossentropy", optimizer=optimizers.SGD(lr=0.0001, momentum=0.9), metrics=["accuracy"])

    model_final.summary()
     # SET CHECKPOINTS SAVE AND SOTP CONDITIONS
    checkpoint = ModelCheckpoint("../models/vgg16_1.h5", monitor="accuracy", verbose=1, save_best_only=True, save_weights_only=False, mode="auto", period=1)
    early = EarlyStopping(monitor="val_accuracy", min_delta = 0, patience=40, verbose = 1, mode="auto")

    # FIT
    model_final.fit(train_data, steps_per_epoch = 2, epochs=100, validation_data=test_data, validation_steps=1, callbacks=[checkpoint, early])

    # SAVE TRAINNED MODEL
    model_final.save_weights("../models/vgg16_1.h5")

if __name__ == "__main__":
    run()
    # createNewData()
