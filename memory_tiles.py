import tkinter as tk
import random

root = tk.Tk()
root.title("Memory Match 2x3")

values = ["😭", "😭", "💀", "💀", "😔", "😔"]
random.shuffle(values)

buttons = []

for i in range(6):
    btn = tk.Button(root, text="?", width=6, height=3)
    buttons.append(btn)

row = i // 3
col = i % 3
btn.grid(row=row, column=col, padx=5, pady=5)

button = []
for i in range(6):
    btn = tk.Button(root, text="?", width=6, height=3)
    button.append(btn)
    row = i // 3
    col = i % 3
    btn.grid(row=row, column=col, padx=5 , pady=5)

first_index = None
lock = False
matched = [False] * 6

def handle_click(i):
    global first_index, lock

    if lock:
        return
    if matched[i]:
        return
    
    buttons[i].config(text=values[i])

    if first_index is None:
        first_index = i
    else:
        if values[i] == values[first_index]:
            matched[i] = True
            matched[first_index] = True
            first_index = None
        else:
            lock = True
            root.after(800, flip_back, i, first_index)
            first_index = None

def flip_back(i1, i2):
    global lock
    buttons[i1].config(text="?")
    buttons[i2].config(text="?")
    lock = False

def make_handler(index):
    def handler():
        handle_click(index)
    return handler 

buttons = []
for i in range(6):
    btn = tk.Button(root, text="?", width=6, height=3)
    btn.config(command=make_handler(i))
    buttons.append(btn)
    row = i // 3
    col = i % 3
    btn.grid(row=row, column=col, padx=5, pady=5)

btn = tk.Button(root, text="?", width=6, height=3,
                command=lambda idx=i: handle_click(idx))

root.mainloop()
