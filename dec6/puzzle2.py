import time

start = time.time()
with open("dec6/input.txt", "r") as file:
    lines = file.readlines()
    split = [line.strip().split(")") for line in lines]
    data = {b: a for (a, b) in split}

c = 0
source, destination = data["YOU"], data["SAN"]
source_path = []
n = source
while n in data:
    n = data[n]
    source_path.append(n)
    c += 1
c = 0
n = destination
while n in data:
    n = data[n]
    c += 1
    if n in source_path:
        print(c + source_path.index(n) + 1)
        break
print(time.time()-start)
