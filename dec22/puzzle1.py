import timeit

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

class LinearModuloFunction:

    #form a + bn
    def __init__(self, base, constant=0, coefficient=1): 
        self.base = base
        self.constant = constant
        self.coefficient = coefficient
    
    def __add__(self, other):
        return LinearModuloFunction(self.base, self.constant + other.constant, self.coefficient + other.coefficient)
    
    #scalar multiplication
    def __rmul__(self, other):
        return LinearModuloFunction(self.base, other*self.constant % self.base, other*self.coefficient % self.base)

    #works like matrix multiplication in reverse, first left then right is applied
    def __mul__(self, other):
        if isinstance(other, LinearModuloFunction):
            newconstant = other.constant + other.coefficient * self.constant
            newcoefficient = other.coefficient * self.coefficient
            return LinearModuloFunction(self.base, newconstant % self.base, newcoefficient % self.base)
        else:
            return self.__rmul__(other)
    
    def __call__(self, value):
        return (self.constant + self.coefficient * value) % self.base
    
    def __repr__(self):
        return f"{self.constant} + {self.coefficient} * n"
    
    def __pow__(self, val):
        newcoefficient = pow(self.coefficient, val, self.base)
        newconstant = (pow(self.coefficient, val, self.base) - 1) * modinv(self.coefficient - 1, self.base) * self.constant
        return LinearModuloFunction(self.base, newconstant % self.base, newcoefficient % self.base)

def main():
    BASE = 10007
    current_function = LinearModuloFunction(BASE)  # Identity function (0 + 1x)
    with open("dec22/input.txt", "r") as file:
        for line in file.readlines():
            if "cut" in line:
                current_function *= LinearModuloFunction(BASE, -int(line.strip().split(" ")[-1]))
            elif "deal with increment" in line:
                current_function *= int(line.strip().split(" ")[-1])
            else:
                current_function *= LinearModuloFunction(BASE, -1, -1)
    return current_function(2019)

print(main())
print(timeit.timeit(main, number=1000)/1000)