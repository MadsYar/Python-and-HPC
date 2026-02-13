import sys
import numpy as np

def main():
    
    diagonal_elements = [float(arg) for arg in sys.argv[1:]]
    
    matrix = np.diag(diagonal_elements)
    
    np.save('matrix.npy', matrix)
    print(f"Matrix saved to 'matrix.npy'")

if __name__ == "__main__":
    main()