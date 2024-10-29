import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([3, -1])
l = 0.3
v1m = v1 * l

plt.plot([0, v1[0]], [0, v1[1]], label = 'v1')
plt.plot([0, v1m[0]], [0, v1m[1]], label = 'lambda v1')
plt.legend()

plt.savefig('plot_3.png')
