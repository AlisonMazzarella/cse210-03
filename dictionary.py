#dictionary class to open and process words.csv file with randomized words

#using randint()
import random 

# open file
with open("words.csv", "r") as file:
    data = file.read()
    words = data.split()

    #Generating a random number for word position
    word_pos = random.randint(0, len(words)-1)
    print("Your word was:", words[word_pos])