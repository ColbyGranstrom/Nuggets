# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:15:24 2016

@author: colbygranstrom
"""
import random

def print_header():
    print("\tWelcome to 'Guess My Number'!")
    print("\tI'm going to guess your number between 1 and 100.")
    print("\tI will try to guess it in as few attempts as possible.\n")


def print_footer(guess, tries):
    print("I guessed it! The number was", guess)
    print("And it only took me", tries, "tries!\n")
    print("\n\nPress the enter key to exit.")    
    
def main():
    # print the greeting banner
    print_header()
    
    # set the initial values
    
    
    def c_guess (High,Low):
        The_Guess = (High+Low)//2
        return The_Guess
    
    Low = 0
    High = 100
    guess = c_guess(High, Low)
    tries = 1
    
    user_input = input ("Was the guess + " + str(guess) + " higher, lower, or good? ")
    while  user_input != "good":
        if user_input == "higher":
            Low = guess + 1
            guess = c_guess (High,Low)
            tries = tries + 1
        if user_input == "lower":
            High = guess - 1
            guess = c_guess (High,Low)
            tries = tries + 1
        user_input = input ("Was the guess  " + str(guess) + " higher, lower, or good? ")

    print_footer(guess, tries)
    
if __name__ == "__main__":
    main()

