#Q.2)Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# Define a function to get an integer from the user
def get_integer():  
    try:
        # Prompt the user to enter an integer and convert it to an integer type
        number = int(input("Enter an integer: "))  
        
        # If input is valid, print the entered integer
        print(f"Valid integer entered: {number}")
    
    except ValueError:  # Catch ValueError if input is not a valid integer
        # Display an error message for invalid input
        print("Error: Input is not a valid integer.")

# Call the function to execute the integer input check
get_integer()

"""

When i entered a both string or numeric value the output is given below,
OUTPUT : Enter an integer: Kun123
Error: Input is not a valid integer.

When i entered a only numeric value the output is given below
OUTPUT : Enter an integer: 9
Valid integer entered: 9

"""
