import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

hide_n_num = 5

x_data = np.float32(np.linspace(0, 7, 300))#define the input data
x_data.shape = (300, 1)
y_data = np.sin(x_data)#define the output data

#input and output placeholder
input1 = tf.placeholder(tf.float32, shape=[None, 1])
output1 = tf.placeholder(tf.float32, shape=[None, 1])
#plt.plot(x_data, y_data)
#plt.show()
# define the structure of nn
W1 = tf.Variable(tf.random_uniform([1, hide_n_num], -5.0, 5.0))
b1 = tf.Variable(tf.random_uniform([1, hide_n_num], -5.0, 5.0))
hide1 = tf.sigmoid(tf.matmul(input1, W1) + b1) * 2 - 1

W2 = tf.Variable(tf.random_uniform([hide_n_num, 1], -5.0, 5.0))
b2 = tf.Variable(tf.random_uniform([1], -5.0, 5.0))
y = tf.sigmoid(tf.matmul(hide1, W2) + b2) * 2 - 1

# end define the structure of nn


# calculate the loss of nn
loss = tf.reduce_mean(tf.square(y - output1))
#trainning the nn
#optimizer = tf.train.AdamOptimizer(learning_rate=0.01, beta1=0.5, beta2=0.4, epsilon=1e-8, use_locking=False)()
optimizer = tf.train.AdagradOptimizer(0.9, 0.1, False)
#optimizer = tf.train.MomentumOptimizer(0.5, 0.2, use_locking= False)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
for i in range(2000):
    sess.run(train, feed_dict={input1: x_data, output1: y_data})
    print sess.run(loss, feed_dict={input1: x_data, output1: y_data})

#print sess.run(output1)
#print sess.run(y, feed_dict={input1: x_data})
plt.plot(x_data, y_data)
print sess.run(y, feed_dict={input1: x_data})
plt.plot(x_data, sess.run(y, feed_dict={input1: x_data}))
plt.show()
