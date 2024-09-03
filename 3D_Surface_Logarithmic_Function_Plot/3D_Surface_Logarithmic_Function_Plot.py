import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function f(x, y)
def f(x, y):
    return (x * y**2) * np.log(x + y)

# Generate x and y values
x = np.linspace(1, 10, 400)  # Avoid x=0 to prevent log(0)
y = np.linspace(1, 10, 400)  # Avoid y=0 to prevent log(0)

# Create a meshgrid
X, Y = np.meshgrid(x, y)

# Compute f(X, Y)
Z = f(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set plot labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('f(x, y)')
ax.set_title('Surface plot of f(x, y) = (xy^2)ln(x+y)')

plt.show()
