import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy > dx
    if slope:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    y = y1
    y_step = 1 if y1 < y2 else -1
    D = 2 * dy - dx
    for x in range(x1, x2 + 1):
        if slope:
            points.append((y, x))
        else:
            points.append((x, y))
        if D >= 0:
            y += y_step
            D -= 2 * dx
        D += 2 * dy
    return points

# Example usage
x1, y1 = 1, 1
x2, y2 = 8, 5

points = draw_line(x1, y1, x2, y2)

x_values, y_values = zip(*points)

# Plotting the line
plt.plot(x_values, y_values, marker='o')
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
