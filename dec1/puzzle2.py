with open("input.txt", "r") as file:
    modules = map(int, file.readlines())

def fuel(mass):
    f, c = 0, mass//3 - 2
    while c > 0:
        f += c
        c = c//3 - 2
    return f

print(sum(fuel(m) for m in modules))
