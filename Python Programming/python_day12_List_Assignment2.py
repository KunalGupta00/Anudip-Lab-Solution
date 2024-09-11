#Q.2) Write a Python program to get the largest and smallest number from a list without builtin functions.

# Function to find the largest and smallest number in a list
def find_largest_smallest(numbers):

    # Initialize both largest and smallest with the first element of the list
    largest = numbers[0]
    smallest = numbers[0]

    # Loop through the list starting from the second element
    for num in numbers[1:]:
        if num > largest :
            largest = num       # Update largest if a larger number is found
        if num < smallest :
            smallest = num      # Update smallest if a smaller number is found

    # Return both largest and smallest
    return largest, smallest

# Example usage
my_list = [34, 78, 12, 89, 3, 56]

 # Call the function
largest , smallest = find_largest_smallest(my_list)

# Output the largest number
print("The Largest Number is : ", largest)

 # Output the smallest number
print("The Smallest Number is : ", smallest)

"""
OUTPUT : The Largest Number is :  89
The Smallest Number is :  3

"""
