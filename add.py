import sys

def main():
    # If arguments are passed via command line (e.g., in CI or terminal)
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        except ValueError:
            print("Error: Please provide valid numbers.")
            sys.exit(1)
    else:
        # Fallback for manual user input or default CI test values
        print("No command-line arguments provided. Using default values for verification.")
        num1 = 5.0
        num2 = 10.0

    total = num1 + num2
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"The sum is: {total}")

if __name__ == "__main__":
    main()
