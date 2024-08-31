def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? Looping through a range of numbers 1-20
# 2. When is the function meant to print "You got it"? once i is equal to 20
# 3. What are your assumptions about the value of i? i is a range from 1-20 but since range will not include 20 it will not print "You got it"

#fixed
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()