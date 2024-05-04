import numpy as np
import matplotlib.pyplot as plt

# Defining maximum number of points in polygon
MAX_POINTS = 20

# Function to return x-value of point of intersection of two lines
def x_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

# Function to return y-value of point of intersection of two lines
def y_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

# Function to clip all the edges w.r.t one clip edge of clipping area
def clip(poly_points, poly_size, x1, y1, x2, y2):
    new_points = np.zeros((MAX_POINTS, 2), dtype=int)
    new_poly_size = 0

    # (ix,iy),(kx,ky) are the co-ordinate values of the points
    for i in range(poly_size):
        # i and k form a line in polygon
        k = (i+1) % poly_size
        ix, iy = poly_points[i]
        kx, ky = poly_points[k]

        # Calculating position of first point w.r.t. clipper line
        i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)

        # Calculating position of second point w.r.t. clipper line
        k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)

        # Case 1 : When both points are inside
        if i_pos < 0 and k_pos < 0:
            # Only second point is added
            new_points[new_poly_size] = [kx, ky]
            new_poly_size += 1

        # Case 2: When only first point is outside
        elif i_pos >= 0 and k_pos < 0:
            # Point of intersection with edge and the second point is added
            new_points[new_poly_size] = [x_intersect(x1, y1, x2, y2, ix, iy, kx, ky),
                                         y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)]
            new_poly_size += 1
            new_points[new_poly_size] = [kx, ky]
            new_poly_size += 1

        # Case 3: When only second point is outside
        elif i_pos < 0 and k_pos >= 0:
            # Only point of intersection with edge is added
            new_points[new_poly_size] = [x_intersect(x1, y1, x2, y2, ix, iy, kx, ky),
                                         y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)]
            new_poly_size += 1

        # Case 4: When both points are outside
        else:
            pass  # No points are added, but we add a pass statement to avoid the IndentationError

    # Copying new points into a separate array and changing the no. of vertices
    clipped_poly_points = np.zeros((new_poly_size, 2), dtype=int)
    for i in range(new_poly_size):
        clipped_poly_points[i] = new_points[i]

    return clipped_poly_points, new_poly_size

# Function to implement Sutherland–Hodgman algorithm
def suthHodgClip(poly_points, poly_size, clipper_points, clipper_size):
    # i and k are two consecutive indexes
    for i in range(clipper_size):
        k = (i+1) % clipper_size

        # We pass the current array of vertices, it's size and the end points of the selected clipper line
        poly_points, poly_size = clip(poly_points, poly_size, clipper_points[i][0],
                                      clipper_points[i][1], clipper_points[k][0],
                                      clipper_points[k][1])

    # Return the clipped polygon points
    return poly_points, poly_size

# Driver code
if __name__ == "__main__":
    # Defining polygon vertices in clockwise order
    poly_size = 3
    poly_points = np.array([[100, 150], [200, 250], [300, 200]])

    # Defining clipper polygon vertices in clockwise order
    clipper_size = 4
    clipper_points = np.array([[150, 150], [150, 200], [200, 200], [200, 150]])

    # Calling the clipping function
    clipped_polygon, clipped_size = suthHodgClip(poly_points, poly_size, clipper_points, clipper_size)

    # Plotting the original and clipped polygons
    plt.plot(poly_points[:, 0], poly_points[:, 1], 'b-', label='Original Polygon')
    plt.plot(clipper_points[:, 0], clipper_points[:, 1], 'g-', label='Clipper Polygon')
    plt.plot(clipped_polygon[:clipped_size, 0], clipped_polygon[:clipped_size, 1], 'r-', label='Clipped Polygon')
    plt.xlim(0, 400)
    plt.ylim(0, 300)
    plt.legend()
    plt.title('Sutherland-Hodgman Polygon Clipping')
    plt.grid(True)
    plt.show()
