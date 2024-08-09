#Step 4

import random
import hangman_art

lives = 6
end_of_game = False
#word_list = ["ardvark", "baboon", "camel"]
#chosen_word = random.choice(word_list)
chosen_word = ""

#choose word from wordlist.txt which is in the same directory as this file
with open('wordlist.txt') as f:
    #For my reference : 
    #with is statement is used to wrap the execution of a block with methods defined by a context manager (an object that defines the runtime context to be established when executing a with statement)
    #If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
    chosen_word = random.choice(f.readlines())
    
word_length = len(chosen_word)


#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter        
                
    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
            print("Incorrect guess")
            lives -= 1                        
            if lives == 0:
                end_of_game = True
                print("You lose.\n")
                
                
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])
    if lives == 0:
        print(f"\nThe word is {chosen_word}")
    print(" ")
