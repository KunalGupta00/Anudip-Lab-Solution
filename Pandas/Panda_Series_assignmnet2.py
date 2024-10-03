#Task 2 : Suppose you want to track and analyze your household expenses for a month.
#You have recorded the expenses for various categories, such as groceries, utilities, rent, transportation, and entertainment.
#You can represent this expense data using a Pandas Series.

# Importing the pandas library, which helps in data manipulation and analysis.
import pandas as pd 

# List of expense categories like groceries, utilities, rent, etc.
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# List of corresponding expenses (in dollars) for each category
expenses = [500, 200, 1200, 300, 150]

# Creating a Pandas Series from the expenses list, using the categories list as the index
# The 'name' parameter gives the Series a meaningful label "Expense categories"
expense_categories = pd.Series(expenses, index=categories, name="Expense categories")

# Print the Series to display the data for the different categories and their corresponding expenses
print(expense_categories)

"""
OUTPUT :
Groceries          500
Utilities            200
Rent                1200
Transportation     300
Entertainment      150
Name: Expense categories, dtype: int64
"""

