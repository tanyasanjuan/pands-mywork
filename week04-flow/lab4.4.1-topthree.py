# This program generates 10 random numbers. 
# prints them out, then 
# prints out the top 3

# It'll be used a list to store and
# manupulate the numbers. 

import random
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100

numbers = []

for i in range (0, howMany):
    numbers.append(random.randint(rangeFrom, rangeto))
print (f'{howMany} random numbers\t {numbers}')

# keeping the original list
topOnes = numbers.copy()

topOnes.sort(reverse = True)
print (f'The top {topHowMany} are \t\t {topOnes[0:topHowMany]}')