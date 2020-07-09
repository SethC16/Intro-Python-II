from room import Room
from player import Player
from item import Item

# Declare all items

item = {
    'Worn Dagger': Item('Worn Dagger', 'An old rusty dagger.'),
    'Sword of Thousand Truths': Item('Sword of Thousand Truths', 'Sword destorys all.'),
    'Cloak over 9000': Item('Cloak over 9000', 'Cloak has unbearable power.'),
    'Boots of Blinding Speed': Item('Boots of Blinding Speed', 'You will be fast but blind.'),
    'The Gatekeepers Key': Item('The Gatekeepers Key', 'Must open something valuable.')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['Worn Dagger']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['Boots of Blinding Speed']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['Cloak over 9000']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['The Gatekeepers Key']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['Sword of Thousand Truths']),
}

# Link items to rooms
# room['outside'] = item['Worn Dagger']
# room['foyer'] = item['Boots of Blinding Speed']
# room['overlook'] = item['Cloak over 9000']
# room['narrow'] = item['The Gatekeepers Key']
# room['treasure'] = item['Sword of Thousand Truths']

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('What is your name adventurer?')

player = Player(name, current_room = room['outside'])

print(f'Welcome, {player.name}, Your current location is {player.current_room}')
# Write a loop that:
while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

    
    

# * Waits for user input and decides what to do.
    if player.current_room.item != None:
        print(f"You see {player.current_room.item.name}")
        pickup_item = input("Would you like to pick up the item (y or n)?:").lower()
        if pickup_item == "y" or pickup_item == "yes":
            player.get_item(player.current_room.item)
            player.current_room.item = None
            print(f"\n You now have:")
            for count, item in enumerate(player.item, 1):
                print(count, item)



    direction = input("What is your next action? (N to go north, S to go South, E to go East, W to go West, or Q to quit)").lower()


    if direction == "n":
        location = player.current_room.n_to
        if location != None:
            player.current_room = player.current_room.n_to
        else:
            print("There is no passage to the North, keep searching!")
    elif direction == "s":
        location = player.current_room.s_to
        if location != None:
            player.current_room = player.current_room.s_to
        else:
            print("There is no passage to the South, keep searching!")
    elif direction == "e":
        location = player.current_room.e_to
        if location != None:
            player.current_room = player.current_room.e_to
        else:
            print("There is no passage to the East, keep searching!")
    elif direction == "w":
        location = player.current_room.w_to
        if location != None:
            player.current_room = player.current_room.n_to
        else:
            print("There is no passage to the West, keep searching!")
    elif direction == "q":
        print("Farewell, adventurer!")
        exit()
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
