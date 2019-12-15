def add(i, args, modes):
    if modes[0] == 0:
        a = i.get(args[0])
    elif modes[0] == 1:
        a = args[0]
    elif modes[0] == 2:
        a = i.get(args[0]+i.relative)
    if modes[1] == 0:
        b = i.get(args[1])
    elif modes[1] == 1:
        b = args[1]
    elif modes[1] == 2:
        b = i.get(args[1]+i.relative)
    c = args[2]+i.relative if modes[2] == 2 else args[2]
    i.set(c, a + b)
def mul(i, args, modes):
    if modes[0] == 0:
        a = i.get(args[0])
    elif modes[0] == 1:
        a = args[0]
    elif modes[0] == 2:
        a = i.get(args[0]+i.relative)
    if modes[1] == 0:
        b = i.get(args[1])
    elif modes[1] == 1:
        b = args[1]
    elif modes[1] == 2:
        b = i.get(args[1]+i.relative)
    c = args[2]+i.relative if modes[2] == 2 else args[2]
    i.set(c, a * b)
def inp(i, args, modes):
    if len(i.inp) > 0:
        c = args[0]+i.relative if modes[0] == 2 else args[0]
        i.set(c, i.inp.pop(0))
    else:
        return True
def out(i, args, modes):
    if modes[0] == 0:
        a = i.get(args[0])
    elif modes[0] == 1:
        a = args[0]
    elif modes[0] == 2:
        a = i.get(args[0]+i.relative)
    i.out.append(a)
def jif(i, args, modes):
    if modes[0] == 0:
        a = i.get(args[0])
    elif modes[0] == 1:
        a = args[0]
    elif modes[0] == 2:
        a = i.get(args[0]+i.relative)
    if modes[1] == 0:
        b = i.get(args[1])
    elif modes[1] == 1:
        b = args[1]
    elif modes[1] == 2:
        b = i.get(args[1]+i.relative)
    if a != 0:
        i.pointer = b
        i.skip = False
def jit(i, args, modes):
    if modes[0] == 0:
        a = i.get(args[0])
    elif modes[0] == 1:
        a = args[0]
    elif modes[0] == 2:
        a = i.get(args[0]+i.relative)
    if modes[1] == 0:
        b = i.get(args[1])
    elif modes[1] == 1:
        b = args[1]
    elif modes[1] == 2:
        b = i.get(args[1]+i.relative)
    if a == 0:
        i.pointer = b
        i.skip = False
def le(i, args, modes):
    if modes[0] == 0:
        a = i.get(args[0])
    elif modes[0] == 1:
        a = args[0]
    elif modes[0] == 2:
        a = i.get(args[0]+i.relative)
    if modes[1] == 0:
        b = i.get(args[1])
    elif modes[1] == 1:
        b = args[1]
    elif modes[1] == 2:
        b = i.get(args[1]+i.relative)
    c = args[2]+i.relative if modes[2] == 2 else args[2]
    if a < b:
        i.set(c, 1)
    else:
        i.set(c, 0)
def eq(i, args, modes):
    if modes[0] == 0:
        a = i.get(args[0])
    elif modes[0] == 1:
        a = args[0]
    elif modes[0] == 2:
        a = i.get(args[0]+i.relative)
    if modes[1] == 0:
        b = i.get(args[1])
    elif modes[1] == 1:
        b = args[1]
    elif modes[1] == 2:
        b = i.get(args[1]+i.relative)
    c = args[2]+i.relative if modes[2] == 2 else args[2]
    if a == b:
        i.set(c, 1)
    else:
        i.set(c, 0)
def rel(i, args, modes):
    if modes[0] == 0:
        a = i.get(args[0])
    elif modes[0] == 1:
        a = args[0]
    elif modes[0] == 2:
        a = i.get(args[0]+i.relative)
    i.relative += a

OPCODES = {1: [add, 3],
           2: [mul, 3],
           3: [inp, 1],
           4: [out, 1],
           5: [jif, 2],
           6: [jit, 2],
           7: [le, 3],
           8: [eq, 3],
           9: [rel, 1]}

class IntCode:

    def __init__(self, memory, inp=None, ops=OPCODES):
        self.ops = ops
        self.memory = dict(enumerate(memory))
        self.inp = inp or []
        self.out = []
        self.pointer = 0
        self.skip = True
        self.running = False
        self.hashalted = False
        self.relative = 0
    
    def set(self, i, x):
        if i < 0:
            raise Exception(f"Attempted to access negative memory address {i}")
        self.memory[i] = x
    
    def get(self, i):
        if i not in self.memory:
            return 0
        else:
            return self.memory[i]
    
    def on_input_update(self):
        if not self.running:
            self.start()
    
    def start(self, inp=[]):
        self.inp += inp
        self.out = []
        self.running = True
        while self.pointer in self.memory:
            code, opcode = divmod(self.memory[self.pointer], 100)
            if opcode == 99:
                self.hashalted = True
                break
            elif opcode not in self.ops:
                raise Exception(f"Invalid opcode {opcode}")
            else:
                func, numargs = self.ops[opcode]
                args = [self.memory.get(i) for i in range(self.pointer+1, self.pointer+numargs+1)]
                modes = []
                for i in range(numargs):
                    code, d = divmod(code, 10)
                    modes.append(d)
                if func(self, args, modes):
                    break
                else:
                    if self.skip:
                        self.pointer += numargs + 1
                    else:
                        self.skip = True
        self.running = False
        return self.out
