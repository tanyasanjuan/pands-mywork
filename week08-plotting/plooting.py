# This program plots the function y = x^2
# Import matplotlib.pyplot as plt: The matplotlib.pyplot module provides a MATLAB-like 
# interface for creating plots and visualizations.
# Import numpy as np: The numpy module provides support for large, 
# multi-dimensional arrays and matrices,

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # muktiply each entry by itself.

plt.plot(xpoints, ypoints)
plt.show()