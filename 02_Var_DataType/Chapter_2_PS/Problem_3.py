# check the type of variable assigned using input

check = input("enter any thing:")

print(type(check))

# this ill give only striong class so updated program Below

user_input = input("Enter Something , like number string or boolean :: ")


# attempt to convert the input to different and check the type

try: 
    int_value = int(user_input)
    print("the type of input is : int")
except ValueError:

    try: 
        float_value = float(user_input)
        print("The type of the input is : float")
    except ValueError:

        if user_input.lower() in ['true','flase']:
           print("The type of the input is: Boolean")
        else:
                 print("The type of the input is: str")

print("============== END ======================")

