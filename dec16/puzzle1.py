def next_phase(val):
    result = ""
    for i, n in enumerate(val):
        remainder = 0
        for i2, n2 in enumerate(val):
            pattern = int((i2+1)/(i+1)) % 4
            if pattern == 1:
                remainder += int(n2)
            elif pattern == 3:
                remainder -= int(n2)
        result += str(abs(remainder) % 10)
    return result

with open("dec16/input.txt", "r") as file:
    string = file.read().strip()

for i in range(100):
    string = next_phase(string)
    print(string[-8:])
