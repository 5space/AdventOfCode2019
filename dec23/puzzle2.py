import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec23/input.txt", "r") as file:
    memory = list(map(int, file.read().split(",")))

ics = [IntCode(memory.copy()) for _ in range(50)]
for i, ic in enumerate(ics):
    ic.inp.append(i)
    ic.start()
currentindex = 0
queues = {n: [] for n in range(50)}

nat = (None, None)
lasty = -1

while True:
    if queues[currentindex] == []:
        ics[currentindex].inp.append(-1)
    else:
        for p in queues[currentindex]:
            ics[currentindex].inp += list(p)
        queues[currentindex] = []
    ics[currentindex].start()
    out = ics[currentindex].popout()
    for i in range(0, len(out), 3):
        if out[i] == 255:
            nat = (out[i+1], out[i+2])
        else:
            queues[out[i]].append((out[i+1], out[i+2]))
    if all(queues[k] == [] for k in queues):
        queues[0] = [(nat[0], nat[1])]
        if lasty == nat[1]:
            print(nat[1])
            break
        lasty = nat[1]
    currentindex = (currentindex + 1) % 50