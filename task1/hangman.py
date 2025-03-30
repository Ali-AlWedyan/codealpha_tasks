import words

def get_word():
    word = words.getWord()
    return word.upper()

def play_hangman():
    word = get_word()
    word_completion = "_ " * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("Let's play Hangman!")
    print(f"You have {tries}!")
    print(word_completion)

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper() 
        print()
        
        # guessing a word, it has to be same lenght
        if len(word) == len(guess) and guess.isalpha():
        
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
        
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
        
            else:
                word_completion = word
                break
        # guessing a letter
        elif guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                changed_index = []
                for i, letter in enumerate(word):
                    if letter == guess:
                        changed_index.append(i)

                for index in changed_index:
                    word_as_list[index*2] = guess
                word_completion = "".join(word_as_list)
            
                if "_" not in word_completion:
                    break
        
        else:
            print("Not a valid guess.")
        
        print(word_completion)
        print(f"\nYou have {tries} tries left!\n")

    if tries > 0:
        print(f"Congrats, you guessed the word {word}! You win!\n")
    
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!\n")



if __name__ == "__main__":
    play_hangman()