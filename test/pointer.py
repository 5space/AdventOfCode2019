from intcodeplt import IntCode
from matplotlib import pyplot as plt


# def main():
#     with open("test/program.txt", "r") as file:
#         memory = list(map(int, file.read().split(",")))
    
#     paddlepos = 0
#     ballpos = 0

#     xs = []
#     ys = []
#     currx = 0

#     def callback(pointer):
#         nonlocal currx
#         xs.append(currx)
#         ys.append(pointer)
#         currx += 1

#     ic = IntCode(memory, pointer_callback=callback)
    
#     while True:
#         if ballpos < paddlepos:
#             joystick = -1
#         elif ballpos > paddlepos:
#             joystick = 1
#         else:
#             joystick = 0
#         ic.start(inp=[joystick])
#         if len(ic.out) == 0:
#             break
#         for i in range(0, len(ic.out), 3):
#             x, y, tile = ic.out[i:i+3]
#             if x == -1 and y == 0:
#                 print("score", tile)
#             else:
#                 if tile == 3:
#                     paddlepos = x
#                 elif tile == 4:
#                     ballpos = x
#         ic.out = []
    
#     plt.scatter(xs, ys, 1)
#     plt.show()

def main():
    with open("test/program.txt", "r") as file:
        memory = list(map(int, file.read().split(",")))
    
    xs = []
    ys = []
    currx = 0
    
    def callback(pointer):
        nonlocal currx
        xs.append(currx)
        ys.append(pointer)
        currx += 1

    ic = IntCode(memory, pointer_callback=callback)
    
    ic.start(inp=[1])
    plt.scatter(xs, ys, 1)
    plt.show()

if __name__ == "__main__":
    main()

