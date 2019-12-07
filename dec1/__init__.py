def opcode1(i, args, modes):
    m = i.memory
    m[args[2]] = m[args[0]] + m[args[1]]
def opcode2(i, args, modes):
    m = i.memory
    m[args[2]] = m[args[0]] * m[args[1]]
def opcode3(i, args, modes):
    i.memory[args[0]] = i.inp.pop(0)
def opcode4(i, args, modes):
    i.out.append(i.memory[args[0]])

OPCODES = {'1': [opcode1, 3], '2': [opcode2, 3], '3': [opcode3, 1]}

class IntCode:

    def __init__(self, memory, inp=[], ops=OPCODES):
        self.ops = ops
        self.memory = memory
        self.inp = inp
        self.out = []
    
    def run(self):
        pointer = 0
        while pointer < len(self.memory):
            code = str(self.memory[pointer])
            opcode = code[-2:]
            code = code[:-2]
            if opcode == "99":
                break
            elif opcode not in self.ops:
                raise Exception(f"Invalid opcode {opcode}")
            else:
                func, numargs = self.ops[opcode]
                code = code.zfill(numargs)[::-1]
                args = self.memory[pointer+1:pointer+numargs+1]
                modes = [d == "1" for d in code]
                func(self, args, modes)
                pointer += numargs + 1
        return memory
