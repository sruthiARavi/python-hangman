#Not a challenge but embellishments based on the recommended solution 
from hangman_art import stages, logo
import random

lives = 6
end_of_game = False
chosen_word = ""
previous_guesses = []

#choose word from wordlist.txt which is in the same directory as this file
with open('wordlist.txt') as f:
    #For my reference : 
    #with is statement is used to wrap the execution of a block with methods defined by a context manager (an object that defines the runtime context to be established when executing a with statement)
    #If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
    #Using strip() function because of extra spaces
    chosen_word = random.choice(f.readlines()).strip()
    
word_length = len(chosen_word)

#print the logo first
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}. Length is {word_length}\n')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f"************* {lives}/6 lives left *************\n")

    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    if guess in previous_guesses:
        print(f"You've already guessed {guess}")
        
    #If guess is not a letter in the chosen_word, then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."  
    elif guess not in chosen_word:        
        print(f"You guessed {guess}. That's not in the word. You lose a life.")
        previous_guesses.append(guess)
        lives -= 1                        
        if lives == 0:
            end_of_game = True
            print("\n********************* YOU LOSE *********************\n")
            
    else:
        previous_guesses.append(guess)
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter        
                                                       
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\n********************* YOU WIN *********************")

    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    if lives == 0:
        print(f"\nThe word is {chosen_word}")
        
    print("\n")
