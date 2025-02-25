# -*- coding: utf-8 -*-
"""cnn_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13L9tNzEgQSyE5Z0_R64A2kb9j1moYHZm
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install keras

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten, BatchNormalization
from keras.regularizers import l2
from keras.optimizers import Adam
from keras.callbacks import ReduceLROnPlateau, EarlyStopping
from keras.models import load_model

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

X_train.shape

y_train.shape

y_train = y_train.reshape(-1,)
y_train[:5]

#creating a list for classes
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

classes[8]

def plot_sample(X, y, index) :
  plt.figure(figsize=(15,2))
  plt.imshow(X[index])
  plt.xlabel(classes[y[index]])

plot_sample(X_train, y_train, 0)

plot_sample(X_train, y_train, 8)

#nornalise the data
X_train = X_train / 255
x_test = X_test / 255

print(X_train[0])

# Define CNN model
cnn = models.Sequential([
    layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(32,32,3)),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

cnn.fit(X_train, y_train, epochs=10)

cnn.evaluate(X_test, y_test)

