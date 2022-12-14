#dictionary class to open and process words.csv file with randomized words

#using randint()
import random 

#create dictionary class
class Dictionary: 


    def __init__(self):
        self.__word = ""

    def get_word(self):
    #open file + private modifiers added to data and words, if changed will break program
        with open("words.csv", "r") as file:
            __data = file.read()
            __words = __data.split()

        #Generating a random number for word position
            word_pos = random.randint(0, len(__words)-1)
            self.__word = __words[word_pos]
            #Return the random word
            return self.__word
    
    def display_word(self):
        #Display the word
        print("Your word was:", self.__word)