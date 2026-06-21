#define the fish and their values as two separate lists
fish_names = ['Trout', 'Salmon', 'Bass', 'Catfish', 'Shark']
fish_values = [5, 10, 15, 20, 50]

#define player's initial score and number of turns
score = 5
turns = 5

#print the instructions
print('Welcome! U have 5 turns to catch as many fishes as u can!')
print('Type "fish" to cast your line and "quit" to end the game.\n')

#loop each turn
for i in range(turns):
    print('Turn', i+1)
#get the player's input
action = input('What do u want to do?')

#check if player wants to quit
if action == 'fish':
    #choose a random fish name and value
    fish_index = random.randint(0, len(fish_names)-1)
    fish_name = fish_names[fish_index]
    fish_value = fish_values[fish_index]
    print('You caught a', fish_name, 'worth', fish_value, 'points!')
    #add the fish's value to player's score

#invalid inout
else:
    print('Invalid input. Type "fish" or "quit".')

#define the fish and their values as a list of dictionaries
fishes = [
    {'name': 'Trout', 'value': 5}
    {'name': 'Salmon', 'value': 10}
    {'name': 'Bass', 'value': 15}
    {'name': 'Catfish', 'value': 20}
    {'name': 'Shark', 'value': 50}
]

