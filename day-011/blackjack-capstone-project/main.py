import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_wins = 0
computer_wins = 0
game_on = True

def check_for_blackjack(player_cards, computer_cards):
    player_has_blackjack = 10 in player_cards and 11 in player_cards
    computer_has_blackjack = 10 in computer_cards and 11 in computer_cards
    if player_has_blackjack and computer_has_blackjack:
        print("Both players have Blackjack. It's a tie!")
        print(f"Your score: {sum(player_cards)} | Computer's score: {sum(computer_cards)}")
        return "draw"
    elif player_has_blackjack:
        print("You have Blackjack! You win!")
        print(f"Your score: {sum(player_cards)} | Computer's score: {sum(computer_cards)}")
        return "player"
    elif computer_has_blackjack:
        print("Computer has Blackjack! You lose!")
        print(f"Your score: {sum(player_cards)} | Computer's score: {sum(computer_cards)}")
        return "computer"

    return None

def adjust_for_aces(cards):
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

def player_turn(player_cards):
    while sum(player_cards) < 21:
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == "y":
            player_cards.append(random.choice(cards))
            adjust_for_aces(player_cards)
        else:
            return sum(player_cards)
    return sum(player_cards)

def computer_turn(computer_cards):
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        adjust_for_aces(computer_cards)
    return sum(computer_cards)

def display_results(player_cards, computer_cards, player_score, computer_score):
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if player_score > 21:
        print("You went over. You lose!")
        return "computer"
    elif computer_score > 21:
        print("Computer went over. You win!")
        return "player"
    elif player_score > computer_score:
        print("You are the winner!")
        return "player"
    elif computer_score > player_score:
        print("You lose!")
        return "computer"
    elif player_score == computer_score:
        print("It's a tie!")
        return "draw"

while game_on:
    play_choice = input("Would you like to play Blackjack? Type 'y' or 'n': ").lower()
    print("\n" * 20)
    print(logo)
    if play_choice == "y":
        player_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 2)

        blackjack_status = check_for_blackjack(player_cards, computer_cards)
        if blackjack_status:
            if blackjack_status == "player":
                player_wins += 1
            elif blackjack_status == "computer":
                computer_wins += 1
            continue

        player_score = player_turn(player_cards)
        if player_score <= 21:
            computer_score = computer_turn(computer_cards)
        else:
            computer_score = sum(computer_cards)

        result = display_results(player_cards, computer_cards, player_score, computer_score)
        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1

    else:
        game_on = False

print(f"Final scores - Player: {player_wins}, Computer: {computer_wins}")