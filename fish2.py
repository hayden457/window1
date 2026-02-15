import random
import time

fishes = (
    ('Trout', 5),
    ('Salmon', 10),
    ('Bass', 15),
    ('Catfish', 20),
    ('Shark', 50)
)

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
        print('Type any word to catch a fish!')
        start_time = time.time()

        #wait for the player to enter the word within the time limit
        while True:
            input_word = input()
            end_time = time.time()
            time_taken = end_time - start_time

            #check if the player typed the word within the time limit
            if time_taken <= time_limit:
                #choose a random fish from the list
                fish = random.choice(fishes)
                print('You caught a', fish[0], 'worth', fish[1], 'points!')
                #add the fish's value to the player's score
                score += fish[1]
                break
            else:
                print('Sorry you took too long to cath a fish!')
                break

    #invalid input
    else:
        print('Invalid input. Type "fish" or "quit".')

    print('Score:', score, '\n')

#print the final score
print('Final scofrfe:', score)

