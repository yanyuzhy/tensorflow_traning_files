import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


x_data = np.linspace(-10,10,100)
y_data = x_data*x_data - 10

plt.plot(x_data,y_data)
plt.show()
