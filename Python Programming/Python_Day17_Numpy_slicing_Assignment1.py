# 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

# Create an array of 10 zeros
zeros_array = np.zeros(10)    # np.zeros(10): Creates an array of ten zeros.

# Create an array of 10 ones
ones_array = np.ones(10)      # np.ones(10): Creates an array of ten ones.

# Create an array of 10 fives
fives_array = np.full(10, 5)  # np.full(10, 5): Creates an array of ten fives by filling an array of size 10 with the value 5

# Printing the arrays
print("Array of 10 zeros:", zeros_array)
print("Array of 10 ones:", ones_array)
print("Array of 10 fives:", fives_array)

#Output
"""
Array of 10 zeros: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Array of 10 ones: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
Array of 10 fives: [5 5 5 5 5 5 5 5 5 5]

"""

