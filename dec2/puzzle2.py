from util import run_vm

with open("dec2/input.txt", "r") as file:
    f = list(map(int, file.read().split(",")))

for n in range(100):
    for v in range(100):
        field = f.copy()
        field[1] = n
        field[2] = v
        res = run_vm(field)
        if res[0] == 19690720:
            print(n, v)
