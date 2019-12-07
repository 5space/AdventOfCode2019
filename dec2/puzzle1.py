import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec2/input.txt", "r") as file:
    field = list(map(int, file.read().split(",")))
field[1] = 12
field[2] = 2

ic = IntCode(field)
ic.start()
print(ic.memory[0])
