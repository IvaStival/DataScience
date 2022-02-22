from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Flatten, Dense, BatchNormalization, Dropout

class PlacasNet:

    @staticmethod
    def build(width, height, depth, classes):
        model = Sequential()

        inputShape = (height, width, depth)
        dim = 1

        model.add(Conv2D(8, (5,5), padding = "same", input_shape = inputShape))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=dim))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Conv2D(16, (3,3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=dim))
        model.add(Conv2D(16, (3,3), padding = "same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=dim))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Conv2D(32, (3,3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=dim))
        model.add(Conv2D(32, (3,3), padding = "same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=dim))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Flatten())
        model.add(Dense(128))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))

        model.add(Flatten())
        model.add(Dense(128))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))

        model.add(Dense(classes))
        model.add(Activation("softmax"))

        return model
