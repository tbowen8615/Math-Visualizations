import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function
def f(x, y):
    return 3*x**2 - 5*x*y - 4*y**2

# Create a grid of (x, y) values
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)
z = f(x, y)

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface = ax.plot_surface(x, y, z, cmap='viridis', alpha=0.7)

# Plot the plane z=0
z_plane = np.zeros_like(x)
plane = ax.plot_surface(x, y, z_plane, color='red', alpha=0.5)

# Label the axes
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Add a legend
plane_proxy = plt.Line2D([0], [0], linestyle="none", color='red', marker='o')
surface_proxy = plt.Line2D([0], [0], linestyle="none", color='yellowgreen', marker='o')
ax.legend([surface_proxy, plane_proxy], ['Surface: f(x, y)', 'Plane: z = 0'], numpoints=1)

plt.show()
