# This proram counts how many times the program was run
# and saves it to a file called count.txt

# The funtion will read the file and oyutput the number. 

FILENAME = "count.txt"
def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        # This file will be created when we write back.
        # no file assumes fisrt time running the program.
        # ie 0 previous runs.
        return 0

#test the readNumber function
num = readNumber()
print(num)


# The function will write the number to the file.
def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))
# test the writeNumber function
writeNumber(15)
# The text file will show 3 in it. 
# If the number 3 is modified to 4, the text file will show 4 in it.
# But the number printed will be 3. (The previous number)

# The function will count how many times the program was run.
# Main program
# read the number from the file
number = readNumber()

# increment the number by 1
number += 1
print(f"we have run this program has {number} times.")

# write the new number to the file
writeNumber(number)


# The program will check if the file exists.
# If the file does not exist, it will create the file and write 0 to it.
# Import os.path: The os.path module provides functions 
# for manipulating file and directory paths.
import os.path
FILENAME = "count.txt"
# check if the file exists
if not os.path.isfile(FILENAME):
    print ("File does not exist.")
    # create the file and write 0 to it
    writeNumber(0)

