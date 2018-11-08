import tensorflow as tf
import numpy as np
import pandas as pd

DATASET_PATH = "/Users/HsnFirooz/Downloads/1/"

def load_dataset():
    data = pd.read_csv(DATASET_PATH + "x_train.txt", sep=',', header=None).values
    label = pd.read_csv(DATASET_PATH + "y_train.txt", sep=',', header=None).values
    x_train, y_train = _normalize_data(data, label)

    data = pd.read_csv(DATASET_PATH + "x_test.txt", sep=',', header=None).values
    label = pd.read_csv(DATASET_PATH + "y_test.txt", sep=',', header=None).values
    x_test, y_test = _normalize_data(data, label)

    y_train = _convert_to_one_hot(y_train)
    y_test = _convert_to_one_hot(y_test)

    return x_train, y_train, x_test, y_test

def _normalize_data(data, label):
    return data / 1000.0, label - 1

def _convert_to_one_hot(labels):
    with tf.Session() as sess:
        one_hot = tf.one_hot(labels, 3)
        labels = sess.run(one_hot)
        return np.reshape(labels, (-1, 3))