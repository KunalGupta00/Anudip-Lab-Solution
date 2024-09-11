#Q.1)Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers():  # Define a function to handle division
    try:
        # Prompt the user to enter the numerator and convert it to a floating-point number
        numerator = float(input("Enter the numerator: "))  
        
        # Prompt the user to enter the denominator and convert it to a floating-point number
        denominator = float(input("Enter the denominator: "))  
        
        # Perform the division operation
        result = numerator / denominator
        
        # If no error occurs, print the result of the division
        print(f"The result is: {result}")
    
    except ZeroDivisionError:  # Catch ZeroDivisionError if the denominator is zero
        # Display an error message if division by zero occurs
        print("Error: Cannot divide by zero.")

# Call the function to execute the division
divide_numbers()

"""

When i run a program 1st time the output is given below,
OUTPUT : Enter the numerator: 30
Enter the denominator: 0
Error: Cannot divide by zero.

When i run a program 2nd time the output is given below,
OUTPUT : Enter the numerator: 11
Enter the denominator: 2
The result is: 5.5

"""
