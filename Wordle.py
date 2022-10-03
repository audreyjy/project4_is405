# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    
    # Checks if input is in word list and displays messages
    def enter_action(input_string):
        if input_string.lower() in FIVE_LETTER_WORDS:
            gw.show_message("That is a word!")
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message(input_string + " in word list")
            gw.set_square_letter(gw.get_current_row(), 0, 'Z')



    def add_row(row_number, input_string) :
        for i, letter in  enumerate(input_string) :
            gw.set_square_letter(row_number, i, letter) 


    # get random word from word list and make it an array
    correct_answer = random.choice(FIVE_LETTER_WORDS)
    correct_answer_list = list(correct_answer)
    correct_guess = False



    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    


    
# Startup code

if __name__ == "__main__":
   wordle()


