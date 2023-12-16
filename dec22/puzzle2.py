import timeit

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
        newconstant = (pow(self.coefficient, val, self.base) - 1) * pow(self.coefficient - 1, -1, self.base) * self.constant
        return ModuloLinearFunction(self.base, newconstant, newcoefficient)

def main():
    BASE = 119315717514047
    current_function = ModuloLinearFunction(BASE)  # Identity function (0 + 1x)
    with open("dec22/input.txt", "r") as file:
        for line in file.readlines():
            if "cut" in line:
                current_function *= ModuloLinearFunction(BASE, -int(line.strip()[4:]))
            elif "deal with increment" in line:
                current_function *= int(line.strip()[20:])
            else:
                current_function *= ModuloLinearFunction(BASE, -1, -1)
    current_function **= 101741582076661
    a, b = current_function.constant, current_function.coefficient
    return ((2020-a) * pow(b, -1, BASE)) % BASE

print(main())
print(timeit.timeit(main, number=1000)/1000)
