#Q.2)Write a python program finding the factorial of a given number using a while loop

# Prompt the user to input a number and convert it to an integer.
# Store the input in the variable 'number'.
number = int(input("Enter the number to find factorial : "))

# Initialize the variable 'factorial' to 1.
factorial = 1

# Create a new variable 'n' and set it equal to the input number.
n = number

while n > 0 :
     # Start a while loop. It will continue as long as 'n' is greater than 0.
     
    factorial *= n
    # Multiply the current value of 'factorial' by 'n' and update 'factorial'.

    n -= 1
    # Decrement 'n' by 1 in each iteration of the loop.
    # The loop stops when 'n' becomes 0.

print(f"Factorial of {number} is : ", factorial)

"""
OUTPUT : Enter the number to find factorial: 5
Factorial of 5 is: 120

"""
