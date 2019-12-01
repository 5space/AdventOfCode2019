with open("input.txt", "r") as file:
    modules = map(int, file.readlines())

print(sum(m//3 - 2 for m in modules))