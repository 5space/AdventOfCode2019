import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec19/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

def test(x, y):
    if x < 0 or y < 0:
        return False
    ic = IntCode(memory.copy())
    ic.inp += [x, y]
    ic.start()
    out = ic.popout()
    return out[0] == 1

size = 99
pos = [10, 0]
while True:
    if test(pos[0], pos[1]):  # check one corner
        if test(pos[0]-size, pos[1]+size):  # check opposite corner
            print(10000*(pos[0]-size) + pos[1])
            break
        pos[0] += 1
    else:
        pos[1] += 1
