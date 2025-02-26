# This program prints out a number guess for the user 
# The program should keep promting the user to guess the number 
# until the users gets the right on
# Author: Tanya San Juan

numberToGuess = 30
guess = int (input ('Please guess the number: ')) 
while guess != numberToGuess:
    print ('wrong')
    guess = int (input ('Please guess again: '))

print ('Well done! Yes the number was: ', numberToGuess)