#Q.1)Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file_line_by_line(filename):
    """
    Reads the content of a text file line by line and displays it on the screen.
    Parameters:
        filename (str): The name of the file to read.
    """
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                print(line.strip())  # Print each line after removing leading/trailing whitespace
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")  # Handle case where file does not exist
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle other exceptions

# Call the function to read and display content from "ABC.txt"
read_file_line_by_line("ABC.txt")


"""
OUTPUT : Hello, Good Afternoon.
My name is Kunal SureshKumar Gupta. and now i am doing a course of Data Analytics from a Anudip Foundation.
"""














