import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1, 2, 3])
v2 = np.array([2, 6, 18])

angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
print(angle)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]])
ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]])

ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_zlim([-6, 6])

plt.savefig('plot_5.png')
