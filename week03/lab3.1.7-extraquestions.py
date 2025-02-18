# Program lab3.7X-extraquestions.py is to solve extra questions for week 3.
# Author: Tanya San Juan
'''
# Question 6: Why does this expression cause an error? 
message = 'I have eaten' + 99 + 'burritos'
print (message)

# There is an error because the are strings + int (number 99), 
# And it is not possible the contatenation between a string and an int using the +.

# Question 7: How can you fix it? 
# To solve this problem should we convert the integer to a string. 
'''
numburritos = 99
message = 'I have eaten ' + str (numburritos) + ' burritos'
print (message)

# Question 8: Why is eggs a valid variable name while 100 is invalid?
# Python cannot accept variables starting with numbers, or only number. However we can use egg100

# Question 9: What three functions can be used to get the integer, floating-point number, or string version of a value?
# To convert a value into a Integer we can use the function "int()" 
# To convert a value into a Float number we can use the function "float()"
# To convert any tyoe into a String we can use the function "str()"
