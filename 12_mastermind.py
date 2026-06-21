import tkinter as tk
import random
from collections import Counter

COLOURS = ['red', 'blue', 'green', 'yellow']

root = tk.Tk()
root.title('Mastermind')

def pick_colour(colour):
    if len(guess) < 4:
        guess.append(colour)
        slot = slots[len(guess) - 1]
        slot.config(bg=colour)

for colour in COLOURS:
    btn = tk.Button(
        root,
        text=colour,
        bg=colour,
        width=8, height=2,
        command=lambda c=colour: pick_colour(c)
    )
    btn.pack(side='left', padx=4, pady=10)
    
guess = []
slot_frame = tk.Frame(root)
slot_frame.pack(pady=10)

slots = []
for i in range(4):
    box = tk.Label(slot_frame, text=' ', bg='white',
                   width=6, height=2, relief='solid', borderwidth=1)
    box.pack(side='left', padx=3)
    slots.append(box)

secret = [random.choice(COLOURS) for _ in range(4)]

print('SECRET (for testing):', secret) #remove later

def count_blacks(guess, secret):
    blacks = 0
    for i in range(4):
        if guess[i] == secret[i]:
            blacks += 1
    return blacks

result_label = tk.Label(root, text='Pick 4 colours, then check',
                        font=('Arial', 12))
result_label.pack(pady=8)

guesses_used = 0
MAX_GUESSES = 8

def check_guess():
    global guesses_used

    if len(guess) < 4:
        result_label.config(text='Pick 4 colours first!')
        return
    
    guesses_used += 1
    blacks, whites = count_pegs(guess, secret)
    
    if blacks == 4:
        result_label.config(
            text=f'You win in {guesses_used} guesses!'
        )
    elif guesses_used >= MAX_GUESSES:
        result_label.config(
            text=f'Out of guesses! Code was {secret}'
        )
    else:
        left = MAX_GUESSES - guesses_used 
        result_label.config(
            text=f'Black: {blacks}  White: {whites} ({left} guesses left)'
        )
    clear_guess()

def new_game():
    global secret, guesses_used
    secret = [random.choice(COLOURS) for _ in range(4)]
    guesses_used = 0
    clear_guess()
    result_label.config(text='New game! Pick 4 colours.')
    print('SECRET (for testing):', secret)

new_btn = tk.Button(root, text='New Game', command=new_game)
new_btn.pack(pady=4)

def clear_guess():
    guess.clear()
    for box in slots:
        box.config(bg='white')

check_btn = tk.Button(root, text='Check', command=check_guess)
check_btn.pack(pady=4)

clear_btn = tk.Button(root, text='Clear', command=clear_guess)
clear_btn.pack(pady=4)

def count_pegs(guess, secret):
    secret_left = list(secret)
    guess_left = list(guess)

    blacks = 0
    whites = 0

    for i in range(3, -1, -1):
        if guess_left[i] == secret_left[i]:
            blacks += 1
            secret_left.pop(i)
            guess_left.pop(i)

    for colour in guess_left:
        if colour in secret_left:
            whites += 1
            secret_left.remove(colour)

    return blacks, whites

def count_pegs_advanced(guess, counter):
    blacks = sum(g == s for g, s in zip(guess, secret))

    secret_count = Counter(secret)
    guess_count = Counter(guess)
    total = sum(min(secret_count[c], guess_count[c]) for c in COLOURS)

    whites = total - blacks
    return blacks, whites


root.mainloop()
