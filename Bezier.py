import numpy as np
import matplotlib.pyplot as plt

def bezier_curve(p0, p1, p2, p3, num_points=100):
    t = np.linspace(0, 1, num_points)[:, np.newaxis]
    curve = (1-t)**3 * p0 + 3 * (1-t)**2 * t * p1 + 3 * (1-t) * t**2 * p2 + t**3 * p3
    return curve

# Define control points
p0 = np.array([0, 0])
p1 = np.array([0.3, 1])
p2 = np.array([0.7, 1])
p3 = np.array([1, 0])

# Generate the Bezier curve
curve = bezier_curve(p0, p1, p2, p3)

# Plotting
plt.figure()
plt.plot(curve[:, 0], curve[:, 1], 'b-')
plt.scatter([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], color='red')
plt.plot([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], 'r--')
plt.grid(True)
plt.title('Bezier Curve')
plt.show()
