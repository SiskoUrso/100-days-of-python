# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height ** 2

if bmi < 18.5:  # This step will check if the BMI is less than 18.5 and then will print the result, if not it will move onto the next step
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:  # This step will check if the BMI is less than 25 and then will print the result, if not it will move onto the next step
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:  # This step will check if the BMI is less than 30 and then will print the result, if not it will move onto the next step
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:  # This step will check if the BMI is less than 35 and then will print the result, if not it will move onto the next step
  print(f"Your BMI is {bmi}, you are obese.")
else:           # This step will print the result if the BMI is greater than 35 ending the loop with the else statement
  print(f"Your BMI is {bmi}, you are clinically obese.")