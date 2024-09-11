#Q.3) Write a Python program to find duplicate values from a list and display those

# Function to find duplicate values in a list
def find_duplicate(numbers):

    # List to store unique numbers
    seen = []
    # List to store duplicates
    duplicate = []

    # Loop through the list 
    for num in numbers :
        if num in seen and num not in duplicate :
            duplicate.append(num)       # Add to duplicates if already seen
        else:
            seen.append(num)        # Add to seen if it's the first time

    # Return the list of duplicate numbers
    return duplicate

# Example usage
my_list = [4, 7, 9, 4, 3, 7, 1, 9]

 # Call the function
duplicate = find_duplicate(my_list)

# Output the duplicates
print("Duplicate values:", duplicate)

"""
OUTPUT : Duplicate values: [4, 7, 9]
"""
