# Using try and excpet to fix the errors, if the user enters a string it will not work
#broken code

# age = int(input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")

# Fixed code


try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")