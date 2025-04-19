# This proram counts how many times the program was run
# and saves it to a file called count.txt
# The program will read the file and increment the count by 1
# and then write the new count to the file.

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

#test the readNumber function
num = readNumber()
print(num)