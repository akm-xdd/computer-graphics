import matplotlib.pyplot as plt

def draw_circle(radius):
    x = 0
    y = radius
    d = 1 - radius
    points = []
    
    while x <= y:
        # Append points for all eight octants
        points.append((x, y))
        points.append((y, x))
        points.append((-x, y))
        points.append((-y, x))
        points.append((-x, -y))
        points.append((-y, -x))
        points.append((x, -y))
        points.append((y, -x))
        
        # Decision to either move directly east or south-east
        if d < 0:
            # Mid-point is inside the circle
            d += 2 * x + 3
        else:
            # Mid-point is outside or on the circle
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    
    return points

# Example usage
radius = 20  # Increased radius for better visualization
points = draw_circle(radius)

# Unzip the points to get x and y coordinates separately
x_values, y_values = zip(*points)

# Plotting
plt.figure(figsize=(8, 8))  # Make the figure size larger to see the circle clearly
plt.scatter(x_values, y_values, marker='o')
plt.gca().set_aspect('equal', adjustable='box')  # Ensure the aspect ratio is equal to make the circle round
plt.title("Mid-Point Circle Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
