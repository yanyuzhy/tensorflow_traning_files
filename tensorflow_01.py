import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


matrix1 = tf.constant([[3,3]])

matrix2 = tf.constant([[2],[2]])

product = tf.matmul(matrix1,matrix2)


sess = tf.Session()

result = sess.run(product)

sess.close()

print result
