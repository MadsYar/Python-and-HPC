import zarr
import sys
import numpy as np

def mandelbrot_escape_time(c, max_iter=100):
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return max_iter

if __name__ == "__main__":
    n = int(sys.argv[1])
    c = int(sys.argv[2])

    xmin, xmax = -2, 2
    ymin, ymax = -2, 2

    zar = "mandelbrot.zarr"
    mandelbrot_array = zarr.open(zar, mode="w", shape=(n, n), chunks=(c, c), dtype=np.int32)

    val1 = np.linspace(xmin, xmax, n)  # (rows)
    val2 = np.linspace(ymin, ymax, n)  # (columns2)

    for i in range(0, n, c):  
        for j in range(0, n, c): 
            i_end = min(i + c, n)
            j_end = min(j + c, n)

            chunk = np.zeros((i_end - i, j_end - j), dtype=np.int32)
            for ii, x in enumerate(val1[i:i_end]):  
                for jj, y in enumerate(val2[j:j_end]): 
                    chunk[ii, jj] = mandelbrot_escape_time(complex(x, y))

            mandelbrot_array[i:i_end, j:j_end] = chunk