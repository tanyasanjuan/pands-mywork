# This program makes a list , that has 10 random numbers in it.
# numbers (2000 - 8000)

import numpy as np
#it is a good idea to have absolute values set into variables at the beginning of the program.
minSalary = 2000
maxSalary = 8000
numberOfEntries = 10
np.random.seed(10) # This will make the random numbers the same each time.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print(salaries)
