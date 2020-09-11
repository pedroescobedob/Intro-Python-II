# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, player, currentRoom):
        self.player = player
        self.currentRoom = currentRoom

    def move(self, direction):
        self.direction = direction