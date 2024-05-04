import matplotlib.pyplot as plt

def draw_circle(radius):
    x = 0
    y = radius
    d = 1 - radius
    points = []
    
    while x <= y:
        points.append((x, y))
        points.append((y, x))
        points.append((-x, y))
        points.append((-y, x))
        points.append((-x, -y))
        points.append((-y, -x))
        points.append((x, -y))
        points.append((y, -x))
        
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    
    return points

# Example usage
radius = 3
points = draw_circle(radius)

# Unzip the points to get x and y coordinates separately
x_values, y_values = zip(*points)

# Plotting
plt.scatter(x_values, y_values)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Mid-Point Circle Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
