import cv2
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

# Training Set

training_generator = ImageDataGenerator(rescale=1. / 255,
                                        rotation_range=7,
                                        horizontal_flip=True,
                                        zoom_range=0.2)

train_set = training_generator.flow_from_directory('Training',
                                                   target_size=(64, 64),
                                                   batch_size=64,
                                                   class_mode='categorical',
                                                   shuffle=True)

# Testing Set

testing_generator = ImageDataGenerator('Testing')

test_set = testing_generator.flow_from_directory('Testing',
                                                 target_size=(64, 64),
                                                 batch_size=1,
                                                 class_mode='categorical',
                                                 shuffle=False)

with tf.device('/device:GPU:0'):
    network_image = Sequential()

    # Adding the 1st conv. layer
    network_image.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 3)))
    network_image.add(MaxPool2D(pool_size=(2, 2)))

    # Adding the 2nd conv. layer
    network_image.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
    network_image.add(MaxPool2D(pool_size=(2, 2)))

    # Adding the 3rd conv. layer
    network_image.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
    network_image.add(MaxPool2D(pool_size=(2, 2)))

    # Adding the 4th conv. layer
    network_image.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
    network_image.add(MaxPool2D(pool_size=(2, 2)))

    network_image.add(Flatten())

    network_image.add(Dense(units=65, activation='relu'))
    network_image.add(Dense(units=65, activation='relu'))
    network_image.add(Dense(units=2, activation='softmax'))

    s = network_image.summary()
    network_image.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    history = network_image.fit(train_set, epochs=50)

result = network_image.predict(test_set)
result = np.argmax(result, axis=1)

# Checking Accuracy

from sklearn.metrics import accuracy_score

print("The Accuracy is:-", accuracy_score(test_set.classes, result))

# Saving And Loading The model

model_json = network_image.to_json()

with open('network_json', 'w') as json_file:
    json_file.write(model_json)

# Saving the model

from keras.models import save_model

saved_model = save_model(network_image, 'weights.hdf5')

# Opening the model

with open('network_json') as json_file:
    json_saved_model = json_file.read()

network_loaded = tf.keras.models.model_from_json(json_saved_model)
network_loaded.load_weights('weights.hdf5')
network_loaded.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])

network_loaded.summary()

# Testing the model

image = cv2.imread('Testing/female/129562.jpg.jpg')
image = cv2.resize(image, (64, 64))

# Normalize the image

image = image / 255
image = image.reshape(-1, 64, 64, 3)

# Final Result
result_new = network_loaded.predict(image)
result_new = np.argmax(result_new)

print(result_new)

if result_new == 0:
    print("Female")
else:
    print("Male")
