# Read in two numbers and multiple them

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
