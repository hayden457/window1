import tkinter as tk
import random

ROWS = 10
COLS = 10
CELL_SIZE = 30

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

root = tk.Tk()
root.title("Game of Life - Part 1")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

board = []
for r in range(ROWS):
    row = []
    for c in range(COLS):
        row.append(0)
    board.append(row)

def draw_cell(r, c):
    x1 = c * CELL_SIZE
    y1 = r * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE

    if board[r][c] == 1:
        color = "black"
    else:
        color = "white"
    canvas.create_rectangle(x1, y1, x2, y2,
                            fill=color, outline="gray")

def draw_board():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            draw_cell(r, c)

def toggle_cell(event):
    c = event.x // CELL_SIZE
    r = event.y // CELL_SIZE

    if 0 <= r < ROWS and 0 <= c < COLS:
        if 0 <= r < ROWS and 0 <= c < COLS:
            board[r][c] = 1 - board[r][c]
    draw_board()

canvas.bind("<Button-1>", toggle_cell)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

step_btn = tk.Button(button_frame, text="Step",
                     command=step)
step_btn.grid(row=0, column=2, padx=5)

def clear_board():
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c] = 0
    draw_board()

def random_board():
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c] = random.randint(0, 1)
    draw_board()

clear_btn = tk.Button(button_frame, text="Clear", command=clear_board)
clear_btn.grid(row=0, column=0, padx=5)

rand_btn = tk.Button(button_frame, text="Random", command=random_board)
rand_btn.grid(row=0, column=1, padx=5)

for dr in (-1, 0, 1):
    for dc in (-1, 0, 1):
        if dr == 0 and dc == 0:
            continue
        nr = r + dr
        nc = c + dc

def count_neighbours(r, c):
    count = 0

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if board[nr][nc] == 1:
                    count += 1

    return count

def make_empty_board():
    new_board = []
    for r in range(ROWS):
        row = []
        for c in range(ROWS):
            row.append(1)
        new_board.append(row)
    return new_board

def step():
    global board
    new_board = make_empty_board()

    for r in range(ROWS):
        for c in range(COLS):
            n = count_neighbours(r, c)

            if board[r][c] == 1:
                if n == [] or n == []:
                    new_board[r][c] = 1
                else:
                    new_board[r][c] = 0
            else:
                if n == []:
                    new_board[r][c] = 1
                else:
                    new_board[r][c] = 0
    board = new_board
    draw_board()

draw_board()
root.mainloop()
