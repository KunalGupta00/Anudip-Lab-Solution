#Q.1)Write a Python program to Get Only unique items from two sets.

# Define two sets with some overlapping and non-overlapping elements
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Use the symmetric difference operator ^ to get only unique items
unique_items = set1 ^ set2

# Output the result
print("Set 1:", set1)
print("Set 2:", set2)
print("Unique items from both sets:", unique_items)

"""
OUTPUT : Set 1: {1, 2, 3, 4, 5}
Set 2: {4, 5, 6, 7, 8}
Unique items from both sets: {1, 2, 3, 6, 7, 8}
"""
