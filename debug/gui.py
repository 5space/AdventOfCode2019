import PySimpleGUI as sg
import sys, os
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec2/input.txt", "r") as file:
    memory = list(map(int, file.read().strip().split(",")))

ic = IntCode(memory)

def repr(memory):
    keys = sorted(memory.keys())
    string = str(memory[keys[0]])
    for i in range(1, len(keys)):
        if keys[i]-keys[i-1] == 1:
            string += f", {memory[keys[i]]}"
        else:
            string += f", ({keys[i]-keys[i-1]-1} empty), {memory[keys[i]]}"
    return string

layout = [[sg.Text("IntCode Debugger")],
          [sg.Button("Run", key="_RUN_BUTTON_"),
           sg.Button("Step"),
           sg.Text("", key="_INFO_", size=(40, 1))],
          [sg.Text("", key="_MEMORY_", size=(80, 40))]]
window = sg.Window("IntCode Debugger", layout)

run_toggle = False
k = 0
while True:
    k += 1
    event, values = window.read(timeout=0)
    if event is None:
        break
    if event == "Step":
        ic.step()
    elif event == "_RUN_BUTTON_":
        run_toggle = not run_toggle
        if run_toggle:
            window["_RUN_BUTTON_"].update("Stop")
        else:
            window["_RUN_BUTTON_"].update("Run")
    if run_toggle:
        ic.step()
    if k % 100 == 0:
        print(k)
    window["_MEMORY_"].update(repr(ic.memory))
    window["_INFO_"].update(f"IP {ic.pointer} | Input {ic.inp} | Output {ic.out}")
