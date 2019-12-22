def cut(cards, value):
    return cards[value:] + cards[:value]

def new_stack(cards):
    return cards[::-1]

def increment(cards, value):
    out = [0 for _ in range(len(cards))]
    for i in range(len(cards)):
        out[(i*value)%len(cards)] = cards[i]
    return out

cards = list(range(10007))

with open("dec22/input.txt", "r") as file:
    for line in file.readlines():
        if "cut" in line:
            cards = cut(cards, int(line.strip().split(" ")[-1]))
        elif "deal with increment" in line:
            cards = increment(cards, int(line.strip().split(" ")[-1]))
        else:
            cards = new_stack(cards)

print(cards.index(2019))