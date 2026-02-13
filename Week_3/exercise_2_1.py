import os
import blosc
import numpy as np
import time


def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    os.sync()


def write_blosc(arr, file_name, cname="lz4"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
    os.sync()


def read_numpy(file_name):
    return np.load(f"{file_name}.npy")


def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
    return blosc.unpack_array(b_arr)

def main(size):
    arr = np.zeros((size, size, size), dtype='uint8')

    start_time = time.time()
    write_numpy(arr, "numpy_array")
    numpy_write_time = time.time() - start_time

    start_time = time.time()
    write_blosc(arr, "blosc_array")
    blosc_write_time = time.time() - start_time

    start_time = time.time()
    read_numpy("numpy_array")
    numpy_read_time = time.time() - start_time

    start_time = time.time()
    read_blosc("blosc_array")
    blosc_read_time = time.time() - start_time

    print(f"Write time (numpy): {numpy_write_time:.6f} seconds")
    print(f"Write time (blosc): {blosc_write_time:.6f} seconds")
    print(f"Read time (numpy): {numpy_read_time:.6f} seconds")
    print(f"Read time (blosc): {blosc_read_time:.6f} seconds")


if __name__ == "__main__":
    size = int(sys.argv[1])
    main(size)