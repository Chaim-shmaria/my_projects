# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math


p = 0.5
# Creating vectors X and Y
x = np.linspace(1, 10000, 100)

y = ((1-p)**(x-1))*p

fig = plt.figure(figsize=(10, 5))
# Create the plot

plt.plot(x, y)

# Show the plot
plt.show()
