import numpy as np
import time

SIZE = 100

mat = np.random.rand(SIZE, SIZE)

t = time.time()
for _ in range(1000):
    double_column = 2 * mat[:, 0]
    double_row = 2 * mat[0, :]

t = time.time() - t

print("Time: ", t)