#Q.2)Write a Python script to concatenate the following dictionaries to create a new one. 

# Function to concatenate multiple dictionaries into a new one
def concatenate_dicts(*dicts):  #The * allows us to pass multiple arguments.
    # The *dicts allows us to pass any number of dictionaries as arguments

    # Initialize an empty dictionary to store the final result
    result = {}  
    # Loop through each dictionary provided
    for d in dicts:

        # Update the result with key-value pairs from each dictionary  
        result.update(d)
        
    # Return the concatenated dictionary
    return result  

# Given dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Call the function with the dictionaries
result = concatenate_dicts(dic1, dic2, dic3)
print("Concatenated dictionary:", result)  # Output the concatenated dictionary


"""
OUTPUT : Concatenated dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""




















