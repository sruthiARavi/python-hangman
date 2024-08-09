from hangman_art import stages, logo
from hangman_words import word_list
import random

lives = 6
end_of_game = False
previous_guesses = []
chosen_word = random.choice(word_list) 
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
            
    elif guess not in chosen_word:        
        print(f"You guessed {guess}. That's not in the word. You lose a life.")
        previous_guesses.append(guess)
      
        #If guess is not a letter in the chosen_word, then reduce 'lives' by 1.   
        lives -= 1 

        #If lives goes down to 0 then the game should stop       
        if lives == 0:
            end_of_game = True
            print(f"\n********************* IT WAS {chosen_word}! YOU LOSE *********************\n")
            
    else:
        previous_guesses.append(guess)
      
        for position in range(word_length):
            letter = chosen_word[position]
          
            # Testing code 
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          
            if letter == guess:
                display[position] = letter        
                                                       
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if the user got all letters.
    if "_" not in display:
        end_of_game = True
        print("********************* YOU WIN *********************")

    #Printing the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])    
    print("\n")
