"""
=======================================================================================================================
Title           : Paraboloid and z-Plane Visualization
Description     : This program visualizes a 3D surface plot of the function f(x,y) = 44 - x^2 - y^2 along with a
                    horizontal plane at z = 8. This is useful for intuitively understanding the region being integrated
                    between the plane and the surface of the paraboloid.
Author          : Tyler Bowen
Date            : August 2, 2024
Version         : 1
Usage           : Ensure you have NumPy and Matplotlib installed and run the program. A 3D interactive visualization
                    will appear.
Notes           : Nothing particularly noteworthy.
Python Version  : 3.11.7
=======================================================================================================================
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function and the plane
def f(x, y):
    return 44 - x**2 - y**2

# Set up a grid for plotting
x = np.linspace(-7, 7, 400)
y = np.linspace(-7, 7, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Define the plane z = 8
Z_plane = np.full_like(X, 8)

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface of the function
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')

# Plot the plane z = 8
plane = ax.plot_surface(X, Y, Z_plane, color='red', alpha=0.5, edgecolor='none')

# Add a color bar which maps values to colors
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Visualization of f(x, y) = 44 - x^2 - y^2 and the plane z = 8')

# Set the limits of the plot
ax.set_xlim([-7, 7])
ax.set_ylim([-7, 7])
ax.set_zlim([0, 50])

plt.show()
