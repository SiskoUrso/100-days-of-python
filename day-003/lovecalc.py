print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = name1 + name2 
lower_names = combined_name.lower()  # this will convert the names to lower case and then count the letters

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
true_total = t + r + u + e # this will count the letters and then add them together

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
love_total = l + o + v + e # this will count the letters and then add them together

love_score = int(str(true_total) + str(love_total)) # this will convert the numbers to strings using the int function and str function and then add them

if (love_score < 10) or (love_score > 90):  # this will check if the score is less than 10 or greater than 90
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):  # this will check if the score is between 40 and 50
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
  
  
# this was the worst exersize that was provided so far in the course, it covered multiple things we have not gone over yet such as the count function, and the lower function. Had to use the solution from the course to pice together to work correctly 