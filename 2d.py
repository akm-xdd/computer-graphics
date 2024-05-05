import numpy as np
import matplotlib.pyplot as plt

# Create a set of points representing a 2D object (a triangle in this example)
points = np.array([
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1]

])

def apply_transformation(points, transformation_matrix):
    return np.dot(points, transformation_matrix.T)

def translation(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def scaling(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def rotation(theta):
    rad = np.radians(theta)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad), 0],
        [0, 0, 1]
    ])

def shear(kx, ky):
    return np.array([
        [1, kx, 0],
        [ky, 1, 0],
        [0, 0, 1]
    ])

def reflection():
    return np.array([
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])

# Perform transformations
translated = apply_transformation(points, translation(2, 3))
scaled = apply_transformation(points, scaling(2, 2))
rotated = apply_transformation(points, rotation(45))
sheared = apply_transformation(points, shear(0.5, 0.5))
reflected = apply_transformation(points, reflection())

# Plot the original and transformed objects in subplots
fig, axes = plt.subplots(2, 3, figsize=(10, 10))

# Original
axes[0, 0].plot(*zip(*points[:, :2]), 'r-o')
axes[0, 0].set_title("Original")
axes[0, 0].grid(True)

# Translated
axes[0, 1].plot(*zip(*translated[:, :2]), 'g-o')
axes[0, 1].set_title("Translated")
axes[0, 1].grid(True)

# Scaled
axes[1, 0].plot(*zip(*scaled[:, :2]), 'b-o')
axes[1, 0].set_title("Scaled")
axes[1, 0].grid(True)

# Rotated
axes[1, 1].plot(*zip(*rotated[:, :2]), 'y-o')
axes[1, 1].set_title("Rotated")
axes[1, 1].grid(True)

# Sheared
axes[1, 2].plot(*zip(*sheared[:, :2]), 'm-o')
axes[1, 2].set_title("Sheared")
axes[1, 2].grid(True)

# Reflected
axes[0, 2].plot(*zip(*reflected[:, :2]), 'c-o')
axes[0, 2].set_title("Reflected")
axes[0, 2].grid(True)

# Adjust layout and show
plt.tight_layout()
plt.show()
