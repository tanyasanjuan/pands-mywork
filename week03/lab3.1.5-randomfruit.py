# Program lab3.1.5-randomfruit.py prints out a random fruit.
# Author: Tanya San Juan

import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# We want a random number between 0 and lenght -1
index = random.randint (0, len(fruits)-1)

fruit = fruits [index]

print ('A Random Fruit {}'.format (fruit))
