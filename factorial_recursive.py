#factorial_recursive.py
# Function to compute factorial using recursion

def factorial_recursive(n):

    #Returns the factorial of a number using recursion.
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Tests
if __name__ == "__main__":
    print(factorial_recursive(5))  # prints 120
    print(factorial_recursive(3))  # prints 6
    print(factorial_recursive(0))  # prints 1
