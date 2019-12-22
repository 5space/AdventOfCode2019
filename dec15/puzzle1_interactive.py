import sys, os, pygame
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

screen = pygame.display.set_mode((430, 430))
clock = pygame.time.Clock()

minx = -22
miny = -22
maxx = 20
maxy = 20

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN):
            if event.key == pygame.K_RIGHT:
                direction = 4
            elif event.key == pygame.K_LEFT:
                direction = 3
            elif event.key == pygame.K_UP:
                direction = 1
            else:
                direction = 2
            
            ic.start(inp=[direction])
            out = ic.out[0]
            ic.out = []
            dx, dy = directions[direction]
            data[(position[0]+dx, position[1]+dy)] = out
            if out != 0:
                position = (position[0]+dx, position[1]+dy)
    
            img = Image.new("RGB", (maxx-minx+1, maxy-miny+1), (192, 192, 192))
            pixels = img.load()
            for k, v in data.items():
                x, y = k
                if k == position:
                    pixels[x-minx, y-miny] = (0, 0, 255)
                elif v == 0:
                    pixels[x-minx, y-miny] = (255, 255, 255)
                elif v == 1:
                    pixels[x-minx, y-miny] = (0, 0, 0)
                elif v == 2:
                    pixels[x-minx, y-miny] = (255, 0, 0)
                elif v == 3:
                    pixels[x-minx, y-miny] = (0, 255, 0)
            img = img.resize((430, 430))
            raw_str = img.tobytes("raw", "RGB")
            pg = pygame.image.fromstring(raw_str, (430, 430), "RGB")
            screen.blit(pg, (0, 0))
        elif event.type == pygame.QUIT:
            done = True
            break
    
    pygame.display.flip()
    clock.tick(60)
