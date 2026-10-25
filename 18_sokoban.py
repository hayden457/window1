import tkinter as tk
from PIL import Image, ImageTk

TILE = 64
W = 8
H = 8

current_level = 0

root = tk.Tk()
root.title("Sokoban")

game_map = []
player_r = 0
player_c = 0

canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()

TILE_IMAGE = {
    '#': 'wall',
    ' ': 'floor',
    '.': 'goal',
    '@': 'player',
    '+': 'player_goal',
    '$': 'box',
    '*': 'box_goal'
}

def load_tile(filename):
    img = Image.open('tiles/' + filename)
    img = img.resize((TILE, TILE), Image.NEAREST)
    return ImageTk.PhotoImage(img)


images = {
    'wall': load_tile('tile_wall_vertical.png'),
    'floor': load_tile('tile_path.png'),
    'goal': load_tile('tile_goal.png'),
    'player': load_tile('tile_player.png'),
    'player_goal': load_tile('tile_player_goal.png'),
    'box': load_tile('tile_block.png'),
    'box_goal': load_tile('tile_goal.png')
}
LEVELS = [
    [
        "#######",
        "#     #",
        "# .$. #",
        "# .@. #",
        "#     #",
        "#######",
    ]
]

def load_level(index):
    global game_map, player_r, player_c

    game_map = []
    for row_string in LEVELS[index]:
        game_map.append(list(row_string))

    for r in range(len(game_map)):
        for c in range(len(game_map[r])):
            if game_map[r][c] in ('@', '+'):
                player_r = r
                player_c = c

    rows = len(game_map)
    cols = len(game_map[0])
    canvas.config(width=cols*TILE, height=rows*TILE)

def draw_title(r, c, key):
    x = c * TILE
    y = r * TILE
    canvas.create_image(x, y, image=images[key], anchor='nw')

def draw_world():
    canvas.delete('all')
    for r in range(len(game_map)):
        for c in range(len(game_map[r])):
            ch = game_map[r][c]
            key = TILE_IMAGE[ch]
            draw_title(r, c, key)

def try_move(dr, dc):
    global player_r, player_c
    nr = player_r + dr
    nc = player_c + dc

    if not (0 <= nr < len(game_map) and 0 <= nc < len(game_map[0])):
        return

    tile = game_map[nr][nc]

    if tile == '#':
        return

    if tile in (' ', '.'):
        move_player(nr, nc)

    elif tile in ('$', '*'):
        br = nr + dr
        bc = nc + dc

        if not (0 <= br < len(game_map) and 0 <= bc < len(game_map[0])):
            return
        box_dest = game_map[br][bc]

        if box_dest in (' ', '.'):
            push_box(nr, nc, br, bc)
            move_player(nr, nc)

def move_player(nr, nc):
    global player_r, player_c

    if game_map[player_r][player_c] == '+':
        game_map[player_r][player_c] == '.'


def push_box():
    game_map[br][bc] = '*' if game_map[br][bc] == '.' else '$'

def check_win():
    for row in game_map:
        if '$' in row:
            return
    print("You win!")

#check_win()
print()
load_level(0)
draw_world()

root.mainloop()
