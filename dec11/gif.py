import sys, os, imageio, colorsys
sys.path.append(os.getcwd())
from util.intcode import IntCode
from PIL import Image

with open("dec11/input2.txt", "r") as file:
    field = list(map(int, file.read().split(",")))

ic = IntCode(field)
# grid = {(0, 0): 1}
grid = {}
x, y = 0, 0
d = 0

# minx = min(g[0] for g in grid.keys())
# miny = min(g[1] for g in grid.keys())
# maxx = max(g[0] for g in grid.keys())
# maxy = max(g[1] for g in grid.keys())
# minx = -40
# miny = -74
# maxx = 31
# maxy = 13
minx = -28
miny = -24
maxx = 50
maxy = 25

images = []
steps = 0
hue = 0
while True:
    if (x, y) in grid and grid[x, y] != 0:
        color = 1
    else:
        color = 0
    ic.start(inp=[color])
    if len(ic.out) < 2:
        break
    newcolor, direction = ic.out
    ic.out = []
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    if newcolor == 0:
        grid[x, y] = 0
    else:
        grid[x, y] = (int(255*r), int(255*g), int(255*b))
    hue = (hue + 0.0001) % 1
    if direction == 0:
        d = (d-1)%4
    else:
        d = (d+1)%4
    
    if d == 0: y -= 1
    elif d == 1: x += 1
    elif d == 2: y += 1
    else: x -= 1

    steps += 1
    if steps % 30 == 0:
        image = Image.new("RGB", (maxx-minx, maxy-miny), (0, 0, 0))
        pixels = image.load()
        for x2 in range(minx, maxx):
            for y2 in range(miny, maxy):
                if (x2, y2) in grid and grid[x2, y2] != 0:
                    pixels[x2-minx,y2-miny] = grid[x2, y2]
        image = image.resize((image.width*2, image.height*2))
        image.save("dec11/image.png")
        images.append(imageio.imread("dec11/image.png"))
    if len(grid) % 100 == 0:
        print(len(grid), steps, len(images))
for _ in range(100):
    images.append(image)
imageio.mimsave("dec11/anim2.gif", images, duration=0.03)

minx = min(g[0] for g in grid.keys())
miny = min(g[1] for g in grid.keys())
maxx = max(g[0] for g in grid.keys())
maxy = max(g[1] for g in grid.keys())
print(minx, miny, maxx, maxy)
