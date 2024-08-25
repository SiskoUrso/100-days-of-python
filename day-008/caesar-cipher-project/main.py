from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):    # this creates the caesar cipher function which has 3 parameters (original_text, shift_amount, choice)
    output_text = ""                                          # this sets the output_text variable to an empty string which will be used to store the encrypted or decrypted text
    if encode_or_decode == "decode":                         # if the choice is decode, the shift_amount is multiplied by -1 which will shift the letters in the opposite direction
        shift_amount *= -1                                                                  

    for letter in original_text:                                # this loops through each letter in the original_text string

        if letter not in alphabet:                               # if the letter is not in the alphabet list, it is not encoded or decoded and is added to the output_text string
            output_text += letter
        else:                                                    # if the letter is in the alphabet list, it is encoded or decoded and is added to the output_text string
            shifted_position = alphabet.index(letter) + shift_amount           # this finds the index of the letter in the alphabet list and adds the shift_amount to it
            shifted_position %= len(alphabet)                    # this will ensure that the shifted index is within the range of the alphabet list by using the modulus operator that will divide the shifted index by the length of the alphabet list 0-25 and return the remainder
            output_text += alphabet[shifted_position]            # this adds the shifted letter to the output_text string
    print(f"Here is the {encode_or_decode}d result: {output_text}")

continue_or_quit = True

while continue_or_quit:                                       # this loop will continue until the user chooses to quit
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' to continue or 'quit' to end.").lower()
    
    if restart == "quit":
        continue_or_quit = False
        print("Ending")


