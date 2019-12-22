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


minx = -20
miny = -20
maxx = 18
maxy = 18

images = []
frame = 1
while True:
    ic.start(inp=[direction])
    out = ic.out[0]
    ic.out = []
    dx, dy = directions[direction]
    if out != 0:
        position = (position[0]+dx, position[1]+dy)
    if position not in data:
        data[position] = out
    if out == 0:
        direction = order[(order.index(direction) + 1) % 4]
    else:
        direction = order[(order.index(direction) - 1) % 4]
    img = Image.new("RGB", (maxx-minx+1, maxy-miny+1), (255, 255, 255))
    pixels = img.load()
    for k, v in data.items():
        x, y = k
        if k == position:
            pixels[x-minx, y-miny] = (0, 0, 255)
        elif v == 1:
            pixels[x-minx, y-miny] = (0, 0, 0)
        elif v == 2:
            pixels[x-minx, y-miny] = (255, 0, 0)
        elif v == 3:
            pixels[x-minx, y-miny] = (0, 255, 0)
    img = img.resize((456, 456))
    img.save(f"img{frame}.png", "PNG")
    frame += 1
    images.append(img)
    print(len(images), len(data))
    if len(data) == 799:
        break
