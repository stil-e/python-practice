#even_odd_checker.py
#function to check if a number is even or odd

def is_evenor_odd(number):
    #returns even if num is even and odd if num is odd
    
    if number%2==0:
        return "even"
    else:
        return "odd"
    
    #tests
if __name__ == "__main__":
    print(is_evenor_odd(5)) #is odd
    print(is_evenor_odd(35)) #is odd
    print(is_evenor_odd(76)) #is even
