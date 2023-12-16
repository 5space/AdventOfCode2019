layout = set()
with open("dec24/input.txt", "r") as file:
    for y, line in enumerate(file.readlines()):
        for x, c in enumerate(line.strip()):
            if c == "#":
                layout.add((x, y, 0))

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

def get_all_neighbors():
    final = set()
    for pos in layout:
        final = final.union(set(get_neighbors(pos)))
    return final

def get_num_neighbors(pos):
    count = 0
    for n in get_neighbors(pos):
        if n in layout:
            count += 1
    return count

def iterate():
    global layout
    new_layout = layout.copy()
    for pos in layout:
        neighbors = get_num_neighbors(pos)
        if neighbors != 1:
            new_layout.remove(pos)
    for pos in get_all_neighbors():
        if pos in layout:
            continue
        neighbors = get_num_neighbors(pos)
        if 0 < neighbors < 3:
            new_layout.add(pos)
    layout = new_layout

def display():
    for i in range(-5, 6):
        print("Depth", i)
        for y in range(5):
            e = []
            for x in range(5):
                if (x, y, i) in layout:
                    e.append("#")
                else:
                    e.append(".")
            print("".join(e))
        print()

for i in range(200):
    print(i, len(layout))
    iterate()

print(len(layout))