# Program lab3.1.4-randomGenerator.py prints out a random number between 1 and 10.
# Author: Tanya San Juan

import random
number = random.randint(1,10)
print ('Here is a random number {}'.format (number))

# Modify the program so that the user inputs the range.
import random
min_number = int (input ('Enter a minimum value: '))
max_number = int (input ('Enter a maximum value: '))
random_number = random.randint (min_number, max_number)
 
#print the results
print (f'Here is a random number between {min_number} and {max_number}: {random_number}')