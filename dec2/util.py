def run_vm(mem, ops={1: lambda x,y: x+y, 2: lambda x,y: x*y, 99: None}):
    memory = mem.copy()
    c = 0
    while c < len(memory) - 3:
        a, a1, a2, a3 = memory[c], memory[c+1], memory[c+2], memory[c+3]
        if a in ops:
            if ops[a] is None:
                break
            else:
                memory[a3] = ops[a](memory[a1], memory[a2])
        else:
            raise Exception(f"Invalid opcode {a}")
        c += 4
    return memory
