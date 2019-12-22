import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec19/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

count = 0
for y in range(50):
    line = ""
    for x in range(50):
        ic = IntCode(memory)
        ic.inp += [x, y]
        ic.start()
        out = ic.popout()
        if out[0] == 1:
            count += 1
            line += "#"
        else:
            line += "."
    print(line)
print(count)