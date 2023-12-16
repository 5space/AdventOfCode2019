layers = [[[False for _ in range(5)] for _ in range(5)] for _ in range(400)]
offset = 200
with open("dec24/input.txt", "r") as file:
    for y, line in enumerate(file.readlines()):
        for x, c in enumerate(line.strip()):
            if c == "#":
                layers[offset][y][x] = True

NEIGHBORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_neighbors(pos):
    x, y, level = pos
    final = []
    for n in NEIGHBORS:
        newx, newy = x + n[0], y + n[1]
        if newx < 0:
            final.append((1, 2, level-1))
        elif newx >= 5:
            final.append((3, 2, level-1))
        elif newy < 0:
            final.append((2, 1, level-1))
        elif newy >= 5:
            final.append((2, 3, level-1))
        elif newx == 2 and newy == 2:
            if n[0] == 1:
                for i in range(5):
                    final.append((0, i, level+1))
            elif n[0] == -1:
                for i in range(5):
                    final.append((4, i, level+1))
            elif n[1] == 1:
                for i in range(5):
                    final.append((i, 0, level+1))
            elif n[1] == -1:
                for i in range(5):
                    final.append((i, 4, level+1))
        else:
            final.append((newx, newy, level))
    return final

def get_num_neighbors(pos):
    count = 0
    for x, y, level in get_neighbors(pos):
        if 0 <= level < 400 and 0 <= x < 5 and 0 <= y < 5 and layers[level][y][x]:
            count += 1
    return count

def iterate():
    global layers
    new_layers = layers.copy()
    for level in range(400):
        for y in range(5):
            for x in range(5):
                value = layers[level][y][x]
                neighbors = get_num_neighbors((x, y, level))
                if value and neighbors != 1:
                    new_layers[level][y][x] = False
                elif not value and 0 < neighbors < 3:
                    new_layers[level][y][x] = True
    layers = new_layers

def num_bugs():
    return sum(layers[level][y].count(True) for y in range(5) for level in range(400))

for i in range(200):
    print(i, num_bugs())
    iterate()

print(num_bugs())