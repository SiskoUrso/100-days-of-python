# Issue reproduced: when dice_num hits 6 it will produce an error as it is out of range of the list which is 0-5

# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])


# Pause 1 exercise was to fix the code so the error happens all the time, changing the random number range to 6-7 will always fail with that error

# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(6, 7)
# print(dice_images[dice_num])


#Pause 2 exercise was to fix the code, changing the range to 0-5 resolve the issue

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
