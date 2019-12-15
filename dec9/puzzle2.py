import sys, os, timeit
sys.path.append(os.getcwd())
from util.intcode import IntCode

def main():
    with open("dec9/input.txt", "r") as file:
        memory = list(map(int, file.read().split(",")))

    ic = IntCode(memory, inp=[2])
    ic.start()
    return ic.out[0]

print(main())
print(timeit.timeit(main, number=1))
