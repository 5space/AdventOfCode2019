import sys, os, itertools
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec25/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

directions = ["east\n", "north\n", "west\n", "south\n"]

items = ["spool of cat6", "weather machine", "hypercube", "shell", "space heater", "candy cane", "space law space brochure", "whirled peas"]

with open("dec25/path.txt", "r") as pathfile:
    path = pathfile.read()

ic = IntCode(memory)
ic.inp += list(map(ord, list(path)))
for combo in itertools.product((False, True), repeat=8):
    for i, value in enumerate(combo):
        if value:
            ic.inp += list(map(ord, list("drop " + items[i] + "\n")))
        else:
            ic.inp += list(map(ord, list("take " + items[i] + "\n")))
    ic.start()
    print("".join(map(chr, ic.popout())))
    ic.inp += list(map(ord, list("east\n")))
    ic.start()
    string = "".join(map(chr, ic.popout()))
    print(combo)
    if "lighter" not in string and "heavier" not in string:
        print(string)
        break