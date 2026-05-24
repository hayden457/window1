#Page 3
COLOURS = ["R", "B", "G", "Y"]
COLOUR_NAMES = {"R": "Red", "B": "Blue", "G": "Green", "Y": "Yellow"}
PEGS = 4
MAX_GUESSES = 8

#Page 4
import random

secret = [random.choice(COLOURS) for _ in range(PEGS)]

def guess(selections):
     return [selections[i].get() for i in range(PEGS)]

blacks = 0
for i in range(PEGS):
        if guess[i] == secret[i]:
            blacks += 1

#Page 5
from collections import Counter

secret_counts = Counter(secret)
guess_counts = Counter(guess)

total_matched = sum(min(secret_counts[c], guess_counts[c]) for c in COLOURS)

whites = total_matched - blacks

#Page 6
from collections import Counter

def get_feedback(secret, guess):
    blacks = 0
    for i in range(PEGS):
        if guess[i] == secret[i]:
            blacks += 1

    secret_counts = Counter(secret)
    guess_counts = Counter(guess)
    total_matched = sum(min(secret_counts[c], guess_counts[c]) for c in COLOURS)
    whites = total_matched - blacks

    return blacks, whites

#Page 7
import tkinter as tk
from collections import Counter
import random

COLOURS = ['R', 'B', 'G', 'Y']
COLOUR_NAMES = {'R':'Red', 'B':'Blue', 'G':'Green', 'Y':'Yellow'}
COLOUR_HEX = {'R':'#E74C3C', 'B':'#2980B9', 'G':'#27AE60', 'Y':'#F1C40F'}
PEGS = 4
MAX_GUESSES = 8

root = tk.Tk()
root.title('Mastermind')
root.resizeable(False, False)

secret = [random.choice(COLOURS) for _ in range(PEGS)]
guess_count = 0
game_over = False

header = tk.Label(root, text='Mastermind -- Crack the 4-colour code!',
                  font=('Arial', 14, 'bold'), pady=8)
header.grid(row=0, column=0, columnspan=6, sticky='ew')

#Page 8
history_frame = tk.Frame(root)
history_frame.grid(row=1, column=0, columnspan=6, padx=10, pady=5)

for i, text in enumerate(['#', 'Peg 1', 'Peg 2', 'Peg 3', 'Peg 4', 'Feedback']):
     tk.Label(history_frame, text=text, font=('Arial', 11, 'bold'),
              width=8, relief='groove').grid(row=0, column=i)
     
#Page 9
selections = [tk.StringVar(value='R') for _ in range(PEGS)]

input_frame = tk.Frame(root)
input_frame.grid(row=2, column=0, columnspan=6, pady=8)

tk.Label(input_frame, text='Your guess:', font=('Arial', 11)).grid(row=0, column=0, padx=5)

def make_callback(index):
     def callback(val):
          on_dropdown_change(val, index)
     return callback 

for i in range(PEGS):
     om = tk.OptionMenu(
          input_frame,
          selections[i],
          *[COLOUR_NAMES[c] for c in COLOURS],
          command=make_callback(i)
     )
     om.config(width=8)
     om.grid(row=0, column=i+1, padx=3)

NAME_TO_LETTER = {v: k for k, v in COLOUR_NAMES.items()}

def on_dropdown_change(name, idx):
     selections[idx].set(NAME_TO_LETTER[name])

#Page 10

def submit_guess():
     global guess_count, game_over

     if game_over:
          return
     guess = [selections[i].get() for i in range(PEGS)]

     blacks, whites = get_feedback(secret, guess)

     guess_count += 1
     row = guess_count

     tk.Label(history_frame, text=str(guess_count),
              width=8, relief='goove').grid(row=row, column=0)
     
     #Page 11
     for i, letter in enumerate(guess):
          tk.Label(history_frame,
                   text=COLOUR_NAMES[letter],
                   fg='white', width=8, relief='groove'
                   ).grid(row=row, column=i+1)

submit_btn = tk.Button(input_frame, text='Submit Guess',
                       font=('Arial', 11), command=submit_guess)
submit_btn.grid(row=0, column=PEGS+1, padx=10)

status_label = tk.Label(root, text=f'Guess 1 of {MAX_GUESSES}',
                        font=('Arial', 12), pady=6)
status_label.grid(row=3, column=0, columnspan=6)
          
feedback_text = '⚫' * blacks + '⚪' * whites
if blacks + whites == '0':
     feedback_text = '__'

row=guess_count
tk.Label(history_frame, text=feedback_text,
         width=8, relief='groove').grid(row=row, column=PEGS+1)

def reveal_secret():
    reveal_frame = tk.Frame(root)
    reveal_frame.grid(row=4, column=0, columnspan=6, pady=4)

    tk.Label(reveal_frame, text='Secret code:',
             font=('Arial', 11, 'bold')).grid(row=0, column=0, padx=5)

    for i, letter in enumerate(secret):
        tk.Label(reveal_frame,
                 text=COLOUR_NAMES[letter],
                 bg=COLOUR_HEX[letter],
                 fg='white', width=8, relief='groove'
                 ).grid(row=0, column=i+1)

if blacks == PEGS:
     status_label.config(text=f'You cracked it in {guess_count} guesses!')
     game_over = True
     reveal_secret()
elif guess_count >= MAX_GUESSES:
     status_label.config(text='Out of guesses! See the secret below.')
     game_over = True
     reveal_secret()
else:
     remaining = MAX_GUESSES - guess_count
     status_label.config(text=f'Remaining guesses: {remaining}')

#Page 12

def new_game():
    global secret, guess_count, game_over

    secret = [random.choice(COLOURS) for _ in range(PEGS)]

    for widget in history_frame.winfo_children():
        widget.destroy()

    for i, text in enumerate(['#', 'Peg 1', 'Peg 2', 'Peg 3', 'Peg 4', 'Feedback']):
     tk.Label(history_frame, text=text, font=('Arial', 11, 'bold'),
              width=8, relief='groove').grid(row=0, column=i)
     #Page 13
     for widget in root.grid_slaves():
          if int(widget.grid_info()['row']) == 4:
               widget.destroy()

     status_label.config(text=f'Guess 1 of {MAX_GUESSES}')

     for s in selections:
          s.set('R')
new_game_btn = tk.Button(root, text='New Game',
                         font=('Arial', 11), command=new_game)
new_game_btn.grid(row=5, column=0, columnspan=6, pady=6)
