#Q.3)Using max() and min() functions display the maximum and minimum of 5 random numbers

import random

# Generate five random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]
# Each integer is generated using 'random.randint(1, 100)' (inclusive range from 1 to 100).

# Find the maximum and minimum
maximum_number = max(random_numbers)
# 'max(random_numbers)' gives us the largest number in the list.

minimum_number = min(random_numbers)
# 'min(random_numbers)' gives us the smallest number in the list.

print(f"Random numbers: {random_numbers}")
# Display the list of random numbers.
print(f"Maximum: {maximum_number}")
# Display the maximum number.
print(f"Minimum: {minimum_number}")
# Display the minimum number.

"""
OUTPUT : Random numbers: [44, 53, 30, 3, 97]
Maximum: 97
Minimum: 3
"""
