line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]  # the first 3 lines are lists
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3] # the map is a list of lists
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()  # this converts the first letter of the position input to lowercase
abc = ["a", "b", "c"]  # this is a list of the letters a, b, and c
letter_index = abc.index(letter)  # this finds the index of the letter in the abc list
number_index = int(position[1]) - 1  # this finds the index of the number in the position input
map[number_index][letter_index] = "X"  # this puts an "X" in the map at the position specified by the user
# Write your code above this row 👆
# 🚨 Don't change the code below 👇 
print(f"{line1}\n{line2}\n{line3}")  # and finally, you print the map using \n to create a new line