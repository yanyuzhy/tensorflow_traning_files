import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

state = tf.Variable([[0,0]],name="counter")
one = tf.constant([[1,1]])

w = tf.Variable(tf.random_normal([20,30], mean=0.0, dtype = tf.float32),name = 'w')


newvalue = tf.add(state,one)
update = tf.assign(state,newvalue)

init_op = tf.initialize_all_variables()


sess = tf.Session()
sess.run(init_op)
print sess.run(state)
print sess.run(w)

for _ in range(3):
    sess.run(update)
    print sess.run(state)


sess.close()
