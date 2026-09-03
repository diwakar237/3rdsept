import sys

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    if y == 0:
        return "Error: Division by zero!"
    return x / y

if __name__ == "__main__":
    # Test values for the pipeline execution
    num1, num2 = 10, 5
    
    print("=== Python Calculator Automated Test ===")
    print(f"Inputs: num1 = {num1}, num2 = {num2}\n")
    print(f"Addition ({num1} + {num2}): {add(num1, num2)}")
    print(f"Subtraction ({num1} - {num2}): {subtract(num1, num2)}")
    print(f"Multiplication ({num1} * {num2}): {multiply(num1, num2)}")
    print(f"Division ({num1} / {num2}): {divide(num1, num2)}")
    print("=========================================")
