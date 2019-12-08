from PIL import Image

with open("dec8/input.txt", "r") as file:
    k = list(map(int, list(file.read().strip())))

layers = []
for n in range(0, len(k), 25*6):
    p = k[n:n+150]
    layers.append([p[:25], p[25:50], p[50:75], p[75:100], p[100:125], p[125:150]])

layers = layers[::-1]
image = Image.new("RGBA", (25, 6))
pixels = image.load()
for l in layers:
    for x in range(25):
        for y in range(6):
            if l[y][x] == 1:
                pixels[x,y] = (255, 255, 255)
            elif l[y][x] == 0:
                pixels[x,y] = (0, 0, 0)
image.show()