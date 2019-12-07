import sys, os, time
sys.path.append(os.getcwd())
from util.intcode import IntCode

start = time.time()
with open("dec2/input.txt", "r") as file:
    f = list(map(int, file.read().split(",")))

for n in range(100):
    for v in range(100):
        field = f.copy()
        field[1] = n
        field[2] = v
        ic = IntCode(field)
        ic.start()
        if ic.memory[0] == 19690720:
            print(n, v)
print(time.time()-start)
