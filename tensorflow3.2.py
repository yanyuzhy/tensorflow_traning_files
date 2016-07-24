import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
#tf.random_normal()
weights = tf.Variable(tf.random_normal([2,2], mean=0.0, stddev = 0.35, dtype=tf.float32),name='weights')

w2 = tf.Variable(weights.initialized_value(), name="w2")

w_twice = tf.Variable(weights.initialized_value()*2,name="w_twice")

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    result = sess.run(init_op)
    print sess.run(weights)
    print sess.run(w2)
    print sess.run(w_twice)

    sess.close()
