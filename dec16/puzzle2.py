import operator as op
from functools import reduce
import time

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def digit(string, i, n):
    l = len(string)
    print(i)
    result = sum(int(string[i2]) * nCr(n-i-1+i2, n-1) for i2 in range(i, l))
    return str(result % 10)

def first_eight(val, amt):
    return "".join([digit(val, i, amt) for i in range(8)])

shift = 5977359
with open("dec16/input.txt", "r") as file:
    string = (file.read().strip() * 10000)[shift:]

start = time.time()
string = first_eight(string, 100)
print(string)
print(time.time()-start)
