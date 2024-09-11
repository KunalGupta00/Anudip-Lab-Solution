#Q.1) Write a Python program and calculate the mean of the below dictionary.

# Function to calculate the mean of dictionary values
def calculate_mean(num):
    # Sum all the values in the dictionary
    total_sum = sum(num.values())
     # Count the number of entries in the dictionary
    num_items = len(num)
     # Calculate the mean by dividing total sum by number of items
    mean_value = total_sum / num_items
     # Return the calculated mean
    return mean_value
# Given dictionary
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
# Call the function with the dictionary
result = calculate_mean(test_dict)
 # Output the result
print("Mean of dictionary values:", result)

"""
OUTPUT : Mean of dictionary values: 6.2
"""
