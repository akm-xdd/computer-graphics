import numpy as np
from skimage.draw import polygon

# Define polygon vertices (x, y)
vertices = np.array([[10, 20], [30, 40], [50, 30]])

# Create an empty image
image = np.zeros((100, 100), dtype=np.uint8)

# Fill the polygon
rr, cc = polygon(vertices[:, 1], vertices[:, 0])
image[rr, cc] = 255  # Set pixel values to black

# Display the image
import matplotlib.pyplot as plt
plt.imshow(image, interpolation='nearest')
plt.axis('off')
plt.show()



# import numpy as np
# import matplotlib.pyplot as plt

# # Function to find intersections of scanline with polygon edges
# def find_intersections(x, y, vertices):
#     intersections = []
#     n = len(vertices)

#     for i in range(n):
#         x1, y1 = vertices[i]
#         x2, y2 = vertices[(i + 1) % n]

#         if y1 <= y and y2 > y or y1 > y and y2 <= y:
#             if y1 != y2:
#                 xi = x1 + (y - y1) / (y2 - y1) * (x2 - x1)
#                 if xi <= x:
#                     intersections.append(xi)

#     return intersections

# # Function to fill polygon using scanline algorithm
# def scanline_fill(vertices, height):
#     min_y = min(vertices, key=lambda p: p[1])[1]
#     max_y = max(vertices, key=lambda p: p[1])[1]

#     scanlines = {}
#     for y in range(min_y, max_y + 1):
#         scanlines[y] = []

#     for y in range(min_y, max_y + 1):
#         intersections = find_intersections(float('-inf'), y, vertices)
#         intersections.sort()
#         counter = 0
#         for pixel in range(0, height + 1):
#             if pixel in intersections:
#                 counter += 1
#             if [p for p in vertices if p[1] == y]:
#                 counter += 2
#             if counter % 2 == 1:
#                 scanlines[y].append(pixel)

#     return scanlines

# # Function to plot filled polygon
# def plot_filled_polygon(vertices, height, width):
#     scanlines = scanline_fill(vertices, height)

#     for y, pixels in scanlines.items():
#         for pixel in pixels:
#             plt.scatter(pixel, y, color='black')

# # Test the function
# vertices = np.array([[50, 50], [200, 150], [150, 250], [100, 200], [50, 50]])

# # Plotting the polygon and filled area
# plt.figure(figsize=(8, 6))
# plt.plot(vertices[:, 0], vertices[:, 1], 'b-', label='Polygon')
# plot_filled_polygon(vertices, 300, 300)
# plt.xlim(0, 300)
# plt.ylim(0, 300)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.legend()
# plt.title('Scan Line Fill Algorithm')
# plt.grid(True)
# plt.show()
