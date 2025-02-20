import re

def find_digits():
    # Input string
    input_string = input("Enter a sequence of words: ")

    # Use re.findall() to find all substrings that are digits
    digits_only = re.findall(r'\b\d+\b', input_string)

    # Print the result
    print(digits_only)

# Call the function
find_digits()
