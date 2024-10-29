import numpy as np

m = 4
n = 6

A = np.random.randn(m, n)
B = np.random.randn(m, n)

print(A)
print(B)

dps = np.zeros(n)
for i in range(n):
    dps[i] = np.dot(A[:, i], B[:, i])

print(dps)
