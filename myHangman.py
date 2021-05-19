import random, string, sys


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    file = open("./words.txt", "r")
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



def get_possible_matches(my_word, wordList, guessed_letters):
    '''
    Takes in a word and lists all the possible available based on how many letters have already been guessed.
    '''  
    possibleMatches = []
    formattedWord = my_word.split()
    formattedWord = ''.join(formattedWord)
    sameLengthWords = [i for i in wordList if len(i) == len(formattedWord)]
    guessed_letters = guessed_letters[:]
    for i in formattedWord:
        if i in guessed_letters:
            guessed_letters.remove(i)


    

    for i in sameLengthWords:

        for j in range(len(formattedWord)):
            
            if (formattedWord[j] != i[j] and formattedWord[j] != "_") or i[j] in guessed_letters:
                break

            else:
                
                if j+1 == len(formattedWord):
                    possibleMatches.append(i)
                
                else:
                    pass
    
    return(' '.join(possibleMatches))






print("\n \n \n \n \n \n \n \nWelcome to the game of Hangman! We will brutally hang a man until\n" 
    + "you can guess the word I randomly thought of. Sounds exciting, right?\n \n")

while True:
    print("A word has been randomly selected so you may begin your guessing!\n \n \n \n \n")

    wordList = load_words()
    #theWord = choose_word(wordList);
    theWord = "shop"
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
            guess = input("         ___________       Please guess a letter(Press * for hints): \n \n \n")
            guess = guess.lower()
            print("Enter * to get a list of all the possible words our word could be")
            if guess == '*':
                print("Your possibilities are: " + get_possible_matches(get_guessed_word(theWord, guessedLetters), wordList, guessedLetters))
                guess = input()
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
            guess = input("         ___________       Please guess a letter(Press * for hints): \n \n \n")
            
            if guess == '*':
                print("Your possibilities are: " + get_possible_matches(get_guessed_word(theWord, guessedLetters), wordList, guessedLetters))
                guess = input()
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
            guess = input("         ___________       Please guess a letter(Press * for hints): \n \n \n")
            if guess == '*':
                print("Your possibilities are: " + get_possible_matches(get_guessed_word(theWord, guessedLetters), wordList, guessedLetters))
                guess = input()

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
            guess = input("         ___________       Please guess a letter(Press * for hints): \n \n \n")
            if guess == '*':
                print("Your possibilities are: " + get_possible_matches(get_guessed_word(theWord, guessedLetters), wordList, guessedLetters))
                guess = input()

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
            guess = input("         ___________       Please guess a letter(Press * for hints): \n \n \n")
            if guess == '*':
                print("Your possibilities are: " + get_possible_matches(get_guessed_word(theWord, guessedLetters), wordList, guessedLetters))
                guess = input()
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
            guess = input("         ___________       Please guess a letter(Press * for hints): \n \n \n")
            if guess == '*':
                print("Your possibilities are: " + get_possible_matches(get_guessed_word(theWord, guessedLetters), wordList, guessedLetters))
                guess = input()
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
            guess = input("         ___________       Please guess a letter(Press * for hints): \n \n \n")
            if guess == '*':
                print("Your possibilities are: " + get_possible_matches(get_guessed_word(theWord, guessedLetters), wordList, guessedLetters))
                guess = input()
            print("------------------------------------------------------------------- \n \n \n")

            
            guess = guess.lower()
            guessedLetters.append(guess)
        
        if guess not in theWord or guess not in guessedLetters: 
                wrongGuesses += 1

    if is_word_guessed(theWord, guessedLetters):
        print("Congratulations! You have delayed the stick figure's death until the next time someone loses.")

    else:
        print("Better luck next time! The word was", theWord +"\n \n \n")


    retryAnswer = input("Press r to retry and e to exit ")

    if retryAnswer != 'r' and retryAnswer != 'e':
        retryAnswer = input("Press r to retry and e to exit ")

    elif retryAnswer == 'e':
        sys.exit()

    else:
        pass



    print("\n \n \n \n \n \n")


















