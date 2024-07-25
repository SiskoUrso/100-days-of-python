# using /n can be used to make a new line
print("What Have I Learned\n", "-------------------\n", "1. Functions\n", "2. Variables\n", "3. Comments\n")
print()
print("Enter two words: ")
# Here we are using the input function to get user input and assigning it to the variable, adding the /n will make a new line for the cursor in the terminal
a = input("Word 1\n")
b = input("Word 2\n")
# Here we are using the print function to print the variables, and using concatenation to combine the variables, the " " will add a space between the variables
print(a + " " + b)
# len(name) will provide the length of the string in the variable name
print("What is your name? ")
name = input("Enter your name: \n")
print("There is",len(name),"numbers in your name.")