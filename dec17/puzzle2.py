import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec17/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

memory[0] = 2
ic = IntCode(memory)
inputstring = "B,C,B,A,C,A,B,A,C,A\nL,4,L,6,L,8,L,8\nL,8,R,10,L,10\nR,10,L,8,L,8,L,10\nn\n"

ic.inp += [ord(c) for c in inputstring]
ic.start()

print(ic.out[-1])