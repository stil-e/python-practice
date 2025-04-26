 #Function to compute factorial using a loop

def factorial(n):
    
   # Returns the factorial of a number using a loop.
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Tests
if __name__ == "__main__":
    print(factorial(5))  # will print 120
    print(factorial(0))  # will print 1
    print(factorial(3))  # will print 6
