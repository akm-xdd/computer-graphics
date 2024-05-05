import matplotlib.pyplot as plt


def draw_line(x1, y1, x2, y2):
    points = []
    direction_steps = [(x1,x2)]  # List to store the direction of each step
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
        # Track the direction based on y change
        if D >= 0:
            direction_steps.append("NE")
            y += y_step
            D -= 2 * dx
        else:
            direction_steps.append("E")
        D += 2 * dy
    return points, direction_steps


# Example usage
x1, y1 = 2, 3
x2, y2 = 8, 11

points, directions = draw_line(x1, y1, x2, y2)

x_values, y_values = zip(*points)

# Plotting the line
plt.plot(x_values, y_values, marker='o')
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
for point, direction in zip(points[1:], directions[1:]):
    print(f"Point: {point} - Direction: {direction}")


plt.show()
