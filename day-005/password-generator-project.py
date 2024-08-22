# The project was to create a random password generator with a hard and easy option to compelte. The lists and the input settings were hard coded for the project.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Method
#password = " "  # this will create an empty string
#for char in range(0, nr_letters):   # this will loop through the letters and add them to the password
#    password += random.choice(letters)  # this will choose a random letter from the letters list and add it to the password
#for char in range(0, nr_symbols):
#    password += random.choice(symbols)  # this will choose a random symbol from the symbols list and add it to the password
#for char in range(0, nr_numbers):
#    password += random.choice(numbers)  # this will choose a random number from the numbers list and add it to the password
#print(password)

password_list = []   # this will create an empty list
for char in range(0, nr_letters):   # this will loop through the letters and add them to the password
    password_list.append(random.choice(letters))   # this will choose a random letter from the letters list and add it to the password
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))   # this will choose a random symbol from the symbols list and add it to the password
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))   # this will choose a random number from the numbers list and add it to the password
print(password_list)  # this will print the password list
random.shuffle(password_list)  # this will shuffle the password list
print(password_list)  # this will print the shuffled password list

password = " "  # this will create an empty string
for char in password_list:  # this will loop through the password list and add them to the password
    password += char  # this will add the character to the password

print(f"Your password is: {password}")  