# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

random_number = random.randint(0, 1) # this uses the randint function to generate a random number between 0 and 1 which is then stored in the random_number variable.


if random_number == 1: # this checks if the random_number is equal to 1.
  print("Heads")
else:                  # this checks if the random_number is not equal to 1.
  print("Tails")