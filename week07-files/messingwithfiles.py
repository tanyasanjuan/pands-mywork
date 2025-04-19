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
print(f"we have run this program {number} times.")

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

# The function will store a simple Dictionary to a file as JSON.
# Import json: The json module provides functions for working with JSON data.

import json
FILENAME = "testdict.json"
sample= dict(name='Fred', age=31, grades=[1,34,55])

def writeDict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)
    # The json.dump() function writes the JSON representation of the object to the file.
    # The "wt" mode opens the file for writing in text mode.
    # The file will be created if it does not exist.
    # If the file exists, it will be overwritten.

# Test the writeDict function
writeDict(sample)
# The testdict.json file it's very similar to a Dict.


# The function will read in a dict object from a file.
def readDict():
    # This will throw an error if the file does not exist.
    # It should readly just return an empty dict.
    with open(FILENAME) as f:
        return json.load(f)
    
# Test the readDict function
somedict = readDict()
print(somedict)
