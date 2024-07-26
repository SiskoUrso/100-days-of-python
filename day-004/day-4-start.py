import random  # importing random module (a module is a collection of functions)

random_integer = random.randint(1, 10) # random integer between 1 and 10
print(random_integer)

random_float = random.random() # Returns the next random floating point number between (0.0 to 0.999999999)
print(random_float)

random_decimal = random.uniform(0, 5) # Returns a random floating point N such that a <= N <= b if a <= b and b <= N <= a if b < a.
print(random_decimal)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


