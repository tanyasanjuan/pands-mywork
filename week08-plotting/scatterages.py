# This program makes a list called ages that has the same number random values as salaries (range: 21 to 65)
# and plots a scatter plot of this data.

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# This is so that the random numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high= 65, size= numberOfEntries) # Absolute values set at the top.

plt.scatter(ages, salaries ) # This will be random
#plt.show() # if  you do tihs the program will halt here until the plot is closed.

#add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself.

plt.plot(xpoints, ypoints, color = "red") # This will be a line plot.
plt.show() # See how the axis have changed.
