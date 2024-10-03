#Task 1 :  Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject.
#You have recorded the scores of your students for a recent exam, and you want to represent this data using a Pandas Series.

# Import the pandas library, which is used for data manipulation and analysis.
import pandas as pd  

# List of student names
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']

# List of exam scores corresponding to the students
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Create a Pandas Series using the exam_scores list with the students list as the index
# The 'name' parameter is used to label the Series, making it easier to identify.
mid_result_series = pd.Series(exam_scores, index=students, name="Exam Results")

# Print the created Series to display the data
print(mid_result_series)

"""
OUTPUT :
Alice          92
Bob           88
Charlie      76
David        94
Eve           82
Frank       90
Grace       85
Hannah   89
Ivy           78
Jack         91
Name: Exam Results, dtype: int64
"""
