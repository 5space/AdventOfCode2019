c = 0
start, end = 124075, 580769

def meets(n):
    p = str(n)
    if sorted(list(p)) != list(p):
        return False
    for i in range(1, 6):
        if p[i] == p[i-1]:
            if (i == 5 or p[i+1] != p[i]) and (i == 0 or p[i-2] != p[i-1]):
                return True
    return False

for x1 in range(1, 10):
    for x2 in range(x1, 10):
        for x3 in range(x2, 10):
            for x4 in range(x3, 10):
                for x5 in range(x4, 10):
                    for x6 in range(x5, 10):
                        if start <=100000*x1+10000*x2+1000*x3+100*x4+10*x5+x6 <= end:
                            if len({x1, x2, x3, x4, x5, x6}) <= 5:
                                if x1 == x2 != x3 or x1 != x2 == x3 != x4 \
                                or x2 != x3 == x4 != x5 \
                                or x3 != x4 == x5 != x6 \
                                or x4 != x5 == x6: \
                                    c += 1

print(c)