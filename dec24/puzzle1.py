with open("dec24/input.txt", "r") as file:
    layout = [[c == "#" for c in line.strip()] for line in file.readlines()]
    WIDTH, HEIGHT = len(layout[0]), len(layout)

NEIGHBORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_num_neighbors(layout, x, y):
    count = 0
    for n in NEIGHBORS:
        newx, newy = x+n[0], y+n[1]
        if 0 <= newx < WIDTH and 0 <= newy < HEIGHT and layout[newy][newx]:
            count += 1
    return count

def iterate(layout):
    new = [p.copy() for p in layout]
    for x in range(WIDTH):
        for y in range(HEIGHT):
            value = layout[y][x]
            neighbors = get_num_neighbors(layout, x, y)
            if value and neighbors != 1:
                new[y][x] = False
            elif not value and 0 < neighbors < 3:
                new[y][x] = True
    return new

def rating(layout):
    rating = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if layout[y][x]:
                power = WIDTH*y + x
                rating += 2**power
    return rating

memory = set()
curr_layout = layout
while rating(curr_layout) not in memory:
    memory.add(rating(curr_layout))
    curr_layout = iterate(curr_layout)

print(rating(curr_layout))