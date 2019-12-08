with open("dec8/input.txt", "r") as file:
    k = list(map(int, list(file.read().strip())))

layers = [k[n:n+150] for n in range(0, len(k), 150)]
zeroes = 100
product = 0
for l in layers:
    z = l.count(0)
    if z < zeroes:
        zeroes = z
        product = l.count(1)*l.count(2)
print(product)