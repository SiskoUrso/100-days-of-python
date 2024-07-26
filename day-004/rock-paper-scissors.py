rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇 
import random  # this imports the random module

game_images = [rock, paper, scissors]  # this creates a list of game images

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))  # this gets the user's choice and converts it to an integer
if user_choice >= 3 or user_choice < 0:   # this checks if the user's choice is not between 0 and 2
    print("Incorrect number, you lose!")   # this prints if the user's choice is not between 0 and 2
else:
    print(game_images[user_choice])  # this prints the image of the user's choice

    computer_choice = random.randint(0, 2)  # this generates a random number between 0 and 2
    print("Computer chose:")
    print(game_images[computer_choice])  # this prints the image of the computer's choice

    if user_choice == 0 and computer_choice == 2:  # this checks if the user wins
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:  # this checks if the computer wins
        print("You lose")
    elif computer_choice > user_choice:  # this checks if the computer wins
        print("You lose")
    elif user_choice > computer_choice:  # this checks if the user wins
        print("You win!")
    elif computer_choice == user_choice:  # this checks if it's a draw
        print("It's a draw")
