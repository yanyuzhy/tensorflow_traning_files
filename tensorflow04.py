import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

input1 = tf.placeholder(tf.float32)

input2 = tf.placeholder(tf.float32)
output = tf.mul(input1,input2)

with tf.Session() as sess:
    result = sess.run([output],feed_dict={input1:[7.0],input2:[2.0]})
    print result
