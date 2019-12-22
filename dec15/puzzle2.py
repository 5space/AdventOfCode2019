import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode
from PIL import Image

with open("dec15/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

ic = IntCode(memory.copy())
direction = 2
position = (0, 0)
order = [2, 4, 1, 3]
directions = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}

data = {(0, 0): 3}
source = (0, 0)

while True:
    ic.start(inp=[direction])
    out = ic.out[0]
    ic.out = []
    dx, dy = directions[direction]
    if out != 0:
        position = (position[0]+dx, position[1]+dy)
    if out == 2:
        source = position
    if position not in data:
        data[position] = out
    if out == 0:
        direction = order[(order.index(direction) + 1) % 4]
    else:
        direction = order[(order.index(direction) - 1) % 4]
    if len(data) == 799:
        break

oxygenated = [source]
t = 0
while len(data.keys()) != len(oxygenated):
    to_add = []
    for node in oxygenated:
        for x, y in directions.values():
            pos = (node[0]+x, node[1]+y)
            if pos in data and pos not in oxygenated:
                to_add.append(pos)
    oxygenated += to_add
    t += 1
print(t)
    