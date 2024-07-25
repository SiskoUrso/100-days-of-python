# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:  #This will check if the number is even by using the modulo operator % to divide the number by 2 and check if the remainder is 0 using the == operator which stands for "is equal to".
  print("This is an even number.") 
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:                #This will then report all other numbers not even being odd by ending the if loop with else
  print("This is an odd number.")
