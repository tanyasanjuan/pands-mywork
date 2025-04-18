# The program write a function that prints out a menu of commands we can perform
# ie. add, view, and quit.
# The function should return what the user has selected.
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


# The function readModules should read in the module names and grades
# Read modules until the user enter a module name of blank.
def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module ["name"] = moduleName
        module ["grade"] =int(input("\t\tEnter grade:"))
        modules.append(module)
        #read the next module name
        moduleName = input("\tEnter next module name (blank to quit): ").strip()
    return modules


# The function doAdd should read in the student's name and modules
def doAdd(students):
        currentstudent = {}
        currentstudent["name"] = input("Enter name: ")
        currentstudent["modules"] = readModules()

        students.append(currentstudent)


# Add the function displayModules(modules)
# The function displayModules should display the modules and their grades
def displayModules(modules):
    print ("\tname \tgrade")
    for module in modules:
        print(f"\t {module["name"]} \t {module["grade"]}")


# Add the funcionn doView(students)
# The function doView should display the students and their modules
def doView(students):
    for currentstudent in students:
        print(currentstudent ["name"])
        displayModules(currentstudent["modules"])
    print (students)


# main program 
students = []
choice = displaymenu()
while (choice != "q"):
    # we could do this with lambda functions, but we will not do that yet
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice != "q":
        print("\n\nplease select either a,v or q")
    choice = displaymenu()