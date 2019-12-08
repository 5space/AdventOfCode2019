import itertools
import timeit

import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

def main():
    with open("dec7/input.txt", "r") as file:
        memory = list(map(int, file.read().split(",")))
    m = 0
    for p in itertools.permutations(list(range(5))):
        index = 0
        currinput = [0]
        a, b, c, d, e = p
        ic_a = IntCode(memory.copy(), inp=[a])
        ic_b = IntCode(memory.copy(), inp=[b])
        ic_c = IntCode(memory.copy(), inp=[c])
        ic_d = IntCode(memory.copy(), inp=[d])
        ic_e = IntCode(memory.copy(), inp=[e])
        ics = [ic_a, ic_b, ic_c, ic_d, ic_e]
        for ic in ics:
            currinput = ics[index].start(currinput).copy()
            index = (index + 1) % 5
        ic_a.start([0])
        m = max(m, currinput[0])
    return m

print(main())
print(timeit.timeit(main, number=20)/20)
