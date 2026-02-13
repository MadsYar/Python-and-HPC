import numpy as np
import time
import matplotlib.pyplot as plt

sizes = np.logspace(1, 4.5, num=10, dtype=int)
row_performance = []
column_performance = []
matrix_sizes_kb = []

for SIZE in sizes:
    mat = np.random.rand(1, SIZE)
    matrix_size_kb = mat.nbytes / 1024
    matrix_sizes_kb.append(matrix_size_kb)

    # Measure row doubling performance
    t_row = time.time()
    for _ in range(1000):
        double_row = 2 * mat[0, :]
    t_row = time.time() - t_row
    row_mflops = (SIZE * 1000) / (t_row * 1e6)
    row_performance.append(row_mflops)

    # Measure column doubling performance
    t_column = time.time()
    for _ in range(1000):
        double_column = 2 * mat[:, 0]
    t_column = time.time() - t_column
    column_mflops = (SIZE * 1000) / (t_column * 1e6)
    column_performance.append(column_mflops)

# Plotting the performance
plt.figure(figsize=(10, 6))
plt.loglog(matrix_sizes_kb, row_performance, label='Row Doubling', marker='o')
plt.loglog(matrix_sizes_kb, column_performance, label='Column Doubling', marker='x')
plt.xlabel('Matrix Size (KB)')
plt.ylabel('Performance (MFLOP/s)')
plt.title('Performance of Row and Column Doubling')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('performance_plot.png')

# Plotting the ratio of MFLOP/s
ratio_performance = np.array(row_performance) / np.array(column_performance)
plt.figure(figsize=(10, 6))
plt.loglog(matrix_sizes_kb, ratio_performance, marker='s')
plt.xlabel('Matrix Size (KB)')
plt.ylabel('Ratio of Row to Column Performance (MFLOP/s)')
plt.title('Ratio of Row to Column Doubling Performance')
plt.grid(True, which="both", ls="--")
plt.savefig('ratio_performance_plot.png')