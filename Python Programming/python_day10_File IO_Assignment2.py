#Q.2)Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(filename):
    """
    Counts and displays the total number of words in a text file.

    Parameters:
        filename (str): The name of the file to count words from.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire file content
            words = content.split()  # Split the content into words
            total_words = len(words)  # Count the number of words
            print(f"Total number of words in '{filename}': {total_words}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.") # Handle case where file does not exist
    except Exception as e:
        print(f"An error occurred: {e}")    # Handle other exceptions

# Call the function to count words in "ABC.txt"
count_words_in_file("ABC.txt")


"""
OUTPUT : Total number of words in 'ABC.txt': 23
"""
