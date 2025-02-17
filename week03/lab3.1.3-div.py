# Program lab3.1.3-div.py reads in two numbers
# And outputs the integer answer and reminder.
# Author: Tanya San Juan

x = int (input ('enter first number: '))
y = int (input ('enter the number you want to divide by: '))
answer = int (x // y) # the use of // gives the int division
remainder = x % y # the use % gives the remainder

print ('{} divided by {} is {} whith remainder {}'.format (x, y, answer, remainder))
