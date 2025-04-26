# function to sum all elements in a list

def sum_of_list (numbers):
    """ 
    takes a list of numbers and returns their sum. 
    """
    total = 0
    for num in numbers:
        total+=num

    return total
    
    #tests
if __name__ == "__main__":
        print(sum_of_list([1,2,3,4,5,6]))
        #should print 21 which is the sum of the numbers
        print(sum_of_list([20,-2,3])) #should print 21
        print(sum_of_list([])) #should print 0