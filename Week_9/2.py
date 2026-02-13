# 2. CUDA Vector Addition
# Make a cuda kernal add_kernal that takes two vectors x and y as input and returns a new vector a where a_i = x_i + y_i i.e. a is the element-wise sum of x and y:
from numba import cuda
import numpy as np

@cuda.jit
def add_kernel(x, y, out):
    idx = cuda.grid(1)
    if idx < len(x):
        out[idx] = x[idx] + y[idx]
    


# Write a Python program that measures the run time of your kernel with two random vectors. Each input vector should be a NumPy array of length 1,000,000.
# Hint: Run the kernel once before timing so it has been JIT compiled.

def get_bpg(n, tbp):
    return (n+(tpb-1))//tbp

tpb = 512
bpg = get_bpg(len(x), tpb)
x = np.random.rand(1000000)
y = np.random.rand(1000000)
add_kernel[bpg, tpb](x, y)

# Autolab Run your timing program as a batch job so results are repeatable. Use the queue c02613.

