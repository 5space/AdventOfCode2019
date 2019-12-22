def add(i, args):
    i.put(args[2], i.get(args[0]) + i.get(args[1]))

def mul(i, args):
    i.put(args[2], i.get(args[0]) * i.get(args[1]))

def inp(i, args):
    if len(i.inp) > 0:
        i.put(args[0], i.inp.pop(0))
    else:
        i.waiting = True

def out(i, args):
    i.out.append(i.get(args[0]))

def jif(i, args):
    if i.get(args[0]) != 0:
        i.pointer = i.get(args[1])
        i.skip = False

def jit(i, args):
    if i.get(args[0]) == 0:
        i.pointer = i.get(args[1])
        i.skip = False

def le(i, args):
    if i.get(args[0]) < i.get(args[1]):
        i.put(args[2], 1)
    else:
        i.put(args[2], 0)

def eq(i, args):
    if i.get(args[0]) == i.get(args[1]):
        i.put(args[2], 1)
    else:
        i.put(args[2], 0)

def rel(i, args):
    i.relative += i.get(args[0])

OPCODES = {1: [add, 3],
           2: [mul, 3],
           3: [inp, 1],
           4: [out, 1],
           5: [jif, 2],
           6: [jit, 2],
           7: [le, 3],
           8: [eq, 3],
           9: [rel, 1],
           99: [None, 0]}

class IntCode:

    def __init__(self, memory, inp=None, ops=OPCODES):
        self.ops = ops
        self.memory = dict(enumerate(memory))
        self.inp = inp or []
        self.out = []
        self.pointer = 0
        self.skip = True
        self.hashalted = False
        self.relative = 0
        self.waiting = False
    
    def put(self, i, x):
        if i < 0:
            raise Exception(f"Attempted to access negative memory address {i}")
        self.memory[i] = x
    
    def get(self, i):
        if i < 0:
            raise Exception(f"Attempted to access negative memory address {i}")
        elif i not in self.memory:
            return 0
        else:
            return self.memory[i]
    
    def popout(self):
        out = self.out
        self.out = []
        return out
    
    def start(self):
        if self.inp == [] and self.waiting:
            return
        else:
            self.waiting = False
        while True:
            code, opcode = divmod(self.memory[self.pointer], 100)
            if opcode == 99:
                self.hashalted = True
                break
            elif opcode not in self.ops:
                raise Exception(f"Invalid opcode {opcode}")
            else:
                func, numargs = self.ops[opcode]
                args = []
                for i in range(numargs):
                    code, d = divmod(code, 10)
                    if d == 0:
                        args.append(self.memory.get(self.pointer+i+1))
                    elif d == 1:
                        args.append(self.pointer+i+1)
                    elif d == 2:
                        args.append(self.memory.get(self.pointer+i+1) + self.relative)
                    else:
                        raise Exception(f"Invalid mode {d}")

                func(self, args)
                if self.waiting:
                    break
                
                if self.skip:
                    self.pointer += numargs + 1
                else:
                    self.skip = True
