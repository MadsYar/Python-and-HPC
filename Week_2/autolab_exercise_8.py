import sys
import numpy as np

def main():
    if len(sys.argv) < 2:
        print("Please provide numerical grades as command line arguments.")
        return

    grades = [float(arg) for arg in sys.argv[1:]]
    mean_grade = np.mean(grades)
    result = "Pass" if mean_grade >= 5 else "Fail"
    print(f"{mean_grade} {result}")

if __name__ == "__main__":
    main()
