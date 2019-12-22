import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec21/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))


with open("dec21/instructions2.txt", "r") as ins:
    instructions = ins.read()

ic = IntCode(memory)
ic.inp += list(map(ord, list(instructions)))
ic.start()

# print(ic.popout())
print(ic.popout()[-1])