import time
from matplotlib import pyplot as plt

with open("dec3/input.txt", "r") as file:
    l1, l2 = file.readlines()
    l1 = l1.split(",")
    l2 = l2.split(",")

def plot(directions):
    points = [(0, 0)]
    curr = [0, 0]
    for p in directions:
        d, num = p[0], p[1:]
        num = int(num)
        if d == "R":
            for a in range(1, num+1):
                points.append((curr[0]+a, curr[1]))
            curr[0] += num
        elif d == "L":
            for a in range(1, num+1):
                points.append((curr[0]-a, curr[1]))
            curr[0] -= num
        elif d == "U":
            for a in range(1, num+1):
                points.append((curr[0], curr[1]-a))
            curr[1] -= num
        elif d == "D":
            for a in range(1, num+1):
                points.append((curr[0], curr[1]+a))
            curr[1] += num
    return points

start = time.time()

pts1, pts2 = plot(l1), plot(l2)
plt.plot([x[0] for x in pts1], [x[1] for x in pts1])
plt.plot([x[0] for x in pts2], [x[1] for x in pts2])
plt.show()

print(time.time()-start)