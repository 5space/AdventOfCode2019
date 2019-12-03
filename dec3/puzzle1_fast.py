with open("dec3/input.txt", "r") as file:
    l1, l2 = file.readlines()
    l1 = l1.split(",")
    l2 = l2.split(",")

def plot(directions):
    v, h = [], []
    curr = (0, 0)
    for p in directions:
        d, num = p[0], p[1:]
        num = int(num)
        if d == "R":
            h.append((curr, (curr[0]+num, curr[1])))  # (point1, point2, orientation)
            curr = (curr[0]+num, curr[1])
        elif d == "L":
            h.append(((curr[0]-num, curr[1]), curr))
            curr = (curr[0]-num, curr[1])
        elif d == "U":
            v.append(((curr[0], curr[1]-num), curr))
            curr = (curr[0], curr[1]-num)
        elif d == "D":
            v.append((curr, (curr[0], curr[1]+num)))
            curr = (curr[0], curr[1]+num)
    return (v, h)

pts1, pts2 = plot(l1), plot(l2)
intersections = []
for line1 in pts1[0]:
    for line2 in pts2[1]:
        if line2[0][0] < line1[0][0] < line2[1][0] and line1[0][1] < line2[0][1] < line1[1][1]:
            intersections.append((line1[0][0], line2[0][1]))
for line1 in pts2[0]:
    for line2 in pts1[1]:
        if line2[0][0] < line1[0][0] < line2[1][0] and line1[0][1] < line2[0][1] < line1[1][1]:
            intersections.append((line1[0][0], line2[0][1]))

print(min(abs(x)+abs(y) for (x, y) in intersections))
