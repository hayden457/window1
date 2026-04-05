import random

secret = [random.choice(COLOURS) for _ in range(PEGS)]

blacks = 0
for i in range(PEGS):
    if guess[i] == secret[i]:
        blacks += 1

from collections import Counter

secret_counts = Counter(secret)
guess_counts = Counter(guess)

total_matched = sum(min(secret_counts[c], guess_counts[c]) for c in COLOURS)

whites = total_matched - blacks

from collections import Counter

def get_feedback(secret, guess):
    black = 0
    for i in range(PEGS):
        if guess[i] == secret[i]:
            black += 1

    secret_counts = Counter(secret)
    guess_counts = Counter(guess)
    total_matched = sum(min(secret_counts[c], guess_counts[c]) for c in COLOURS)
    whites = total_matched - blacks

    return blacks, whites
