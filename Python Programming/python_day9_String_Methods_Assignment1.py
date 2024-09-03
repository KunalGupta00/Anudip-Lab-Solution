#Q.1)Write a Python program to Count all letters, digits, and special symbols from the given string.

# Function to count the number of alphabetic characters, digits, and symbols in a string
def count_str (s) :
     # Initialize counters for characters, digits, and symbols
    chars = digits = symbols = 0
    # Loop through each character in the input string
    for char in s :
         # Check if the character is an alphabetic letter (a-z, A-Z)
        if char.isalpha():
            chars += 1    # Increment the character counter
        # Check if the character is a digit (0-9)
        elif char.isdigit():
            digits += 1     # Increment the digit counter
        # If the character is neither a letter nor a digit, it's a symbol
        else:
            symbols += 1    # Increment the symbol counter
    # Return the counts of characters, digits, and symbols
    return chars, digits, symbols

# Input string containing a mix of characters, digits, and symbols
input_str = "P@#yn26at^&i5ve"

# Call the count_str function and unpack the returned values into variables
chars, digits, symbols = count_str(input_str)
# Print the counts of characters, digits, and symbols
print(f" Chars = {chars} Digits = {digits} Symbol = {symbols} ")


"""
OUTPUT :  Chars = 8 Digits = 3 Symbol = 4 
"""
