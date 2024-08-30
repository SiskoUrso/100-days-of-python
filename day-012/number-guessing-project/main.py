from random import randrange
from art import logo

player_turns = 0
game_on = True

def set_difficulty(difficulty):
    """
    Set the difficulty of the game by setting the number of turns the player has.
    
    Args:
        difficulty (str): The difficulty of the game. Can be "easy" or "hard".
    """
    global player_turns
    if difficulty == "easy":
        player_turns = 10
        print(f"You have {player_turns} attempts remaining to guess the number.")
        return player_turns

    else:
        player_turns = 5
        print(f"You have {player_turns} attempts remaining to guess the number.")
        return player_turns

def game(random_number):
    """
    A game of guessing a random number.

    The player is given a random number between 1 and 100 to guess. The player
    has a limited number of attempts to guess the number correctly. If the
    player guesses correctly, they win. If the player runs out of attempts,
    they lose.

    Parameters
    ----------
    random_number : int
        The number to guess.

    Returns
    -------
    bool
        True if the player wins, False if the player loses.

    """
    global player_turns
    players_guess = int(input("Guess a number between 1 and 100: "))
    if players_guess == random_number:
        print("You got it right, you win!")
        return True
    elif players_guess > random_number:
        print("Too high!")
    elif players_guess < random_number:
        print("Too low!")
    player_turns -= 1
    if player_turns == 0:
        print(f"You lose! The number was {random_number}.")
    else:
        print(f"You have {player_turns} attempts remaining.")
    return False

while game_on:
    print(logo)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    set_difficulty(difficulty)
    random_number = randrange(1, 101)

    while player_turns > 0:
        if game(random_number):
            break

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != 'yes':
        game_on = False


