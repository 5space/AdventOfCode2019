import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec17/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

ic = IntCode(memory)
ic.start()
string = "".join(chr(k) for k in ic.popout())
lines = string.strip().split("\n")
print(lines)
total = 0
for x in range(1, len(lines[0])-2):
    for y in range(1, len(lines)-2):
        if lines[y][x] == "#" and lines[y-1][x] == "#" and lines[y+1][x] == "#" and lines[y][x+1] == "#" and lines[y][x-1] == "#":
            total += y*x
print(total)