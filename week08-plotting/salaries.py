# This program makes a list , that has 10 random numbers in it.
# numbers (2000 - 8000)

import numpy as np
#it is a good idea to have absolute values set into variables at the beginning of the program.
minSalary = 2000
maxSalary = 8000
numberOfEntries = 10

# The seed is set to 10, so that the random numbers are the same every time the program is run.
# This will make the random numbers the same each time.
np.random.seed(10) 

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000 # This will add 5000 to each number to each value.
print(salariesPlus)

# Multiply the salaries by 1.05, to give a 5% increase.
salariesMult = salaries * 1.05
print(salariesMult)
# This is a float array, here I convert it to an int array. (it does a floor division)
# astype(int) will convert the float to an int, but it will not round it.
# It will just take the whole number part of the float.
newSalaries = salariesMult.astype(int)
print (newSalaries)
