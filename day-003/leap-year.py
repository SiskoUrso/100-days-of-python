# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0: # This will check if the year is divisible by 4 and uses the modulo operator % to check if the remainder is 0 using the == operator which stands for "is equal to".
    if year % 100 == 0: # This will check if the year is divisible by 100 and uses the modulo operator % to check if the remainder is 0 using the == operator which stands for "is equal to".
        if year % 400 == 0: # This will check if the year is divisible by 400 and uses the modulo operator % to check if the remainder is 0 using the == operator which stands for "is equal to".
            print("Leap year")
        else:   # This will check if the year is not divisible by 400 or 100 and uses the modulo operator % to check if the remainder is 0 using the == operator which stands for "is equal to".
            print("Not leap year")
    else:   # This will check if the year is not divisible by 100 and uses the modulo operator % to check if the remainder is 0 using the == operator which stands for "is equal to".
        print("Leap year")
else:   # This will check if the year is not divisible by 4 and uses the modulo operator % to check if the remainder is 0 using the == operator which stands for "is equal to".
    print("Not leap year")
    