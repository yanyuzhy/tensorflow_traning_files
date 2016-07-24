import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

intermed = tf.add(input1,input2)
mul = tf.mul(input3,intermed)

with tf.Session() as sess:
    result = sess.run([mul,intermed])
    print result
