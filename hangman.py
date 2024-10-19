# Hang man game
import random

def movie():
    movies = ["nila"]
    return random.choice(movies)

def play():
    chance = 8
    word = movie()
    guessed_letters = []  
    word_length = len(word)

    print(f"The selected  word has {word_length} letters")
    
    while chance > 0  :
        
        current_state = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Current word: ", current_state)
        
        if current_state == word:  
            print("You won!")
            return
        
        guess = input("Enter your guess,one letter at a time ").lower()
        
        if len(guess) != 1: 
            print("Please enter only one letter.")

            continue
        if guess.isnumeric ==True:
            print("Please enter alphabets only")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)  
        
        if guess not in word:
            chance -= 1
            print(f"Incorrect guess! You have {chance} chances left.")
        else:
            print("Good guess!")

    print(f"You lost! The word was '{word}'.")

play()