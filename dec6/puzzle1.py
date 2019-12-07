import time

start = time.time()
with open("dec6/input.txt", "r") as file:
    lines = file.readlines()
    split = [line.strip().split(")") for line in lines]
    data = {b: a for (a, b) in split}

c = 0
for node in data:
    while node in data:
        node = data[node]
        c += 1
print(c)
print(time.time()-start)
