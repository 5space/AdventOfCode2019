c = 0
for n in range(124075, 580769+1):
    p = str(n)
    if any(p[i] == p[i-1] for i in range(1, 6)):
        if sorted(list(p)) == list(p):
            c += 1
print(c)
