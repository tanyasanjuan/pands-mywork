# This program reads in numbers until the user enters a 0.
# It will them print back out again
# And their avarage.

numbers = []

# first number then we check if it is 0 in the while loop
number = int(input ('enter number (0 to quit): '))

while number !=0: 
    numbers.append(number)

    #read the next number and check if 0
    number = int(input('enter another (0 to quit): '))

for value in numbers:
    print (value)

# I want avarage to be a float
avarage = float (sum (numbers)) / len(numbers)
print (f'The avarage is {avarage}')    