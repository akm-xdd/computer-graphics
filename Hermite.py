import numpy as np
import matplotlib.pyplot as plt

def hermite_curve(p1, p2, t1, t2, num_points=100):
    t = np.linspace(0, 1, num_points)
    h1 = 2*t**3 - 3*t**2 + 1
    h2 = -2*t**3 + 3*t**2
    h3 = t**3 - 2*t**2 + t
    h4 = t**3 - t**2
    curve = np.outer(h1, p1) + np.outer(h2, p2) + np.outer(h3, t1) + np.outer(h4, t2)
    return curve

# Define points and tangents
p1 = np.array([0, 0])
p2 = np.array([1, 1])
t1 = np.array([1, 0])
t2 = np.array([1, 0])

# Generate the Hermite curve
curve = hermite_curve(p1, p2, t1, t2)

# Plotting
plt.figure()
plt.plot(curve[:, 0], curve[:, 1], 'b-')
plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color='red')
plt.quiver([p1[0], p2[0]], [p1[1], p2[1]], [t1[0], t2[0]], [t1[1], t2[1]], angles='xy', scale_units='xy', color='red')
plt.grid(True)
plt.title('Hermite Curve')
plt.show()
