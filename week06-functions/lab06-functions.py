# The program write a function that prints out a menu of commands we can perform
# ie. add, view, and quit.
# The function should return what the user has selected.
'''
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
'''
# With the function create a program 
# That keeps displaying the menu until the user picks quit
# If the user chooses V then call a function called doView.
def displaymenu ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View student")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    # The strip() method removes any leading and trailing whitespace from the string.

    return choice
def doAdd():
    print("in adding")
def doView():
    print("in viewing")

# main program 
choice = displaymenu()
while (choice != "q"):
    # we could do this with lambda functions, but we will not do that yet
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice != "q":
        print("\n\nplease select either a,v or q")
    choice = displaymenu()