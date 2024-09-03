import numpy as np
import matplotlib.pyplot as plt

# Define the bounds in polar coordinates
theta = np.linspace(0, np.pi/4, 400)
r = np.linspace(0, 4, 400)
theta_grid, r_grid = np.meshgrid(theta, r)
x = r_grid * np.cos(theta_grid)
y = r_grid * np.sin(theta_grid)

# Plot the region in Polar coordinates
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
ax.plot(theta, 4 * np.ones_like(theta), 'r', label=r'$r = 4$')
ax.plot(np.pi/4 * np.ones_like(r), r, 'b', label=r'$\theta = \pi/4$')
ax.fill_between(theta, 0, 4, color='gray', alpha=0.3)
ax.set_title('Region of Integration in Polar Coordinates')
ax.legend()
plt.show()
