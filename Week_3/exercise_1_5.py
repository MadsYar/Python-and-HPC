import numpy as np
import time
import matplotlib.pyplot as plt

sizes = np.logspace(2, 8, num=10, dtype=int)
row_performance = []
matrix_sizes_kb = []

for SIZE in sizes:
    mat = np.random.rand(1, SIZE)
    matrix_size_kb = mat.nbytes / 1024
    matrix_sizes_kb.append(matrix_size_kb)

    # Measure row doubling performance
    t_row = time.time()
    for _ in range(100):
        double_row = 2 * mat[0, :]
    t_row = time.time() - t_row
    row_mflops = (SIZE * 100) / (t_row * 1e6)
    row_performance.append(row_mflops)

# Plotting the performance
plt.figure(figsize=(10, 6))
plt.loglog(matrix_sizes_kb, row_performance, label='Row Doubling', marker='o')
plt.xlabel('Matrix Size (KB)')
plt.ylabel('Performance (MFLOP/s)')
plt.title('Performance of Row Doubling')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('row_performance_plot.png')

# Print the performance values
for size, performance in zip(matrix_sizes_kb, row_performance):
    print(f"Matrix Size: {size} KB, Performance: {performance} MFLOP/s")