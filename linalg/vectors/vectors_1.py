import numpy as np
import matplotlib.pyplot as plt

# 2-dimensional vector
v2 = [3, -2]

# 3-dimensional vector
v3 = [4, -3, 2]

# transpose a vector
v3t = np.transpose(v3)

# a 2-d vector
v1 = np.array([3, -1])

# plot a vector
plt.plot([0, v1[0]], [0, v1[1]])

# save the plot as an image
plt.savefig("plot_1.png")
