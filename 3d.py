import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of a simple 3D cube
cube = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Transformation matrices
def translation(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def scaling(sx, sy, sz):
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

def rotation_z(theta):
    rad = np.radians(theta)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0, 0],
        [np.sin(rad), np.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def shear_xy(kx, ky):
    return np.array([
        [1, kx, 0, 0],
        [ky, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# Projection matrices
def parallel_projection():
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ])

def perspective_projection(d):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1/d],
        [0, 0, 0, 0]
    ])

# Apply transformations
cube_homogeneous = np.hstack([cube, np.ones((8, 1))])  # Convert to homogeneous coordinates
translated = np.dot(cube_homogeneous, translation(1, 2, 3).T)
scaled = np.dot(cube_homogeneous, scaling(2, 2, 2).T)
rotated = np.dot(cube_homogeneous, rotation_z(45).T)
sheared = np.dot(cube_homogeneous, shear_xy(0.5, 0.5).T)

# Apply projections
parallel = np.dot(cube_homogeneous, parallel_projection().T)
perspective = np.dot(cube_homogeneous, perspective_projection(5).T)
perspective[:, :3] /= perspective[:, 3][:, np.newaxis]  # Normalize by the w component

# Plotting
fig, axs = plt.subplots(3, 3, subplot_kw={'projection': '3d'}, figsize=(12, 12))

def plot_cube(ax, cube, title):
    k = [[0, 1, 2, 3, 0], [4, 5, 6, 7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]
    for i in k:
        ax.plot3D(*cube[i].T, color="b")
    ax.set_title(title)

plot_cube(axs[0, 0], cube, "Original")
plot_cube(axs[0, 1], translated[:, :3], "Translated")
plot_cube(axs[1, 0], scaled[:, :3], "Scaled")
plot_cube(axs[1, 1], rotated[:, :3], "Rotated")
plot_cube(axs[2, 0], sheared[:, :3], "Sheared")
plot_cube(axs[2, 1], parallel[:, :3], "Parallel Projection")
plot_cube(axs[2, 2], perspective[:, :3], "Perspective Projection")

for ax in axs.flatten():
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

plt.tight_layout()
plt.show()
