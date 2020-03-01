# coding: utf-8

import tensorflow as tf
import numpy as np


a = tf.placeholder(tf.int32 , shape=(1,3))
b = tf.constant(3)

print(a)
print(b)

c = tf.placeholder(tf.int32 , shape=(1,3))
d = tf.constant(2)

multiply = tf.multiply(a,b)
div = tf.div(c,d)

output = tf.add(multiply,div)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={
        a: np.matrix([3,6,9]) , c: np.matrix([2,4,6])
    }))
    print(sess.run(multiply,feed_dict={
        a: np.matrix([3,6,9])
    }))

def g1():
    g1 = tf.Graph()
    
    with g1.as_default() as g:
        a = tf.placeholder(tf.int32 , shape=(1,3))
        b = tf.constant(3)
        c = tf.placeholder(tf.int32 , shape=(1,3))
        d = tf.constant(2)
        multiply = tf.multiply(a,b)
        div = tf.div(c,d)
        output = tf.add(multiply,div)
        with tf.Session() as sess:
            return sess.run(output,feed_dict={
                a: np.matrix([3,6,9]) , c: np.matrix([2,4,6])
            })
tmp = g1()
print(tmp)

