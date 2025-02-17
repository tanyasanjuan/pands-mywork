# Program lab3.2X-sub.py is to substract a number from another
# Input reads in a string, so we need to it into an int
# so we can perform mathematical operations
# author: Tanya San Juan

x = int (input ('enter first number: '))
y = int (input ('enter second number: '))
answer = x - y 
print ('{} minus {} is  {}'.format (x, y, answer))

# If we enter a value is not an int, for example a float number or a word. 
# Will this cause an error? 
# Yes, because an Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length. 
# Therefore can't be a float number or a word. 
# https://www.w3schools.com/python/python_numbers.asp
