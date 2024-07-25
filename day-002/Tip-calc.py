#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
print()

bill = float(input("What was the total bill? $")) # this will gather the input from the user and convert it to a float
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) # this will gather the input from the user and convert it to an int
people = int(input("How many people to split the bill? ")) # this will gather the input from the user and convert it to an int
tip_percent = tip / 100 # this will divide the input by 100
total_tip = bill * tip_percent # this will multiply the bill by the tip
total_bill = bill + total_tip # this will add the bill and the tip
bill_per_person = total_bill / people # this will divide the total bill by the number of people
final_amount = round(bill_per_person, 2) # this will round the number to 2 decimal places

print(f"Each person should pay: ${final_amount:.2f}")   # this will print the result using an f-string which will include the variables inside the string as long as they are in curly brackets and .2f will format the number to 2 decimal places.