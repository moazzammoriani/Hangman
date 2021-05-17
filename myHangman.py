import random, string


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    file = open("../words.txt", "r")
    wordlist = file.readline().split()
    return(wordlist)

def choose_word(wordList):
    """
    Takes in a list of words and then randomly picks one word.
    """
    return(random.choice(wordList)) 







def is_word_guessed(secret_word, letters_guessed):

    '''
    Takes in a word and a list of letters and returns True
    if the all the letters in the list are in the word.
    '''
    secret_word = secret_word.lower()
    isIn = True

    for l in secret_word:
        if l not in letters_guessed:
            isIn = False

    return(isIn)



def get_guessed_word(secret_word, letters_guessed):
    '''
    Takes in a word and list of letters that have been guessed and returns a string displaying
    the letters guessed in the structure of the word.
    '''
    word_guessed = ""

    for l in secret_word:
        if l in letters_guessed:
            word_guessed += l
        else:
            word_guessed += '_ '

    return(word_guessed)




def get_available_letters(letters_guessed):
    '''Takes in a list of letters and returns a string of all the lowercase
       letters that aren't in the list
    '''
    available_letters = ""

    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter


    return(available_letters)


print("\n \n \n \n \n \n \n \nWelcome to the game of Hangman! We will brutally hang a man until\n" 
    + "you can guess the word I randomly thought of. Sounds exciting, right?\n \n"
    + "A word has been randomly selected so you may begin your guessing!\n \n \n \n \n")

#theWord = choose_word(load_words());
theWord = "orange"
wrongGuesses = 0;
guessedLetters = [];

while wrongGuesses < 6 and not is_word_guessed(theWord, guessedLetters):
    guess = ""
    if wrongGuesses == 0:
        print("    ___________", "           Your available letters are: ", get_available_letters(guessedLetters) + "\n")
        print("    )         |", "           " + "Here's your progress so far: ", get_guessed_word(theWord, guessedLetters))
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("              |") 
        guess = input("         ___________       Please guess a letter: \n \n \n")
        guess = guess.lower()
        print("------------------------------------------------------------------- \n \n \n") 
        
        guessedLetters.append(guess)

        
    elif wrongGuesses == 1:
            
        print("    ___________", "           Your available letters are: ", get_available_letters(guessedLetters) + "\n")
        print("    )         |", "           " + "Here's your progress so far: ", get_guessed_word(theWord, guessedLetters))
        print("    o         |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        guess = input("         ___________       Please guess a letter: \n \n \n")
        print("------------------------------------------------------------------- \n \n \n")

        
        guess = guess.lower()

        guessedLetters.append(guess)
        

    elif wrongGuesses == 2:
        
        print("    ___________", "           Your available letters are: ", get_available_letters(guessedLetters) + "\n")
        print("    )         |", "           " + "Here's your progress so far: ", get_guessed_word(theWord, guessedLetters))
        print("    o         |")
        print("    |         |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        guess = input("         ___________       Please guess a letter: \n \n \n")
        print("------------------------------------------------------------------- \n \n \n")


        guess = guess.lower()
        guessedLetters.append(guess)
        

    elif wrongGuesses == 3:
        
        print("    ___________", "           Your available letters are: ", get_available_letters(guessedLetters) + "\n")
        print("    )         |", "           " + "Here's your progress so far: ", get_guessed_word(theWord, guessedLetters))
        print("    o         |")
        print("   /|         |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        guess = input("         ___________       Please guess a letter: \n \n \n")
        print("------------------------------------------------------------------- \n \n \n")


        guess = guess.lower()
        guessedLetters.append(guess)
        

    elif wrongGuesses == 4:
        
        print("    ___________", "           Your available letters are: ", get_available_letters(guessedLetters) + "\n")
        print("    )         |", "           " + "Here's your progress so far: ", get_guessed_word(theWord, guessedLetters))
        print("    o         |")
        print("   /|\        |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        guess = input("         ___________       Please guess a letter: \n \n \n")
        print("------------------------------------------------------------------- \n \n \n")


        guess = guess.lower()
        guessedLetters.append(guess)
        

    elif wrongGuesses == 5:
        
        print("    ___________", "           Your available letters are: ", get_available_letters(guessedLetters) + "\n")
        print("    )         |", "           " + "Here's your progress so far: ", get_guessed_word(theWord, guessedLetters))
        print("    o         |")
        print("   /|\        |")
        print("   /          |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        guess = input("         ___________       Please guess a letter: \n \n \n")
        print("------------------------------------------------------------------- \n \n \n")

        
        guess = guess.lower()
        guessedLetters.append(guess)
        
    
    else:
        
        print("    ___________", "           Your available letters are: ", get_available_letters(guessedLetters) + "\n")
        print("    )         |", "           " + "Here's your progress so far: ", get_guessed_word(theWord, guessedLetters))
        print("    o         |")
        print("   /|\        |")
        print("   / \        |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        guess = input("         ___________       Please guess a letter: \n \n \n")
        print("------------------------------------------------------------------- \n \n \n")

        
        guess = guess.lower()
        guessedLetters.append(guess)
    
    if guess not in theWord or guess not in guessedLetters: 
            wrongGuesses += 1

if is_word_guessed(theWord, guessedLetters):
    print("Congratulations! You have delayed the stick figure's death until the next time someone loses.")

else:
    print("Better luck next time! The word was", theWord)

print("\n \n \n \n \n \n")

   















