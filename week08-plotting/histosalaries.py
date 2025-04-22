# This program will plots a histogram of the salaries.
# import numpy as np

import numpy as np
# import matplotlib.pyplot as plt: The matplotlib.pyplot module provides a MATLAB-like
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# This is so that the random numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.show()