# The program write a function that prints out a menu of commands we can perform
# ie. add, view, and quit.
# The function should return what the user has selected.

def displaymenu ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View student")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    # The strip() method removes any leading and trailing whitespace from the string.

    return choice

# Test the function
choice = displaymenu()
print(f"You selected: {choice}")