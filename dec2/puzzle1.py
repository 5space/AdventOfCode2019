with open("input.txt", "r") as file:
    field = list(map(int, file.read().split(",")))
field[1] = 12
field[2] = 2

c = 0
while field[c] != 99:
    if field[c] == 1:
        a1, a2, a3 = field[c+1], field[c+2], field[c+3]
        field[a3] = field[a1] + field[a2]
    elif field[c] == 2:
        a1, a2, a3 = field[c+1], field[c+2], field[c+3]
        field[a3] = field[a1] * field[a2]
    c += 4

print(field[0])
