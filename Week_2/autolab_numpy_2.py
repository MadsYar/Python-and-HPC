import sys
import numpy as np

def magnitude(vector):
    return np.linalg.norm(vector)

def main():
    vector = np.array([float(arg) for arg in sys.argv[1:]])
    print(magnitude(vector))

if __name__ == "__main__":
    main()