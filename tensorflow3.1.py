import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
#tf.random_normal()
weights = tf.Variable(tf.random_normal([784,200], mean=0.0, stddev = 0.35, dtype=tf.float32),name='weights')
biases = tf.Variable(tf.zeros([200]), name="biases")

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    result = sess.run(init_op)
    print sess.run(weights)
    sess.close()
