import  numpy as np
import  matplotlib.pyplot as plt

x = np.linspace(0,100,10000)
y1 = np.sin(x)
y2 = np.sin(2 * x)
y3 = np.sin(3 * x)
y4 = np.sin(4 * x)
y5 = np.sin(5 * x)
signal = y1 + y2 + y3 + y4 + y5
#plt.plot(x,y1)
plt.plot(x,signal)
plt.show()

