import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

#data
fashion_mnist = keras.datasets.fashion_mnist
# train and test
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

#classes
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# evaluating to [0,1]
train_images = train_images/255.0
test_images = test_images/255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # input layer (1) each pixel will be associated with one neuron
    keras.layers.Dense(128, activation='relu'),  # hidden layer (2) 128 is a random number...  Dense - this layer will be fully connected and each neuron from the previous layer connects to each neuron of this layer
    keras.layers.Dense(10,activation='softmax') # output layer (3) 10 because we have 10 classes - so 10 outputs... Softmax - neurons will have a value between 0 and 1
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#train... epochs - how many times will the model see the data. More epochs != more accuracy
model.fit(train_images, train_labels, epochs=10)



test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=1)


print('Test accuracy:', test_acc)