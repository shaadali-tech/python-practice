# Factorial Program

# Method 1: Using recursion
def factorial_recursive(n):
    """Calculate factorial using recursion"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Method 2: Using iteration
def factorial_iterative(n):
    """Calculate factorial using iteration"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Method 3: Using math module
import math

def factorial_math(n):
    """Calculate factorial using built-in math module"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    return math.factorial(n)


# Main program
if __name__ == "__main__":
    # Test the functions
    test_number = 5
    
    print(f"Factorial of {test_number}:")
    print(f"Recursive method: {factorial_recursive(test_number)}")
    print(f"Iterative method: {factorial_iterative(test_number)}")
    print(f"Math module: {factorial_math(test_number)}")
    
    # Interactive input
    print("\n--- Interactive Factorial Calculator ---")
    try:
        num = int(input("Enter a number to calculate factorial: "))
        print(f"{num}! = {factorial_iterative(num)}")
    except ValueError:
        print("Please enter a valid integer.")
