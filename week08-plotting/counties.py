# This program has a list of counties, and pick from a five counties. 
# It make some counties appear more than others. 
# It make a pie chart of the counties.

# Demostrate making a pie plot of the unique occurance of values in an array.
# Demostrate more than more than just how to do pies plots.

import numpy as np
import matplotlib.pyplot as plt

# make the arrays of occurences
possibleCounties = ["Mayo", "DirtyDublin", "Galway", "Rosommon", "Donegal"]
# pick 100 randomly from possible counties with the frequency set in p
counties = np.random.choice(
    possibleCounties, 
    p=[0.1, 0.3, 0.2, 0.12, 0.28],
    size=(100)
) 

# right now we need the number of occurances of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)
# we can now put this into a pie plot
#plt.pie(counts, labels=unique)
#plt.show()

# The program now make bar chart of the counties
plt.bar(unique, counts)
plt.show()
