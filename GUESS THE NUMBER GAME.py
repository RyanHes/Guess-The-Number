# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:21:11 2019

@author: Ryan Heslin
"""

#Number Guessing Game
#First Fully Operational Game
#Computer generates a number between 1-100
#User has to guess the number
#Computer lets the user know either higher or lower
#Computer lets the user know how many guess attempts it took 

import random
print("\n")
print("\tWelcome to the 'Guess My Numnber' Game!!")
print("\n")
print("\tI'm thinking of a number between 1 and 100")
print("\tGuess in as little attempts as possible")
print("\n")

#These are the initial values
TheNumber = random.randint(1,100)
guess = int(input("PICK A NUMBER:   "))
tries = 1

#guessing loop
while guess != TheNumber:
    if guess > TheNumber:
        print("LOWER!")
        guess = int(input("PICK A NUMBER:   "))
        tries = tries + 1
    elif guess < TheNumber:
        print("HIGHER!")
        guess = int(input("PICK A NUMBER:   "))
        tries = tries + 1
    if guess == TheNumber:
        print("YOU ARE CORRECT. THE NUMBER IS ", TheNumber, ". IT TOOK YOU", tries, " GUESSES!")
    
        
        
        

    
