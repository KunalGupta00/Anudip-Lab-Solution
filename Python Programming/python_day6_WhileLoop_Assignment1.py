#Q.1)Write a python program to check whether a number is palindrome or not?

# Prompt the user to input a number and convert it to an integer.
# Store the input in the variable 'number'.
number = int(input("Enter a number to check if it's a palindrome: "))

# Create a new variable 'original_number' and set it equal to the input number.
original_number = number

# Initialize the variable 'reversed_number' to 0.
reversed_number = 0

 # Start a while loop. It will continue as long as 'number' is greater than 0.
while number > 0:
    digit = number % 10
    # Extract the last digit of 'number' using the modulo operator (%).
    
    reversed_number = reversed_number * 10 + digit
    # Multiply the current value of 'reversed_number' by 10 and add the extracted digit.
    # This reverses the digits of 'number'.
    
    number //= 10
    #Remove the last digit from 'number' (integer division by 10).
# The loop stops when 'number' becomes 0.

# Compare the original input number with the reversed number.
if original_number == reversed_number :
    print("The Number is Palindrome.")
else :
    print("The Number is not Palindrome.")

"""
when i put 1234 then the output is
OUTPUT : Enter a number to check if it's a palindrome: 1234
The Number is not Palindrome.

when i put 4554 then the output is
OUTPUT : Enter a number to check if it's a palindrome: 4554
The Number is Palindrome.
"""




    
