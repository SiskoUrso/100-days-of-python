import random
from hangman_words import word_list  # imports the word list variable which contains a list of words from the hangman_words.py file
from hangman_art import logo, stages # imports the logo and stages variables from the hangman_art.py file

lives = 6   # sets the number of lives to 6

print(logo)           # prints the logo which is from a variable in the hangman_art.py file
chosen_word = random.choice(word_list)  # chooses a random word from the word list using the random module

placeholder = ""   # this will be used to display the word to guess
word_length = len(chosen_word)   # gets the length of the chosen word
for position in range(word_length):  # creates a placeholder with the length of the chosen word
    placeholder += "_"                # adds an underscore to the placeholder
print("Word to guess: " + placeholder)         # prints the placeholder

game_over = False    # sets the game over variable to false
correct_letters = []   # sets the correct letters variable to an empty list

while not game_over:   # starts a while loop to determine if game over is true

    
    print(f"You have {lives} lives left")
    guess = input("Guess a letter: ").lower()   # gets the user input and converts it to lowercase
    
    display = ""    # sets the display variable to an empty string

    if guess in correct_letters:      # checks if the guess is in the correct letters list
        print(f"The letter {guess} has already been guessed")

    for letter in chosen_word:        # checks if the guess is in the chosen word
        if letter == guess:
            display += letter          # if the guess is in the chosen word, it is added to the display string
            correct_letters.append(guess)    # if the guess is in the chosen word, it is added to the correct letters list 
        elif letter in correct_letters:       # if the guess is in the correct letters list, it is added to the display string
            display += letter
        else:
            display += "_"                   # if the guess is not in the chosen word or in the correct letters list it ads an underscore to the display string

    print("Word to guess: " + display)
    
    if guess not in chosen_word:            # checks if the guess is not in the chosen word and subtracts one from the lives variable
        lives -= 1
        print(f"You guessed {guess}, that is not in the word, one life down")

        if lives == 0:                      # checks if the lives variable is equal to 0 if it is, it sets the game over variable to true and prints you loose
            game_over = True            
            print(f"You loose, the correct word was {chosen_word}")

    if "_" not in display:                  # checks if there is anymore underscores in the display string and if there is not, it sets the game over variable to true and prints you win
        game_over = True
        print("****************************YOU WIN****************************")

    
    print(stages[lives])                    # prints the stages based on the lives variable which is from the hangman_art.py file
