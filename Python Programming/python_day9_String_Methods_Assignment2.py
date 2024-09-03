#Q.2)Write a Python program to remove duplicate characters of a given string.

# Input string that contains duplicate words
input_str = "String and String Function"

# Function to remove duplicate words from a string
def remove_duplictae_words(input_str):

    # Split the input string into a list of words based on spaces
    words = input_str.split()

    # Initialize an empty list to store unique words
    result = []

    # Initialize an empty set to keep track of words that have already been seen
    seen = set()
    
    # Loop through each word in the list of words
    for word in words :

        # Check if the word has not been seen before
        if word not in seen :

            # If the word is unique, add it to the result list
            result.append(word)

            # Add the word to the seen set to mark it as encountered
            seen.add(word)

   # Join the unique words in the result list into a single string, separated by spaces
    return ' '.join(result)

# Call the function to remove duplicate words and store the output
output_str = remove_duplictae_words(input_str)

# Print the original string before removing duplicates
print(f"Before Remove Duplicate Words = {input_str}")

# Print the resulting string after duplicates have been removed
print(f"After Remove Duplicate Words = {output_str}")


"""
OUTPUT : Before Remove Duplicate Words = String and String Function
After Remove Duplicate Words = String and Function
"""


















