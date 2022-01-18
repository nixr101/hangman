from dictionary import listFunctions
import gamestates
import os
import random

class gameFunctions():



    def __init__(self):
        pass


    def GameStart(self):
        os.system('cls')
        print("""
    ----------HANGMAN----------
    [1]	    Play
    [2]    View/ Add words
    [3]	    Help            \n""")

        game_choice = input("Enter Corresponding number to choose: ")
        return str(game_choice)


    def Difficulty(self):
        valid = True
        os.system('cls')
        print("""
    ----------HANGMAN----------
            Difficulty
    [1]     EASY - (6 Words or Less)
    [2]     HARD - (7 Words or More)\n""")
        diff = input("Enter Corresponding number to choose: ")

        difficulty = listFunctions(None)
        colist = difficulty.WordGrab()
        word_pool = []

        if diff == "1":
            for x in colist:
                if len(x) < 6:
                    word_pool.append(x)
            played_word = random.choice(word_pool)
            return played_word, valid
        elif diff == "2":
            for x in colist:
                if len(x) > 6:
                    word_pool.append(x)
            played_word = random.choice(word_pool)
            return played_word, valid
        else:
            played_word = None
            print("Please Enter a Valid Response")
            input("Press Enter to Continue: ")
            # self.Difficulty()
            valid = False
            return played_word, valid


    def WordGuess(self):
        guessed_numbers = []
        guessed_numbers.append(input("Guess a Number"))


    def DisplayState(self, played_word, stage, guessed):
        os.system('cls')
        guessed.sort()

        displayed_letters = []
        i = 0
        sep = ' '

        for x in played_word:
            displayed_letters.append("_")

        for x in played_word:  
            if x.upper() in guessed:
                displayed_letters[i] = x
            i = i + 1

        state = gamestates.GiveState(stage)
        state = state.givestate()
        print(state)
        # print(played_word)
        print(' ' * 11 + 'USED')
        g = 0
        f = len(guessed) % 5
        fa = (len(guessed) - f) / 5

        if f == 0:
            for x in range(0, int(fa)):
                    print(guessed[g:g + 5])
                    g = g + 5
        else:
            for x in range(0, int((fa + 1))):
                    print(guessed[g:g + 5])
                    g = g + 5           
 
        print("\n" + sep.join(displayed_letters).center(27, '-'))
        return guessed

    def to_upper(self, oldList):
        guessed = []
        for element in oldList:
            guessed.append(element.upper())
        return guessed


    def Win(self):
        os.system('cls')
        state = gamestates.GiveState(7)
        state = state.givestate()
        print(state)
        input("Press Enter to Continue: ")


    def Lose(self,played_word):
        os.system('cls')

        state = gamestates.GiveState(6)
        state = state.givestate()
        print(state)
        print(f'The Word was: {played_word}')
        input("Press Enter to Continue: ")


    def Play(self):
        valid = False
        game_choice = self.GameStart()
        if game_choice == '1':
            while valid == False:
                played_word, valid = self.Difficulty()

            guessed = []
            playing = True
            stage = 0

            def add(guessed):
                guessed.append(guess)
                guessed = self.to_upper(guessed)
                print(guessed)

            y = 0
            while playing == True:

                    # if y >= len(played_word):
                    #         playing = False
                    #         self.Win()   
                    # else:
                    #     pass

                    self.DisplayState(played_word, stage, guessed)      
                    guess = input('Guess a Word: ') 

                    if guess.upper() not in guessed and guess.isalpha() and len(guess) == 1:
                        add(guessed)
                        guessed = self.to_upper(guessed)
                        
                        # for x in guessed:
                        # if guess in played_word:
                        count = played_word.count(guess)
                        y = y + count
                        # else:
                        #     pass

                        if guess in played_word:
                            pass
                        else:
                            stage = stage + 1
                        # print(y)
                        # input("\nPress Enter to Continue: ")
                    elif guess.upper() in guessed and guess.isalpha():
                        print("You have Already Guessed This.")
                        input("\nPress Enter to Continue: ")
                    else:
                        print('Please use a Letter of the Alphabet.')
                        input("\nPress Enter to Continue: ")

                    if y >= len(played_word):
                        playing = False
                        self.Win()
                    elif stage >= 6:
                        playing = False
                        self.Lose(played_word)
                    else:
                        pass

        elif game_choice == '2':
            os.system('cls')
            print("""
    ----------HANGMAN----------
    [1]	   Add Word
    [2]    View Word
    [3]    Remove Word\n""")

            word_rm = None
            game_choice = str(input("Enter Corresponding number to choose: "))
            listfunctions = listFunctions(word_rm)
            if game_choice == '1':
                os.system('cls')
                print('    ----------HANGMAN----------\n')
                listfunctions.WordInput()
            elif game_choice == '2':
                os.system('cls')
                print('    ----------HANGMAN----------\n')
                listfunctions.ListRead()
                input("\nPress Enter to Continue: ")
            elif game_choice == '3':
                os.system('cls')
                print('    ----------HANGMAN----------\n')
                listfunctions.ListRead()
                word_rm = input("""\nWhich Word Would you Like to Remove? (Press Enter to cancel): """)
                listfunctions.WordRemove(word_rm)
            else:            
                print("Please Enter a Valid Response")
                input("Press Enter to Continue: ")
    

        elif game_choice == '3':
            os.system('cls')
            print('    ----------HANGMAN----------\n')
            print('''All saved words can be found in /hang/words.txt
If you would like to revert the contents of words.txt,
the original wordlist can be found in /hang/orig.txt''')
            input("\nPress Enter to Continue: ")
        else:
            print('Please enter a valid input')
            input('Press Enter to Continue: ')


playing = True               
while playing == True:
    play = gameFunctions()
    play.Play()
    
