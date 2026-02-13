import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide numbers as command line arguments.")
        return

    numbers = [int(arg) for arg in sys.argv[1:]]
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(even_numbers)

if __name__ == "__main__":
    main()