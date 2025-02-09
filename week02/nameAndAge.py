# nameAndAge.py
# This program gives name and age, plus certain mathematical operations.
# I added solutions that I thought of and there are also solutions based on 3Wschool examples. 
# I added the solutions I come up with, in case of possible feedback. Thanks!
# author: Tanya San Juan

# This is the first solution I found to the problem.
name = input ("Enter your name: ")
number = int (input ('please enter your year of birth: '))
newNumber = 2025 - number
print (f'Hello {name}, your age is {newNumber}.')

# 2nd solution, the follow solution I consider is simplear that the 1st one I thought. I guide myself using W3School.
# The numbers in {} line 15, are index numbers and refers to the position of an element in a sequence (like a list). 
# Indexing starts at 0. 
age = "21"
name = "Andrew"
txt = "Hello {1}, your age is {0}."
print(txt.format (age,name))

#Adding a tab for the 2nd solution to separate the sentences. 
age = "21"
name = "Andrew"
txt = "Hello {1},\t your age is {0}."
print(txt.format (age,name))

# Added a tab in the 1st solution I got to show a space between the two sentences.
name = input ("Enter your name: ")
number = int (input ('please enter your year of birth: '))
newNumber = 2025 - number
print (f'Hello {name},\t your age is {newNumber}.')

#Writing a program that outputs 21- 4
answer = 21 - 4
print (answer)

#Writing a program that 2 is equal to 3
x = 2
y = 3
print (x==y)
