import random
import string

WORDLIST_FILENAME = "words.txt"

def restart():
    while True:
        replay = input("""
        Would you like to play again? Press y or for Yes or n for No: """)
        if replay == "y":
            secretWord = chooseWord(listword).lower()
            hangman(secretWord)
            hangman()
        elif replay == "n":
            print(""" Goodbye!! """)
            break
        else:
            print ("""
            You must enter either y or n.""")
            resart()

def loadWords():

    print ("Reading words from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    fullline = inFile.readline()
    listword = fullline.split()
    print ((" "), len(listword), "words loaded.")
    return listword

def chooseWord(listword):
    """
    listword (list): list of words (strings)

    Returns a word from listword at random
    """
    return random.choice(listword)

listword = loadWords()

def isWordGuessed(secretWord, lettersGuessed):

    count = 0
    for i, c in enumerate(secretWord):
    	if c in lettersGuessed:
    		count += 1
    if count == len(secretWord):
    	return True
    else:
    	return False

def getGuessedWord(secretWord, lettersGuessed):

    count = 0
    blank = ['_ '] * len(secretWord)

    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
            count += 1
            blank.insert(count-1,c)
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        
def getAvailableLetters(lettersGuessed):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = alphabet[:]

    def removeDupsBetter(L1, L2):
        L1Start = L1[:]
        for e in L1:
            if e in L1Start:
                L2.remove(e)
        return ''.join(str(e) for e in L2)

    return removeDupsBetter(lettersGuessed, alphabet2)

def hangman(secretWord):

    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 10
    wordGuessed = False
    # play_again = True

    # while play_again:
    print ('Welcome to the game, Hangman!')
    print (('I am thinking of a word that is ') + intro + (' letters long.'))
    print ('------------')

    while mistakesMade > 0 and mistakesMade <= 10 and wordGuessed is False:
        if mistakesMade == 10:
            print(
            """
            -----
            |   |
            |
            |
            |
            |
            |
            |
            |
            --------
            """
            )
        elif mistakesMade == 9:
            print(
            """
            -----
            |   |
            |   0
            |
            |
            |
            |
            |
            |
            --------
            """
            )
        elif mistakesMade == 8:
            print(
            """
            -----
            |   |
            |   0
            |  -+-
            |
            |
            |
            |
            |
            --------
            """
            )
        elif mistakesMade == 7:
            print(
            """
            -----
            |   |
            |   0
            | /-+-
            |
            |
            |
            |
            |
            --------
            """
            )
        elif mistakesMade == 6:
            print(
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |
            |
            |
            |
            |
            --------
            """
            )
        elif mistakesMade == 5:
            print(
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |
            |
            |
            |
            --------
            """
            )
        elif mistakesMade == 4:
            print(
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |
            |
            |
            --------
            """
            )
        elif mistakesMade == 3:
            print(
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  |
            |
            |
            --------
            """
            )
        elif mistakesMade == 2:
            print(
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | 
            |  | 
            |
            --------
            """
            )
        elif mistakesMade == 1:
            print(
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | | 
            |  | 
            |
            --------
            """
            )
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            print ("Congratulations, you won!!")
            print (
                """ 
                \  0  /
                 \-+-/
                   |
                   |
                  | |
                  | |
                """
                )
            print (
                """
                ___      __      ___   _____________   __    ___   __    ___    ________    _______    __
                \  \    /  \    /  /   |____   ____|  |  \   | |  |  \   | |   |  ______|  |   __  |  |  |
                 \  \  /    \  /  /         | |       | | \  | |  | | \  | |   |  |___     |  |__| |  |  |
                  \  \/  /\  \/  /          | |       | |\ \ | |  | |\ \ | |   |   ___|    |      _|  |__|
                   \    /  \    /       ____| |____   | | \ \| |  | | \ \| |   |  |_____   |  |\  \    __  
                    \__/    \__/       |___________|  |_|  \___|  |_|  \___|   |________|  |__| \__\  |__|
                """
                )
            restart()
            # print ("Would you like to play again?(yes or y)")

            #     response0 = input("> ").lower()
            #     if response0 not in ("yes", "y"):
            #         play_again = False

            wordGuessed = True
            break
        print (('You have ') + str(mistakesMade) + (' guesses left.'))
        print (('Available letters: ') + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print (("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print (('Good guess: ') + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if guess in lettersGuessed:
                print (("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print (('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')

        if wordGuessed == True:
            return 'Congratulations, you won!'
        elif mistakesMade == 0:
            print(
                """
                -----
                |   |
                |   0
                | /-+-\ 
                |   | 
                |   | 
                |  | | 
                |  | | 
                |
                --------
                DEAD!!
                """
                )
            print (('Sorry, you lost. The word was ') + secretWord)
            restart()
        # print ("Would you like to play again?(yes or y)")

        # response = input("> ").lower()
        # if response not in ("yes", "y"):
        #     play_again = False
        # elif response is ("y"):

secretWord = chooseWord(listword).lower()
hangman(secretWord)
