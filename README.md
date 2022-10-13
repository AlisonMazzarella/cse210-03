Objective:
• Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time. 

Rules: 
• The puzzle is a secret word randomly chosen from a list.
• The player guesses a letter in the puzzle.
• If the guess is correct, the letter is revealed.
• If the guess is incorrect, a line is cut on the player's parachute.
• If the puzzle is solved the game is over.
• If the player has no more parachute the game is over.

Requirements: 
• The program must include a README file.
• The program must include class and method comments.
• The program must have at least four classes.
• The program must remain true to game play described in the overview.

Functionality: 
• Create dictionary with words and import csv file to main. 
• Import random but using words from dictionary.
• Create array to only accept letters found in the words from dictionary.
• While loop sends notification letter not found in word or letter found in word.
• Visual representation that parachute is cut (parachute file imported to main) 
• Play again or quit option 

Classes: 
• User (the player)
• Image (produces image of parachute after each wrong guess)
• Questions (facilitates the questions)
• Dictionary (organizes dictionary information)

Attributes:
• correct_guess
• incorrect_guess
• user
• image
• questions
• dictionary
• hotter
• colder

Access Modifiers:
• Public (no syntax)
• Protected (_) _user, _questions, _hotter, _colder 
• Private (__) _ _init_ _, _ _name_ _, __correct_guess, __incorrect_guess, __image, __dictionary

Functions:
• main
• guess
• calculate
• create_image 

Files: 
• README.md
• director.py
• parachute.py
• dictionary.py
• words.csv 

Authors: (Team E) 
- Mazzarella-Woelzl, Alison Reed (maz12005@byui.edu)
- Saenz, Paula (sae21002@byui.edu)
- Shevtsov, Denis (she21012@byui.edu)
- Ogboanoh, Richard Oshiomole Ephraim (ogb22001@byui.edu)
- Diab, Garren Mark (dia22004@byui.edu)
