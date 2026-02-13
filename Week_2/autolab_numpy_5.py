import numpy as np
import time
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit(1)  # Ensure correct argument usage

    npy_path = sys.argv[1]
    p = int(sys.argv[2])

    if p <= 0:
        sys.exit(1)  # Ensure p is strictly positive

    A = np.load(npy_path)  # Load matrix from file

    start_time = time.perf_counter()  # Start timing
    result = np.linalg.matrix_power(A, p + 1)  # Compute A^(p+1)
    elapsed_time = time.perf_counter() - start_time  # Stop timing

    np.save("result.npy", result)  # Save the result

    print(f"{elapsed_time:.6f}")  # Print only the time in seconds

if __name__ == "__main__":
    main()
