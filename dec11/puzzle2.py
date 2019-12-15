import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode
from PIL import Image

with open("dec11/input2.txt", "r") as file:
    field = list(map(int, file.read().split(",")))

ic = IntCode(field)
grid = {(0, 0): 1}
x, y = 0, 0
d = 0

while True:
    if (x, y) in grid:
        color = grid[x, y]
    else:
        color = 0
    ic.start(inp=[color])
    if len(ic.out) < 2:
        break
    newcolor, direction = ic.out
    ic.out = []
    grid[x, y] = newcolor
    if direction == 0:
        d = (d-1)%4
    else:
        d = (d+1)%4
    
    if d == 0: y -= 1
    elif d == 1: x += 1
    elif d == 2: y += 1
    else: x -= 1

minx = min(g[0] for g in grid.keys())
miny = min(g[1] for g in grid.keys())
maxx = max(g[0] for g in grid.keys())
maxy = max(g[1] for g in grid.keys())

img = Image.new("RGB", (maxx-minx+1, maxy-miny+1))
pixels = img.load()
for k in grid.keys():
    if grid[k] == 1:
        pixels[k[0]-minx,k[1]-miny] = (255, 255, 255)

img.show()