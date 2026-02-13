import sys
import numpy as np
from numba import cuda

TPB = 64  # Threads per block

@cuda.jit
def reduce_kernel(data, out, n):
    sdata = cuda.shared.array(shape=TPB, dtype=np.float32)

    tid = cuda.threadIdx.x
    i = cuda.blockIdx.x * cuda.blockDim.x * 2 + tid

    val = 0.0
    if i < n:
        val = data[i]
        if i + cuda.blockDim.x < n:
            val += data[i + cuda.blockDim.x]
    sdata[tid] = val
    cuda.syncthreads()

    s = cuda.blockDim.x // 2
    while s > 0:
        if tid < s:
            sdata[tid] += sdata[tid + s]
        cuda.syncthreads()
        s //= 2

    if tid == 0:
        out[cuda.blockIdx.x] = sdata[0]

def get_grid(n, tpb):
    return (n + (tpb * 2 - 1)) // (tpb * 2)

def reduce(x):
    n = len(x)

    while n >= TPB * 2: 
        bpg = get_grid(n, TPB)
        out = cuda.device_array(bpg, dtype=np.float32)
        reduce_kernel[bpg, TPB](x, out, n)
        x = out
        n = bpg

    return np.sum(x.copy_to_host())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    n = int(sys.argv[1])
    x = np.random.rand(n).astype(np.float32)
    d_x = cuda.to_device(x)
    total = reduce(d_x)
    print(total)
