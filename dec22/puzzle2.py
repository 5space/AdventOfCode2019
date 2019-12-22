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

class ModuloLinearFunction:

    #form a + bn
    def __init__(self, base, constant=0, coefficient=1): 
        self.base = base
        self.constant = constant % self.base
        self.coefficient = coefficient % self.base
    
    def __add__(self, other):
        return ModuloLinearFunction(self.base, self.constant + other.constant, self.coefficient + other.coefficient)
    
    def __rmul__(self, other):
        return ModuloLinearFunction(self.base, other*self.constant % self.base, other*self.coefficient % self.base)

    def __mul__(self, other):
        if isinstance(other, ModuloLinearFunction):
            newconstant = other.constant + other.coefficient * self.constant
            newcoefficient = other.coefficient * self.coefficient
            return ModuloLinearFunction(self.base, newconstant, newcoefficient)
        else:
            return self.__rmul__(other)
    
    def __call__(self, value):
        return (self.constant + self.coefficient * value) % self.base
    
    def __repr__(self):
        return f"{self.constant} + {self.coefficient} * n"
    
    def __pow__(self, val):
        newcoefficient = pow(self.coefficient, val, self.base)
        newconstant = (pow(self.coefficient, val, self.base) - 1) * modinv(self.coefficient - 1, self.base) * self.constant
        return ModuloLinearFunction(self.base, newconstant, newcoefficient)

BASE = 119315717514047

current_function = ModuloLinearFunction(BASE)  # Identity function (0 + 1x)
with open("dec22/input.txt", "r") as file:
    for line in file.readlines():
        if "cut" in line:
            current_function *= ModuloLinearFunction(BASE, int(line.strip()[4:]))
        elif "deal with increment" in line:
            current_function *= int(line.strip()[20:])
        else:
            current_function *= ModuloLinearFunction(BASE, -1, -1)

current_function **= 101741582076661
a, b = current_function.constant, current_function.coefficient
print(((2020-a)*modinv(b, BASE))%BASE)
