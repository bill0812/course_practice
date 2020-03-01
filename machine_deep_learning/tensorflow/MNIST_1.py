# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data
from time import time

mnist = input_data.read_data_sets('../datasets', one_hot = True)
print(mnist.train.num_examples)
print(mnist.validation.num_examples)
print(mnist.test.num_examples)

#print(mnist.train.images[0])
print(mnist.train.images.shape)
print(mnist.train.labels[0])
print(mnist.train.labels.shape)

def plot_image(image):
    plt.imshow(image.reshape(28, 28), cmap = 'binary')
    plt.show()

plot_image(mnist.train.images[0])
print(mnist.train.labels[0])
print(np.argmax(mnist.train.labels[0]))

