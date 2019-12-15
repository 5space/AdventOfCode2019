import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode
from PIL import Image
import pygame
import imageio

screen = pygame.display.set_mode((440, 240))
clock = pygame.time.Clock()

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
joystick = 0
while True:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                joystick = 1
            elif event.key == pygame.K_LEFT:
                joystick = -1
        elif event.type == pygame.KEYUP and event.key in (pygame.K_RIGHT, pygame.K_LEFT):
            joystick = 0
    # if keys[pygame.K_RIGHT]:
    #     joystick = 1
    # elif keys[pygame.K_LEFT]:
    #     joystick = -1
    ic.start(inp=[joystick])
    if len(ic.out) == 0:
        break
    for i in range(0, len(ic.out), 3):
        x, y, tile = ic.out[i:i+3]
        if x == -1 and y == 0:
            print("score", tile)
        else:
            pixels[x, y] = colors[tile]
    img2 = img.resize((440, 240))
    images.append(img)
    raw_str = img2.tobytes("raw", "RGB")
    pg = pygame.image.fromstring(raw_str, (440, 240), "RGB")
    ic.out = []
    screen.blit(pg, (0, 0))
    pygame.display.flip()
    clock.tick(10)

imageio.mimsave("dec13/anim2.gif", images[::5], duration=0.03)
