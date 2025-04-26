# Function to reverse a string without using slicing

def reverse_string(s):
    
    #it reverses the given string without using slicing.
    
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Tests
if __name__ == "__main__":
    print(reverse_string("hello"))    # Will print olleh
    print(reverse_string("Python"))   # will print nohtyP
    print(reverse_string(""))         # will print (empty string)
