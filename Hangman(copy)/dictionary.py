words = {
}

class listFunctions():

    def __init__(self, word):
        self.word = word


    def BlankCheck(self):
        file = open("words.txt", "r+")
        raw_word = file.read()
        colist = raw_word.split('\n')
        end_txt = colist[-1]
        if end_txt == '':
            colist.pop()
        else:
            pass
        return colist, file

    def WordCount(self):
        file = open("words.txt", "r+")
        raw_word = file.read()
        colist = raw_word.split('\n')
        line = 0
        for i in colist:
            if i:
                line += 1
        file.close()
        print(line)
        return line

    def WordGrab(self):
        y = 0
        file = open("words.txt", "r+")
        colist, file = self.BlankCheck()
        for x in colist:
            words[y] = x
            y = y + 1
            file.close()
        return colist


    def WordWrite(self, w):

        file = open("words.txt", "r+")
        colist = self.WordGrab()
        for i in colist:
            file.write(f"{i}\n")
        file.write(f"{w}")
        file.close()

    def ListRead(self):
        words = self.WordGrab()
        for i in words:
            print(i)

    def WordInput(self):
        new_word = input("What word would you like to add?: ")
        word_add = input(f"{new_word}?, Are you sure? [Y/N/CANCEL]: ")

        if word_add.upper() == "Y":
            y = self.WordCount()
            self.WordWrite(new_word)
            print("Word added to list, all words can be located in hang/words.txt")
        elif word_add.upper() == "N":
            self.WordInput()
        elif word_add.upper() == "CANCEL":
            pass
        else:
            print("""Invalid input, please type 'Y', 'N', or 'CANCEL' """)
            self.WordInput()

    def WordRemove(self, word):
        file = open("words.txt", "r+")
        colist = self.WordGrab()
        if word.lower() in colist:
            for i in colist:
                file.truncate(0)
            colist.remove(word.lower())
            for i in colist:
                file.write(f"{i}\n")
                
            file.close()    
        elif word.lower() == '': 
            file.close()
        else: 
            print("Word not In list")
            input('\nPress Enter to Continue: ')
            file.close()