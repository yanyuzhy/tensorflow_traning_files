import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x_data = np.float32(np.random.rand(2,100))
y_data = np.dot([0.1, 0.2], x_data) + 0.3

b = tf.Variable(tf.zeros([1]))
w = tf.Variable(tf.random_uniform([1,2], -1.0, 1.0))
y = tf.matmul(w, x_data) + b
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for step in xrange(0,201):
        sess.run(train)
        if 0 == step % 20:
            print step, sess.run(w), sess.run(b)
    sess.close()
