import tkinter as tk
import random

# --- Setup ---
root = tk.Tk()
root.title("Lights Out")

ROWS = 5
COLS = 5

# Game state grid (all OFF at start)
grid = [[0] * COLS for _ in range(ROWS)]
buttons = [[None] * COLS for _ in range(ROWS)]

# --- Status label ---
status_label = tk.Label(root, text="Turn all lights OFF!", font=("Arial", 14))
status_label.grid(row=ROWS, column=0, columnspan=COLS, pady=10)

# --- Toggle logic ---
def toggle_cell(r, c):
    if 0 <= r < ROWS and 0 <= c < COLS:
        grid[r][c] = 1 - grid[r][c]  # flip 0→1 or 1→0
        colour = "yellow" if grid[r][c] == 1 else "grey20"
        buttons[r][c].config(bg=colour)

# --- Click handler ---
def on_click(r, c):
    toggle_cell(r, c)       # itself
    toggle_cell(r-1, c)     # above
    toggle_cell(r+1, c)     # below
    toggle_cell(r, c-1)     # left
    toggle_cell(r, c+1)     # right
    check_win()

# --- Win check ---
def check_win():
    for row in grid:
        for cell in row:
            if cell == 1:
                return  # found ON cell, not a win yet
    status_label.config(text="🎉 YOU WIN! All lights are OFF!")

# --- Closure for button commands ---
def make_handler(r, c):
    def handler():
        on_click(r, c)
    return handler

# --- Button grid ---
for r in range(ROWS):
    for c in range(COLS):
        btn = tk.Button(root, width=6, height=3, bg="grey20",
                        command=make_handler(r, c))
        btn.grid(row=r, column=c, padx=2, pady=2)
        buttons[r][c] = btn

# --- Shuffle board ---
def shuffle_board(clicks=10):
    for _ in range(clicks):
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        on_click(r, c)

# --- Restart button ---
def restart():
    global grid
    grid = [[0] * COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            buttons[r][c].config(bg="grey20")
    status_label.config(text="Turn all lights OFF!")
    shuffle_board(10)

restart_btn = tk.Button(root, text="New Game", font=("Arial", 12),
                        command=restart)
restart_btn.grid(row=ROWS+1, column=0, columnspan=COLS, pady=8)

# --- Start game ---
shuffle_board(10)
root.mainloop()
