names = names_string.split(", ")

import random

# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
#print(names)
# 🚨 Remember to remove the print statement above when you submit.

num_items = len(names) # this will get the total number of items in the names list

random_choice = random.randint(0, num_items - 1) # this will generate a random number between 0 and the last item in the names list

print(names[random_choice], "is going to buy the meal today!") # this will print the name at the random index in the names list