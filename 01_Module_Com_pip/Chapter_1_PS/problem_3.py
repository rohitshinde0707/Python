# Q) Write python program to print contents of directory using the OS  module

import os

# Function to print the contents of a directory
def print_directory_contents(path='/'):
    try:
        # List the contents of the directory
        contents = os.listdir(path)
        
        # Print each item in the directory
        for item in contents:
            print(item)
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path (default is current directory)
directory_path = '.'

# Call the function
print_directory_contents(directory_path)
