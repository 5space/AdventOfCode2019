import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode
from PIL import Image
import pygame
import imageio

screen = pygame.display.set_mode((440, 240))

colors = {0: (0, 0, 0),
          1: (255, 255, 255),
          2: (255, 0, 0),
          3: (0, 255, 0),
          4: (0, 0, 255)}

with open("dec13/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))
memory[0] = 2

ic = IntCode(memory)
move = 0
ballpos = 0
paddlepos = 0

images = []

img = Image.new("RGB", (44, 24), (0, 0, 0))
img2 = img.resize((440, 240))
images.append(img)
pixels = img.load()
raw_str = img2.tobytes("raw", "RGB")
pg = pygame.image.fromstring(raw_str, (440, 240), "RGB")
while True:
    screen.fill((0, 0, 0))
    if ballpos < paddlepos:
        joystick = -1
    elif ballpos > paddlepos:
        joystick = 1
    else:
        joystick = 0
    ic.start(inp=[joystick])
    if len(ic.out) == 0:
        break
    for i in range(0, len(ic.out), 3):
        x, y, tile = ic.out[i:i+3]
        if x == -1 and y == 0:
            print("score", tile)
        else:
            if tile == 3:
                paddlepos = x
            elif tile == 4:
                ballpos = x
            pixels[x, y] = colors[tile]
    img2 = img.resize((440, 240))
    images.append(img)
    raw_str = img2.tobytes("raw", "RGB")
    pg = pygame.image.fromstring(raw_str, (440, 240), "RGB")
    ic.out = []
    screen.blit(pg, (0, 0))
    pygame.event.pump()
    if len(images) % 10 == 0:
        pygame.display.flip()

imageio.mimsave("dec13/anim2.gif", images[::5], duration=0.03)
