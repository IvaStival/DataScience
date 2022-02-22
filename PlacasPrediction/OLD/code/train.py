import matplotlib
matplotlib.use("Agg")

from PlacasNet import PlacasNet

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
from skimage import transform
from skimage import exposure
from skimage import io

import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import os

class Train:

    def load_split(self, base_path, csv_file):
        data = []
        labels = []

        rows = open(csv_file).read().strip().split("\n")[1:]
        random.shuffle(rows)

        for (i, row) in enumerate(rows):

            if i > 0 and i % 1000 == 0:
                print(f"[INFO] processed {i} total images. ")

            (label, imagePath) = row.strip().split(',')[-2:]

            imagePath = os.path.sep.join([base_path, imagePath])
            image = io.imread(imagePath)

            image = transform.resize(image, (32, 32))
            image = exposure.equalize_adapthist(image, clip_limit=0.1)

            data.append(image)
            labels.append(int(label))

        data = np.array(data)
        labels = np.array(labels)

        return (data, labels)

    def run(self):

        ap = argparse.ArgumentParser()
        ap.add_argument("-d", "--dataset", required = True, help = "Path to dataset.")
        ap.add_argument("-m", "--model", required = True, help = "Path to model file.")
        ap.add_argument("-p", "--plot", required = True, type = str, default = "plot.png", help = "Path to plot file.")
        args = vars(ap.parse_args())

        NUM_EPOCHS = 30
        INIT_LR = 1e-3
        BS = 64

        label_names = open("../dataset/archive/signnames.csv").read().strip().split("\n")[1:]
        label_names = [l.split(',')[1] for l in label_names]

        train_path = os.path.sep.join([args["dataset"], "Train.csv"])
        test_path = os.path.sep.join([args["dataset"], "Test.csv"])

        print("[INFO] loading training and testing data ...\n")
        (X_Train, Y_Train) = self.load_split(args["dataset"], train_path)
        (X_Test, Y_Test) = self.load_split(args["dataset"], test_path)

        X_Train = X_Train.astype("float32")/255.0
        X_Test  = X_Test.astype("float32")/255.0

        num_labels = len(np.unique(Y_Train))
        lb = np.unique(Y_Train)

        Y_Train = to_categorical(Y_Train, num_labels)
        Y_Test = to_categorical(Y_Test, num_labels)

        class_totals = Y_Train.sum(axis=0)
        class_weight = dict()

        for i in range(0, len(class_totals)):
            class_weight[i] = class_totals.max() / class_totals[i]

        aug = ImageDataGenerator(rotation_range = 10,
                                 zoom_range = 0.15,
                                 width_shift_range = 0.1,
                                 height_shift_range = 0.1,
                                 shear_range = 0.15,
                                 horizontal_flip = False,
                                 vertical_flip = False,
                                 fill_mode = "nearest")
        print("[INFO] compiling model ...\n")

        opt = Adam(learning_rate = INIT_LR, decay = INIT_LR / (NUM_EPOCHS * 0.5))

        model = PlacasNet.build(width = 32, height = 32, depth = 3, classes = num_labels)

        model.compile(loss = "categorical_crossentropy", optimizer = opt, metrics = ["accuracy"])

        print("[INFO] training network ...\n")

        H = model.fit(aug.flow(X_Train, Y_Train, batch_size=BS),
                      validation_data = (X_Test, Y_Test),
                      steps_per_epoch = X_Train.shape[0] // BS,
                      epochs = NUM_EPOCHS,
                      class_weight = class_weight,
                      verbose = 1)

        print("[INFO] evaluating network ...\n")
        predictions = model.predict(X_Test, batch_size = BS)
        print(classification_report(Y_Test.argmax(axis=1), predictions.argmax(axis=1), target_names = label_names))

        model_path = args["model"]
        print(f"[INFO] serialiazing network to {model_path}")
        model.save(args["model"])

        N = np.arange(0, NUM_EPOCHS)
        plt.style.use("ggplot")
        plt.figure()
        plt.plot(N, H.history["loss"], label="train_loss")
        plt.plot(N, H.history["val_loss"], label="val_loss")
        plt.plot(N, H.history["accuracy"], label="train_acc")
        plt.plot(N, H.history["val_accuracy"], label="val_acc")
        plt.title("Training Loss and Accuracy on Database.")
        plt.xlabel("Epoch")
        plt.ylabel("Loss/Accuracy")
        plt.legend(loc="lower left")
        plt.savefig(args["plot"])
