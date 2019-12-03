from util import run_vm

with open("dec2/input.txt", "r") as file:
    field = list(map(int, file.read().split(",")))
field[1] = 12
field[2] = 2

f = run_vm(field)
print(f[0])
