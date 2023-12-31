import tensorflow as tf
import keras
from keras import layers, initializers, optimizers

def classify_trucks():
    # Create sequential model
    initial_model = keras.Sequential(
        [
            layers.Conv2D(16, 3, activation="relu", padding="valid", kernel_initializer=initializers.HeNormal(), input_shape=(224, 224, 3)),
            layers.MaxPooling2D(2),
            layers.Conv2D(32, 3, activation="relu", padding="valid", kernel_initializer=initializers.HeNormal()),
            layers.MaxPooling2D(2),
            layers.Conv2D(64, 3, activation="relu", padding="valid", kernel_initializer=initializers.HeNormal()),
            layers.Flatten(),
            layers.Dense(units=20, activation="relu", kernel_initializer=initializers.HeNormal()),
            layers.Dense(units=1, activation="sigmoid", kernel_initializer=initializers.GlorotNormal())
        ]
    )
    initial_model.compile(optimizer=optimizers.Adam(learning_rate=0.01), loss=keras.losses.BinaryCrossentropy(), metrics=[keras.metrics.BinaryAccuracy()])
    return initial_model

if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
