from math import gcd

moons = [[-13, 14, -7, 0, 0, 0],
         [-18, 9, 0, 0, 0, 0],
         [0, -3, -3, 0, 0, 0],
         [-15, 3, -13, 0, 0, 0]]
# moons = [[-1, 0, 2, 0, 0, 0],
#          [2, -10, -7, 0, 0, 0],
#          [4, -8, 8, 0, 0, 0],
#          [3, 5, -1, 0, 0, 0]]

def lcm(x, y, z):
    p = int(x*y/gcd(x, y))
    return int(p*z/gcd(p, z))

totalsteps = []
for dim in range(3):
    start = []
    for m in moons:
        start += [m[dim], m[dim+3]]
    steps = 0
    while True:
        for i1 in range(4):
            for i2 in range(i1, 4):
                if moons[i1][dim] > moons[i2][dim]:
                    moons[i1][dim+3] -= 1
                    moons[i2][dim+3] += 1
                elif moons[i1][dim] < moons[i2][dim]:
                    moons[i1][dim+3] += 1
                    moons[i2][dim+3] -= 1
        for m in moons:
            m[dim] += m[dim+3]
        new = []
        for m in moons:
            new += [m[dim], m[dim+3]]
        steps += 1
        if new == start:
            break
    totalsteps.append(steps)
    print(steps)

print(lcm(*totalsteps))

