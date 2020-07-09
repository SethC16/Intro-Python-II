# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.item = []

    def get_item(self, item):
        return self.item.append(item)

    def drop_item(self, item):
        return self.item.remove(item)

    def __str__(self):
        name = self.current_room.name
        description = self.current_room.description
        return f"{name} - {description}"

    
