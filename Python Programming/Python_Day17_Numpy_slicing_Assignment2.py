# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np

# Create a 1D array with values ranging from 2 to 10
array = np.arange(2, 11)    # np.arange(2, 11): Generates a 1D array with values starting from 2 (inclusive) to 11 (exclusive),

# Reshape the 1D array into a 3x3 matrix
matrix = array.reshape(3, 3)  # array.reshape(3, 3): Reshapes the 1D array into a 3x3 matrix.

# Printing the matrix

print(matrix)


# Output
"""

[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]

 """
