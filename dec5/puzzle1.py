import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec5/input.txt", "r") as file:
    field = list(map(int, file.read().split(",")))

ic = IntCode(field)
f = ic.start([1])
print(f[-1])