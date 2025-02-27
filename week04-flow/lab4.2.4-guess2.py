# This program the tells the user if there guess is too high or too low, 
# Shows statement inside the while loop if the guess is not accurate
# Generate a random number between 0 and 100 to guess.
# Author: Tanya San Juan

# import random randit information: https://docs.python.org/3/reference/import.html
from random import randint

numberToGuess = randint(0, 100)
guess = int (input ('Please guess the number: ')) 
while guess != numberToGuess:
    if guess < numberToGuess:
        print ('too low')
    else: 
        print ('too high')    
    guess = int (input ('Please guess again: '))

print ('Well done! Yes the number was: ', numberToGuess)
