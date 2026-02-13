import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
n = int(sys.argv[2])
step = int(sys.argv[3])

array = np.memmap(path, dtype=np.uint8, mode='r', shape=(n, n))

downsampled = array[::step, ::step]

img = Image.fromarray(downsampled)
img.save('downsampled.png')

