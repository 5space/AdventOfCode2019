import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec13/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

ic = IntCode(memory)
ic.start()

k = [ic.out[i] for i in range(2, len(ic.out), 3)]

print(k.count(2))