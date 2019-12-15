from math import atan2, pi

with open("dec10/input.txt", "r") as file:
    arr = list(map(lambda x: x.strip(), file.readlines()))

WIDTH = len(arr[0])
HEIGHT = len(arr)

asteroids = [(x, y) for x in range(WIDTH) for y in range(HEIGHT) if arr[y][x] == "#"]
a = (20, 18)
unique = {}
for b in asteroids:
    if a != b:
        diff = (b[0]-a[0], b[1]-a[1])
        angle = (atan2(diff[1], diff[0])+pi/2) % (2*pi)
        if angle not in unique or abs(unique[angle][0]) > abs(diff[0]) or abs(unique[angle][1]) > abs(diff[1]):
            unique[angle] = diff

by_angle = sorted(list(unique.items()), key=lambda x: x[0])
print([(k[0]+a[0], k[1]+a[1]) for _, k in by_angle])
a2 = by_angle[199][1]
print((a2[0]+a[0])*100+(a2[1]+a[1]))
