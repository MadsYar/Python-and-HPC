import multiprocessing
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100

def worker(chunk):
    return [mandelbrot_escape_time(c) for c in chunk]

def generate_mandelbrot_set_chunks(x, y):
    chunksize = len(x) // y
    if chunksize <= y:
        chunksize = y + 1
    with multiprocessing.Pool(processes=y) as pool:
        results = pool.map(mandelbrot_escape_time, x, chunksize=chunksize)

    # Convert the list of results to a NumPy array
    escape_times = np.array(results)
    return escape_times

def plot_mandelbrot(escape_times, width, height):
    escape_times = escape_times.reshape((height, width))
    plt.imshow(escape_times, cmap='hot', extent=(-2, 2, -2, 2))
    plt.axis('off')
    plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)

if __name__ == "__main__":
    width = 800
    height = 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    y = 4

    # Precompute x and y values
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)

    # Compute Mandelbrot set with chunk parallelism
    mandelbrot_set = generate_mandelbrot_set_chunks(x_values, y)

    # Save set as image
    plot_mandelbrot(mandelbrot_set, width, height)
