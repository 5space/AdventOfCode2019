def opcode1(i, args, modes):
    m = i.memory
    a = args[0] if modes[0] else m[args[0]]
    b = args[1] if modes[1] else m[args[1]]
    m[args[2]] = a + b
def opcode2(i, args, modes):
    m = i.memory
    a = args[0] if modes[0] else m[args[0]]
    b = args[1] if modes[1] else m[args[1]]
    m[args[2]] = a * b
def opcode3(i, args, modes):
    if len(i.inp) > 0:
        i.memory[args[0]] = i.inp.pop(0)
    else:
        return True
def opcode4(i, args, modes):
    m = i.memory
    a = args[0] if modes[0] else m[args[0]]
    i.out.append(a)
def opcode5(i, args, modes):
    m = i.memory
    a = args[0] if modes[0] else m[args[0]]
    b = args[1] if modes[1] else m[args[1]]
    if a != 0:
        i.pointer = b
        i.skip = False
def opcode6(i, args, modes):
    m = i.memory
    a = args[0] if modes[0] else m[args[0]]
    b = args[1] if modes[1] else m[args[1]]
    if a == 0:
        i.pointer = b
        i.skip = False
def opcode7(i, args, modes):
    m = i.memory
    a = args[0] if modes[0] else m[args[0]]
    b = args[1] if modes[1] else m[args[1]]
    if a < b:
        m[args[2]] = 1
    else:
        m[args[2]] = 0
def opcode8(i, args, modes):
    m = i.memory
    a = args[0] if modes[0] else m[args[0]]
    b = args[1] if modes[1] else m[args[1]]
    if a == b:
        m[args[2]] = 1
    else:
        m[args[2]] = 0

OPCODES = {1: [opcode1, 3],
           2: [opcode2, 3],
           3: [opcode3, 1],
           4: [opcode4, 1],
           5: [opcode5, 2],
           6: [opcode6, 2],
           7: [opcode7, 3],
           8: [opcode8, 3]}

class IntCode:

    def __init__(self, memory, inp=None, ops=OPCODES):
        self.ops = ops
        self.memory = memory
        self.inp = inp or []
        self.out = []
        self.pointer = 0
        self.skip = True
        self.running = False
        self.hashalted = False
    
    def on_input_update(self):
        if not self.running:
            self.start()
    
    def start(self, inp=[]):
        self.inp += inp
        self.out = []
        self.running = True
        while self.pointer < len(self.memory):
            code, opcode = divmod(self.memory[self.pointer], 100)
            if opcode == 99:
                self.hashalted = True
                break
            elif opcode not in self.ops:
                raise Exception(f"Invalid opcode {opcode}")
            else:
                func, numargs = self.ops[opcode]
                args = self.memory[self.pointer+1:self.pointer+numargs+1]
                modes = []
                for _ in range(numargs):
                    code, d = divmod(code, 10)
                    modes.append(d == 1)
                if func(self, args, modes):
                    break
                else:
                    if self.skip:
                        self.pointer += numargs + 1
                    else:
                        self.skip = True
        self.running = False
        return self.out
