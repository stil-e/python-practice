# Function to compute sum of digits of a number

def sum_of_digits(number):

    #Returns the sum of digits of the given number.

    number = abs(number)
    total = 0
    while number > 0:
        total= total + number % 10
        number //= 10
    return total

# Tests
if __name__ == "__main__":
    print(sum_of_digits(1234))   # prints 10
    print(sum_of_digits(0))      # prints 0
    print(sum_of_digits(-567))   # prints 18
