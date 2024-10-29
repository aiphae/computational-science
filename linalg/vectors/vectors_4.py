import numpy as np

v1 = np.array([1, 2, 3, 4, 5, 6])
v2 = np.array([0, -4, -3, 6, 5, 1])

# sum of element wise multiplication
dp1 = sum(np.multiply(v1, v2))

# almost the same methods
dp2 = np.dot(v1, v2) # preferred for dot product
dp3 = np.matmul(v1, v2) # preferred for matrix multiplication

# iterative approach
dp4 = 0
for i in range(0, len(v1)):
    dp4 = dp4 + v1[i] * v2[i]

print(dp1, dp2, dp3, dp4)
