import random
import time

with open('dictionary.txt', 'r') as file:
    words = file.readlines()
words = [word.strip() for word in words]
print(words)

#define the player's initial score and the number of turns
score = 0
turns = 5

#define the time limit for catching a fish in seconds
time_limit = 5

#print the instructions
print('Welcome to the fishing game! You have 5 turns to catch as many fishes as you can.')
print('Type "fish" to cast your line and "quit" to exit the game.\n')

#loop thru each turn
for i in range(turns):
    print('Turn', i+1)

    #get the player's input and start the timer
    action = input('What do you want to do?')

    #check if the player wants to quit
    if action == 'quit':
        print('Thanks for playing!')
        break

    #check if the player wants to fish
    if action == 'fish':
        word = random.choice(words)
        print('Type', word, ':')

        start_time = time.time()

        typed = input('Your input:')

        end_time = time.time()

        time_taken = end_time - start_time

        print(f'n\Time taken: {time_taken:.2f} seconds')

        if typed == word:
            print('Correct!')

            if time_taken <= 2:
                points = 10
            elif time_taken <= 4:
                points = 7
            elif time_taken <= 6:
                points = 5
            else:
                points = 2

            print('Points earned:', points)

        else:
                print('Wrong!')
                print('Points earned: 0')

                break


print('Type "fish" or "quit".')

print('Score:', score, '\n')

#print the final score
print('Final score:', score)

