import matplotlib.pyplot as plt

def sutherland_hodgman_clip(polygon, clip_window):
    def inside(point, clip_edge):
        x, y = point
        xmin, xmax, ymin, ymax = clip_edge
        if xmin == xmax:  # Vertical edge
            return x >= xmin if xmin == clip_edge[0] else x <= xmax
        else:  # Horizontal edge
            return y >= ymin if ymin == clip_edge[2] else y <= ymax

    def intersect(p1, p2, clip_edge):
        x1, y1 = p1
        x2, y2 = p2
        xmin, xmax, ymin, ymax = clip_edge
        dx = x2 - x1
        dy = y2 - y1

        if dx == 0 and dy == 0:
            return None  # p1 and p2 are the same point, thus no intersection

        if xmin == xmax:  # Vertical clip edge
            x = xmin
            if dx == 0:
                return None  # Line is parallel to the clipping edge
            y = y1 + dy * (x - x1) / dx
            if y < ymin or y > ymax:
                return None
        else:  # Horizontal clip edge
            y = ymin
            if dy == 0:
                return None  # Line is parallel to the clipping edge
            x = x1 + dx * (y - y1) / dy
            if x < xmin or x > xmax:
                return None

        return (x, y)

    def clip_polygon(polygon, clip_edge):
        clipped_polygon = []
        prev_point = polygon[-1]
        prev_inside = inside(prev_point, clip_edge)

        for current_point in polygon:
            current_inside = inside(current_point, clip_edge)
            if current_inside:
                if not prev_inside:
                    intersection_point = intersect(prev_point, current_point, clip_edge)
                    if intersection_point:
                        clipped_polygon.append(intersection_point)
                clipped_polygon.append(current_point)
            elif prev_inside:
                intersection_point = intersect(prev_point, current_point, clip_edge)
                if intersection_point:
                    clipped_polygon.append(intersection_point)
            prev_point = current_point
            prev_inside = current_inside

        return clipped_polygon

    xmin, xmax, ymin, ymax = clip_window
    clip_edges = [
        (xmin, xmin, ymin, ymax),  # Left
        (xmax, xmax, ymin, ymax),  # Right
        (xmin, xmax, ymin, ymin),  # Bottom
        (xmin, xmax, ymax, ymax)  # Top
    ]

    clipped_polygon = polygon[:]
    for edge in clip_edges:
        clipped_polygon = clip_polygon(clipped_polygon, edge)
        if not clipped_polygon:
            return []

    return clipped_polygon

# Define a triangle and the clipping window
# triangle= [(50, 50), (300, 50), (175, 275)]
triangle= [(110, 125), (125, 200), (225,110)]
clip_window = (100, 250, 100, 250)  # (xmin, xmax, ymin, ymax)

# Clip the triangle
clipped_triangle = sutherland_hodgman_clip(triangle, clip_window)

# Plotting
fig, ax = plt.subplots()

# Draw the clip window with a green line
clip_path = [(clip_window[0], clip_window[2]), (clip_window[1], clip_window[2]), (clip_window[1], clip_window[3]), (clip_window[0], clip_window[3]), (clip_window[0], clip_window[2])]
ax.plot([p[0] for p in clip_path], [p[1] for p in clip_path], 'g-', label='Clip Window', linewidth=2)

# Draw the original triangle with blue lines
original_path = triangle + [triangle[0]]
ax.plot([p[0] for p in original_path], [p[1] for p in original_path], 'b-', label='Original Triangle', linewidth=1)

# Draw the clipped triangle with red lines
if clipped_triangle:
    clipped_path = clipped_triangle + [clipped_triangle[0]]
    ax.plot([p[0] for p in clipped_path], [p[1] for p in clipped_path], 'r-', label='Clipped Triangle', linewidth=2)

# Set plot limits and show legend
ax.set_xlim(0, 350)
ax.set_ylim(0, 300)
ax.legend()
plt.show()
