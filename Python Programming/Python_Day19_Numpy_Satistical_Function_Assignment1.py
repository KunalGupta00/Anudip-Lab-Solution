#Q.1)Compute the median of the flattened NumPy array 

# Importing the NumPy library for numerical operations
import numpy as np

# Input array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Compute the median of the array using the np.median function
# The median is the middle value when the array is sorted
median = np.median(x_odd)

# Output the computed median value
print("Median:", median)

"""
OUTPUT : Median: 4.0
"""
