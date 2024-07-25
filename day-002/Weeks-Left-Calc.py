age = input() # The user will enter their age whcih will be recieved as an string
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

age_int = int(age) # This will convert the string into an integer
target_age = 90 # This will set the target age
years_left = target_age - age_int # This will calculate the years left
weeks_left = years_left * 52 # This will calculate the weeks left

print(f"You have {weeks_left} weeks left.") # This will print the result using an f-string which will include the variables inside the string as long as they are in curly brackets.