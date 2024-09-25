#Q.2)Suppose you have two sets of employee data—one containing information about full-time employees and another containing information about part-time employees.
#You want to combine this data to create a comprehensive employee dataset for HR analysis. 

# Import the NumPy library, which is essential for numerical operations in Python
import numpy as np

# Employee data for full-time employees as structured arrays
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000], 
    [103, 'Mike Johnson', 'Full-Time', 52000] 
], dtype = object)

# Employee data for part-time employees as structured arrays
part_time_employees = np.array([ 
     [201, 'Alice Brown', 'Part-Time', 25000], 
     [202, 'Bob Wilson', 'Part-Time', 28000],
     [203, 'Emily Davis', 'Part-Time', 22000]
], dtype = object)

# Combine the two structured arrays using np.concatenate
all_employees = np.concatenate((full_time_employees, part_time_employees))

# Display the combined dataset
print("Combined Employee Dataset:")
print(all_employees)

"""
OUTPUT : Combined Employee Dataset:
[[101 'John Doe' 'Full-Time' 55000]
 [102 'Jane Smith' 'Full-Time' 60000]
 [103 'Mike Johnson' 'Full-Time' 52000]
 [201 'Alice Brown' 'Part-Time' 25000]
 [202 'Bob Wilson' 'Part-Time' 28000]
 [203 'Emily Davis' 'Part-Time' 22000]]
"""




























