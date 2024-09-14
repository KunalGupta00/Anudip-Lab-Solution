#Q.2)Write Python program to Return a set of elements present in Set A or B, but not both.

# Define two sets with some overlapping and non-overlapping elements
set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 60, 70, 80}

# Use the symmetric difference operator ^ to get elements in A or B but not both
unique_elements = set_A ^ set_B

# Output the result
print("Set A:", set_A)
print("Set B:", set_B)
print("Elements in A or B but not both:", unique_elements)

"""
OUTPUT : Set A: {50, 20, 40, 10, 30}
Set B: {80, 70, 40, 60, 30}
Elements in A or B but not both: {80, 50, 20, 70, 10, 60}
"""
