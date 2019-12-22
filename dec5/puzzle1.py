import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec5/input.txt", "r") as file:
    field = list(map(int, file.read().split(",")))

ic = IntCode(field)
ic.inp.append(1)
ic.start()
print(ic.out[-1])