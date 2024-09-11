#Q.1) Write a Python program to sum all the items in a list.

# Function to calculate the sum of all items in a list
def sum_of_list(numbers):
    total = 0       # Initialize total sum to 0

    # Loop through each number in the list
    for num in numbers :
        total += num        # Add each number to the total
    return total             # Return the final sum

# Example usage
my_list = [2, 4, 6, 8, 10]
result = sum_of_list(my_list)        # Call the function with the list
print("Sum of all the items in the list : ", result)            # Output the result


"""
OUTPUT : Sum of all the items in the list :  30
"""
