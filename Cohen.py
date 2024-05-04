import matplotlib.pyplot as plt

# Global Variables
xmin, xmax, ymin, ymax = 0, 0, 0, 0

# Lines where co-ordinates are (x1, y1) and (x2, y2)
class Lines:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

# This will return the sign required.
def sign(x):
    if x > 0:
        return 1
    else:
        return 0

# CohenSutherLand LineClipping Algorithm As Described in theory.
# This will clip the lines as per window boundaries.
def clip(mylines):
    global xmin, xmax, ymin, ymax
    # arrays will store bits
    # Here bits implies initial Point whereas byte implies end points
    bits = [0]*4
    byte = [0]*4

    # Finding Bits
    bits[0] = sign(xmin - mylines.x1)
    byte[0] = sign(xmin - mylines.x2)
    bits[1] = sign(mylines.x1 - xmax)
    byte[1] = sign(mylines.x2 - xmax)
    bits[2] = sign(ymin - mylines.y1)
    byte[2] = sign(ymin - mylines.y2)
    bits[3] = sign(mylines.y1 - ymax)
    byte[3] = sign(mylines.y2 - ymax)

    # initial will used for initial coordinates and end for final
    initial = "".join(map(str, bits))
    end = "".join(map(str, byte))
    temp = ""

    # finding slope of line y=mx+c as (y-y1)=m(x-x1)+c
    # where m is slope m=dy/dx;
    m = (mylines.y2 - mylines.y1) / (mylines.x2 - mylines.x1)
    c = mylines.y1 - m * mylines.x1

    # if both points are inside the Accept the line and draw
    if initial == end and end == "0000":
        # plotting the line from (x1, y1) to (x2, y2)
        plt.plot([mylines.x1, mylines.x2], [mylines.y1, mylines.y2], color='red')
        return

    # this will contain cases where line maybe totally outside for partially inside
    else:
        # taking bitwise end of every value
        for i in range(4):
            val = bits[i] & byte[i]
            if val == 0:
                temp += '0'
            else:
                temp += '1'
        # as per algo if AND is not 0000 means line is completely outside hence draw nothing and return
        if temp != "0000":
            return

        # Here contain cases of partial inside or outside
        # So check for every boundary one by one
        for i in range(4):
            # if both bit are same hence we cannot find any intersection with boundary so continue
            if bits[i] == byte[i]:
                continue
            # Otherwise there exist an intersection

            # Case when initial point is in left xmin
            if i == 0 and bits[i] == 1:
                var = round(m * xmin + c)
                mylines.y1 = var
                mylines.x1 = xmin
            # Case when final point is in left xmin
            if i == 0 and byte[i] == 1:
                var = round(m * xmin + c)
                mylines.y2 = var
                mylines.x2 = xmin
            # Case when initial point is in right of xmax
            if i == 1 and bits[i] == 1:
                var = round(m * xmax + c)
                mylines.y1 = var
                mylines.x1 = xmax
            # Case when final point is in right of xmax
            if i == 1 and byte[i] == 1:
                var = round(m * xmax + c)
                mylines.y2 = var
                mylines.x2 = xmax
            # Case when initial point is in top of ymin
            if i == 2 and bits[i] == 1:
                var = round((ymin - c) / m)
                mylines.y1 = ymin
                mylines.x1 = var
            # Case when final point is in top of ymin
            if i == 2 and byte[i] == 1:
                var = round((ymin - c) / m)
                mylines.y2 = ymin
                mylines.x2 = var
            # Case when initial point is in bottom of ymax
            if i == 3 and bits[i] == 1:
                var = round((ymax - c) / m)
                mylines.y1 = ymax
                mylines.x1 = var
            # Case when final point is in bottom of ymax
            if i == 3 and byte[i] == 1:
                var = round((ymax - c) / m)
                mylines.y2 = ymax
                mylines.x2 = var
            # Updating Bits at every point
            bits[0] = sign(xmin - mylines.x1)
            byte[0] = sign(xmin - mylines.x2)
            bits[1] = sign(mylines.x1 - xmax)
            byte[1] = sign(mylines.x2 - xmax)
            bits[2] = sign(ymin - mylines.y1)
            byte[2] = sign(ymin - mylines.y2)
            bits[3] = sign(mylines.y1 - ymax)
            byte[3] = sign(mylines.y2 - ymax)

        # If now both points lie inside or on boundary then simply draw the updated line
        if initial == end and end == "0000":
            plt.plot([mylines.x1, mylines.x2], [mylines.y1, mylines.y2], color='red')
            return
        # else line was completely outside hence rejected
        else:
            return

# Driver Function
def main():
    global xmin, xmax, ymin, ymax

    # Setting values of Clipping window
    xmin = 40
    xmax = 100
    ymin = 40
    ymax = 80

    # Drawing Window using Lines
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], color='black')

    # Assume 4 lines to be clipped
    mylines = []

    # Setting the coordinates of 4 lines
    mylines.append(Lines(30, 65, 55, 30))
    mylines.append(Lines(60, 20, 100, 90))
    mylines.append(Lines(60, 100, 80, 70))
    mylines.append(Lines(85, 50, 120, 75))

    # Drawing Initial Lines without clipping
    for line in mylines:
        plt.plot([line.x1, line.x2], [line.y1, line.y2], color='blue')
        plt.pause(1)

    # Drawing clipped Line
    for line in mylines:
        # Calling clip() which in term clip the line as per window and draw it
        clip(line)
        plt.pause(1)

    plt.show()

if __name__ == "__main__":
    main()