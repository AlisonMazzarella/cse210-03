#dictionary class to open and process words.csv file with randomized words

#using randint()
import random 

#create dictionary class
class Dictionary: 

#open file + private modifiers added to data and words, if changed will break program
    with open("words.csv", "r") as file:
        __data = file.read()
        __words = __data.split()

    #Generating a random number for word position
        word_pos = random.randint(0, len(__words)-1)
        print("Your word was:", __words[word_pos])