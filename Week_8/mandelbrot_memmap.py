import numpy as np
import sys

def mandelbrot_escape_time(c, max_iter=100):
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return max_iter

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mandelbrot_memmap.py <n>")
        sys.exit(1)

    n = int(sys.argv[1])

    xmin, xmax = -2, 2
    ymin, ymax = -2, 2

    mmap_file = "mandelbrot_array.dat"
    mandelbrot_array = np.memmap(mmap_file, dtype=np.int32, mode="w+", shape=(n, n))

    real_values = np.linspace(xmin, xmax, n)
    imag_values = np.linspace(ymin, ymax, n)

    for i, y in enumerate(imag_values): 
        for j, x in enumerate(real_values): 
            mandelbrot_array[j, i] = mandelbrot_escape_time(complex(x, y)) 

    mandelbrot_array.flush()
