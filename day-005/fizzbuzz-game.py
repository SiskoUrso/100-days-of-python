# The goal of this excersize was to create a FizzBuzz game in Python
# The rules are as follows:
# If the number is divisible by 3, print "Fizz"
# If the number is divisible by 5, print "Buzz"
# If the number is divisible by 3 and 5, print "FizzBuzz"
# Otherwise, print the number

for number in range(1,101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
# or

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)