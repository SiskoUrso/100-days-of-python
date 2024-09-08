import random
import game_data
from art import logo, vs

random_choice1 = random.choice(game_data.data)
random_choice2 = random.choice(game_data.data)
choice_A = random_choice1["name"], random_choice1["description"], random_choice1["country"], random_choice1["follower_count"]
choice_B = random_choice2["name"], random_choice2["description"], random_choice2["country"], random_choice2["follower_count"]

while random_choice1 == random_choice2:
    random_choice2 = random.choice(game_data.data)

score = 0

def compare(choice_A, choice_B):
    """
    Compares two choices and returns "a" if choice A has more followers
    and "b" if choice B has more followers.
    """
    if choice_A[3] > choice_B[3]:
        return "a"
    else:
        return "b"

def game(choice_A, choice_B, score):
    """
    Runs the game of Higher or Lower.

    The game starts with two random choices. The user is asked to guess which
    choice has more followers. The user is given a score based on how many
    choices they guess correctly in a row. The game continues until the user
    guesses incorrectly. The user is then asked if they want to play again.

    Args:
        choice_A (tuple): The first choice.
        choice_B (tuple): The second choice.
        score (int): The current score.

    Returns:
        None
    """
    game_on = True
    while game_on:
        print(logo)
        print(f"Compare A: {choice_A[0]}, {choice_A[1]}, from {choice_A[2]}.")
        print(vs)
        print(f"Against B: {choice_B[0]}, {choice_B[1]}, from {choice_B[2]}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_choice == compare(choice_A, choice_B):
            score += 1
            print(f"You're right! Current score: {score}.")
            choice_A = choice_B
            random_choice2 = random.choice(game_data.data)
            while random_choice2["name"] == choice_A[0]:
                random_choice2 = random.choice(game_data.data)
            choice_B = random_choice2["name"], random_choice2["description"], random_choice2["country"], random_choice2["follower_count"]
        else:
            print(f"Sorry that's wrong. Final score: {score}.")
            continue_game = input("Would you like to play again? Type 'y' or 'n': ").lower()
            if continue_game == "y":
                score = 0
                random_choice1 = random.choice(game_data.data)
                random_choice2 = random.choice(game_data.data)
                while random_choice1 == random_choice2:
                    random_choice2 = random.choice(game_data.data)
                choice_A = random_choice1["name"], random_choice1["description"], random_choice1["country"], random_choice1["follower_count"]
                choice_B = random_choice2["name"], random_choice2["description"], random_choice2["country"], random_choice2["follower_count"]
            elif continue_game == "n":
                game_on = False

game(choice_A, choice_B, score)
