from math import atan2

with open("dec10/input.txt", "r") as file:
    arr = list(map(lambda x: x.strip(), file.readlines()))

WIDTH = len(arr[0])
HEIGHT = len(arr)

asteroids = [(x, y) for x in range(WIDTH) for y in range(HEIGHT) if arr[y][x] == "#"]
maximum = 0
location = (0, 0)
for a in asteroids:
    unique = set()
    for b in asteroids:
        if a != b:
            diffx = b[0]-a[0]
            diffy = b[1]-a[1]
            unique.add(atan2(diffy, diffx))
    if len(unique) > maximum:
        maximum = len(unique)
        location = a

print(maximum, location)
