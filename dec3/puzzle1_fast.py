with open("dec3/input.txt", "r") as file:
    l1, l2 = file.readlines()
    l1 = l1.split(",")
    l2 = l2.split(",")

def plot(directions):
    lines = []
    curr = (0, 0)
    for p in directions:
        d, num = p[0], p[1:]
        num = int(num)
        if d == "R":
            lines.append((curr, (curr[0]+num, curr[1]), True))
            curr = (curr[0]+num, curr[1])
        elif d == "L":
            lines.append(((curr[0]-num, curr[1]), curr, True))
            curr = (curr[0]-num, curr[1])
        elif d == "U":
            lines.append(((curr[0], curr[1]-num), curr, False))
            curr = (curr[0], curr[1]-num)
        elif d == "D":
            lines.append((curr, (curr[0], curr[1]+num), False))
            curr = (curr[0], curr[1]+num)
    return lines

pts1, pts2 = plot(l1), plot(l2)
intersections = []
for line1 in pts1:
    for line2 in pts2:
        if set([line1[2], line2[2]]) == {True, False}:
            if line1[2] == True:
                if line1[0][0] < line2[0][0] < line1[1][0] and line2[0][1] < line1[0][1] < line2[1][1]:
                    intersections.append((line2[0][0], line1[0][1]))
            else:
                if line2[0][0] < line1[0][0] < line2[1][0] and line1[0][1] < line2[0][1] < line1[1][1]:
                    intersections.append((line1[0][0], line2[0][1]))

print(min(abs(x)+abs(y) for (x, y) in intersections))
