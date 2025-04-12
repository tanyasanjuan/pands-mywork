# Read in two numbers and multiple them
'''
num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number: "))

answer = num1 * num2
print(f"The answer is: {answer}")
# If the user enters a decimal number, the program will crash
# If the user enters a string, the program will crash
# If the user enters a negative number, the program will work
# If the user enters a zero, the program will work
# If the user enters a very large number, the program will work
# If the user enters a very small number, the program will work

# To avoid user errors, we can use try and except
# If the user in the first input enters a string, the program will ask for a number again
try:
    num1 = int (input("Enter a number: "))
except ValueError:
    num1 = int (input("No strings a number: "))
num2 = int (input("Enter second number: "))

answer = num1 * num2
print(f"The answer is: {answer}")

# If the user in the second attempt enters a string, the program will ask for a number again
# To avoid user errors, we can use a while loop

num1 = False
while (num1 == False):
    try:
        num1 = int (input("Enter a number: "))
    except ValueError:
        print ("Please enter a number: ")

num2 = int (input("Enter second number: "))

answer = num1 * num2
print(f"The answer is: {answer}")

# If the user for the second number enters a string, the program will crash
# To avoid user errors, we will use a while loop for the second number as well
# If the user in the second number enters a string, the program will ask for a number again
num1 = False
while (num1 == False):
    try:
        num1 = int (input("Enter a number: "))
    except ValueError:
        print ("That was not a number", end=" ")

num2 = False
while (num2 == False):
    try:
        num2 = int (input("Enter second number: ")) 
    except ValueError:
        print ("That was not a number", end=" ")

answer = num1 * num2
print(f"The answer is: {answer}")
'''
# To have a code cleaner and easier to read and use, we can use a function
def readNum():
    num = False
    while (num == False):
        try:
            num = int (input("Enter a number: "))
        except ValueError:
            print ("That was not a number", end=" ")
    return num
# Now we can use the function to read the numbers
num1 = readNum()
num2 = readNum()

answer = num1 * num2

print(f"The answer is: {answer}")