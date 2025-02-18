# This program read in a string and strips
# any leading or trailing spaces. 
# It also covnerts all the letters to lower case. 
# It then outputs the lengths of the original string
# and the normalised one
# Author: Tanya San Juan

rawstring = input ('please enter a string: ')
normalisedstring = rawstring.strip().lower()

lengthofrawstring = len (rawstring)
lengthofnormalised = len (normalisedstring)

print (f'That string normalised is: {normalisedstring}')
print (f'We reduced the input string from {lengthofrawstring} to {lengthofnormalised} characters')