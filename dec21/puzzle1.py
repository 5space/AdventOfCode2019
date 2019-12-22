import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec21/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

instructions = "NOT C J\nAND D J\nNOT A T\nOR T J\nWALK"
ic = IntCode(memory)
ic.inp += list(map(ord, list(instructions)))
ic.start()

print(ic.popout())