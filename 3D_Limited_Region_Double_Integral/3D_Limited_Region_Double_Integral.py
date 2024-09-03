import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for x and y
x = np.linspace(0, 2, 400)
y = np.linspace(0, 2, 400)
x, y = np.meshgrid(x, y)

# Define the function e^(x^2)
z = np.exp(x**2)

# Mask the region outside y <= x
z = np.where(y <= x, z, np.nan)

# Create the plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis (e^(x^2))')
ax.set_title('Graph of e^(x^2) over the Region 0 <= y <= x and 0 <= x <= 2')

plt.show()
