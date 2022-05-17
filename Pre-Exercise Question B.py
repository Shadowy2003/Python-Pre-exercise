#    Pre-exercise Question B
#    The Matplotlib library is used for graphics, visualization and statistics in Python.

#    Using the _matplotlib_ library, write a program to plot a Scatter Plot graph with the following array of data:

#    x = [5, 10, 15, 20, 25, 30] for x-axis
#    y = [96, 83, 78, 60, 52, 30] for y-axis



import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 10, 15, 20, 25, 30])
y = np.array([96, 83, 78, 60, 52, 30])

plt.scatter(x, y)
plt.show()