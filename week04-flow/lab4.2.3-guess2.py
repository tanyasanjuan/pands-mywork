# This program the tells the user if there guess is too high or too low, 
# Shows statement inside the while loop if the guess is not accurate
# Author: Tanya San Juan

numberToGuess = 30
guess = int (input ('Please guess the number: ')) 
while guess != numberToGuess:
    if guess < numberToGuess:
        print ('too low')
    else: 
        print ('too high')    
    guess = int (input ('Please guess again: '))

print ('Well done! Yes the number was: ', numberToGuess)