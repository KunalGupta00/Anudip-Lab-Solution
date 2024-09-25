#Q.2) Calculate the profit made by a company
"""Input: revenue = np.array([10000, 12000, 11000, 10500]) 
expenses = np.array([4000, 5000, 4500, 4800])"""

# Import the NumPy library
import numpy as np  

# Revenue data for four periods
revenue = np.array([10000, 12000, 11000, 10500])  

# Expense data for the same four periods
expenses = np.array([4000, 5000, 4500, 4800])      

# Calculate profit by subtracting expenses from revenue for each period
profit = revenue - expenses

# Display the profit
print("Profit:", profit)

"""
OUTPUT : Profit: [6000 7000 6500 5700]
"""

