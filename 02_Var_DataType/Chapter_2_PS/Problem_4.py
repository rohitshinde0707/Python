
# Q| Use comparison operator to findout whether a given variable 
# or you can take 2 number from user and print greater number

# This program compares two numbers entered by the user and prints the greater number

# Take the first number as input from the user and convert it to an integer
num_1 = int(input("Enter First Number::"))

# Take the second number as input from the user and convert it to an integer
num_2 = int(input("Enter Second Number::"))

# Compare the two numbers
if num_1 > num_2:
    # If the first number is greater, print the first number
    print("Greater number is:", num_1)
else:
    # If the second number is greater or equal, print the second number
    print("Greater number is:", num_2)
