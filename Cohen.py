import matplotlib.pyplot as plt

# Cohen-Sutherland line clipping algorithm


def cohen_sutherland_clip(line, clip_window):
    def compute_outcode(point, clip_window):
        x, y = point
        code = 0
        if x < clip_window[0]:
            code |= 1  # to the left of clip window
        elif x > clip_window[1]:
            code |= 2  # to the right of clip window
        if y < clip_window[2]:
            code |= 4  # below clip window
        elif y > clip_window[3]:
            code |= 8  # above clip window
        return code

    x1, y1, x2, y2 = line
    code1 = compute_outcode((x1, y1), clip_window)
    code2 = compute_outcode((x2, y2), clip_window)

    while True:
        if code1 == 0 and code2 == 0:
            # Both endpoints inside the clip window
            return [(x1, y1), (x2, y2)]
        elif code1 & code2 != 0:
            # Both endpoints are outside the same region
            return None
        else:
            # Calculate intersection with clip window
            code_outside = code1 if code1 != 0 else code2
            if code_outside & 1:
                x = clip_window[0]
                y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            elif code_outside & 2:
                x = clip_window[1]
                y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            elif code_outside & 4:
                y = clip_window[2]
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            elif code_outside & 8:
                y = clip_window[3]
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

            if code_outside == code1:
                x1, y1 = x, y
                code1 = compute_outcode((x1, y1), clip_window)
            else:
                x2, y2 = x, y
                code2 = compute_outcode((x2, y2), clip_window)

# Main function


# Define line and clipping window
line = (50, 100, 300, 200)  # (x1, y1, x2, y2)
clip_window = (100, 250, 150, 300)  # (x_min, x_max, y_min, y_max)

# Clip line
clipped_line = cohen_sutherland_clip(line, clip_window)
print("Clipped Line:", clipped_line)

# Plotting
fig, ax = plt.subplots()

# Plot clip window
ax.plot([clip_window[0], clip_window[1], clip_window[1], clip_window[0], clip_window[0]],
        [clip_window[2], clip_window[2], clip_window[3],
            clip_window[3], clip_window[2]],
        'g-', label='Clip Window')

# Plot original line
ax.plot([line[0], line[2]], [line[1], line[3]], 'b-', label='Original Line')

# Plot clipped line if it exists
if clipped_line:
    ax.plot([clipped_line[0][0], clipped_line[1][0]], [clipped_line[0][1], clipped_line[1][1]],
            'r-', label='Clipped Line')

ax.set_xlim(0, 400)
ax.set_ylim(0, 400)
ax.legend()
plt.show()
