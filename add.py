# Simple Python app: read two numbers and display their sum

def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

def main():
    print("Enter two numbers to compute their sum.")
    a = read_number("First number: ")
    b = read_number("Second number: ")
    total = a + b
    # If both inputs were integers (no fractional part), show as int for nicer output
    if total.is_integer():
        total_display = int(total)
    else:
        total_display = total
    print(f"The sum of {a} and {b} is: {total_display}")

if __name__ == "__main__":
    main()