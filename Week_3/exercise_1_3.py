import numpy as np
import time

sizes = np.logspace(1, 4.5, num=10, dtype=int)

for SIZE in sizes:
    mat = np.random.rand(1, SIZE)

    t = time.time()
    for _ in range(1000):
        double_column = 2 * mat[:, 0]
        double_row = 2 * mat[0, :]

    t = time.time() - t

    print(f"SIZE: {SIZE}, Time: {t}")