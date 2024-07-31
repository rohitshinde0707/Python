# this function allows  the user to take input
# from user keyboard as a string


name = input("Entr Your Name::")


# it is important to note that the output of input
# is always a string ( Even if the number is entered )

# to convert input <str> in to <int>

num1 = int(input("Enter A Number:"))
num2 = int(input("Enter A second Number:"))

total = num1+num2

print("Total of num1 and Num2 is:", total)

# string in to decimal 
decimal = float(input("Enter decimal number:"))

print(decimal)

print("-----------------------------------------------")
# some more example of input >>>>>>>>>>>>>

# Convert user input to an integer
int_value = int(input("Enter an integer: "))
print("The Type of int_value is ::", type(int_value))

# Convert user input to a float
float_value = float(input("Enter a float: "))
print("The Type of float_value is ::", type(float_value))

# Convert user input to a list (comma-separated values)
list_value = input("Enter comma-separated values: ").split(',')
print("The Type of list_value is ::", type(list_value))

# Convert user input to a set (comma-separated values)
set_value = set(input("Enter comma-separated values: ").split(','))
print("The Type of set_value is ::", type(set_value))

# Convert user input to a boolean
bool_value = input("Enter True or False: ").lower() == 'true'
print("The Type of bool_value is ::", type(bool_value))

print("========== end ===================")
