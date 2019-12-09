def add(i, args, modes):
    i.set(modes[2], i.get(modes[0]) + i.get(modes[1]))
def mul(i, args, modes):
    i.set(modes[2], i.get(modes[0]) * i.get(modes[1]))
def inp(i, args, modes):
    if len(i.inp) > 0:
        i.set(modes[0], i.inp.pop(0))
    else:
        return True
def out(i, args, modes):
    i.out.append(i.get(modes[0]))
def jif(i, args, modes):
    if i.get(modes[0]) != 0:
        i.pointer = i.get(modes[1])
        i.skip = False
def jit(i, args, modes):
    if i.get(modes[0]) == 0:
        i.pointer = i.get(modes[1])
        i.skip = False
def le(i, args, modes):
    if i.get(modes[0]) < i.get(modes[1]):
        i.set(modes[2], 1)
    else:
        i.set(modes[2], 0)
def eq(i, args, modes):
    if i.get(modes[0]) == i.get(modes[1]):
        i.set(modes[2], 1)
    else:
        i.set(modes[2], 0)
def rel(i, args, modes):
    i.relative += i.get(modes[0])

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
        if i < 0:
            raise Exception(f"Attempted to access negative memory address {i}")
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
                args = []
                with_modes = []
                for i in range(numargs):
                    code, d = divmod(code, 10)
                    args.append(self.memory.get(self.pointer+i+1))
                    if d == 0:
                        with_modes.append(args[i])
                    elif d == 1:
                        with_modes.append(self.pointer+i+1)
                    elif d == 2:
                        with_modes.append(args[i] + self.relative)
                    else:
                        raise Exception(f"Invalid mode {d}")
                if func(self, args, with_modes):
                    break
                else:
                    if self.skip:
                        self.pointer += numargs + 1
                    else:
                        self.skip = True
        self.running = False
        return self.out
