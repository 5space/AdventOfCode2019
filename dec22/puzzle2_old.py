CUT = 0
INCREMENT = 1
NEW_STACK = 2

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print(a, m)
        raise Exception('modular inverse does not exist')
    else:
        return x % m

amt_cards = 119315717514047
instructions = []
with open("dec22/input.txt", "r") as file:
    for line in file.readlines():
        if "cut" in line:
            instructions.append((CUT, int(line.strip().split(" ")[-1])))
        elif "deal with increment" in line:
            instructions.append((INCREMENT, int(line.strip().split(" ")[-1])))
        else:
            instructions.append((NEW_STACK,))

def get_position_change_backwards(index):
    curr_index = index
    for instr in instructions[::-1]:
        if instr[0] == NEW_STACK:
            curr_index = amt_cards - 1 - curr_index
        elif instr[0] == CUT:
            if instr[1] > 0:
                if curr_index < amt_cards - instr[1]:
                    curr_index += instr[1]
                else:
                    curr_index -= amt_cards - instr[1]
            else:
                if curr_index >= instr[1]:
                    curr_index += instr[1]
                else:
                    curr_index += amt_cards + instr[1]
        else:
            curr_index *= modinv(instr[1], amt_cards)
        curr_index %= amt_cards
    return curr_index

# print([get_position_change_backwards(i) for i in range(amt_cards)])
# 24787760213699

def recursive(index, num):
    ci = index
    for _ in range(num):
        ci = get_position_change_backwards(ci)
    return ci

# 80929665533218 - 24787760213699*80929665531198
print(recursive(80929665533218, 1))
print([recursive(i, 0) for i in range(20)])

seen_before = {}
ci = 8326
steps = 0
while ci not in seen_before:
    seen_before[ci] = steps
    ci = get_position_change_backwards(ci)
    steps += 1

print(ci, steps, seen_before[ci])