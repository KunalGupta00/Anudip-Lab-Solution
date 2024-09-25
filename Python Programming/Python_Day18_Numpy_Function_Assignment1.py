#Q.1)Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions.
#Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

# Import the NumPy library, which is essential for numerical operations in Python
import numpy as np

# Define a NumPy array named 'temperatures' containing daily temperature readings
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])

# Use np.where to find indices where temperatures exceed 35°C (Hot Days)
# np.where returns a tuple of arrays, one for each dimension
hot_day_indices = np.where(temperatures > 35)

# Use np.where to find indices where temperatures below 5°C (Cold Days)
cold_day_indices = np.where(temperatures < 5)

# Print header for Hot Days
print("Hot Days :")
print("Day  Temperature  (C)")

# Iterate over the array of hot day indices
for index in hot_day_indices[0]:
    # Print day number (index + 1) and corresponding temperature with one decimal place
    print(f"{index+1}        {temperatures[index]:.1f}")

# Print header for Cold Days
print("Cold Days :")
print("Day  Temperature  (C)")

# Iterate over the array of cold day indices
for index in cold_day_indices[0]:
     # Print day number (index + 1) and corresponding temperature with one decimal place
    print(f"{index+1}       {temperatures[index]:.1f}")


"""
OUTPUT : Hot Days :
Day  Temperature  (C)
3        36.8
6        38.7
10        37.2
Cold Days :
Day  Temperature  (C)
11       -4.0
12       -12.0
"""








    
