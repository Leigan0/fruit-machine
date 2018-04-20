class Game:
    DEFAULT_SLOTS = ["black", "white", "green", "yellow"]

    def __init__(self):
        self.slots = Game.DEFAULT_SLOTS

    def reel(self):
        return ['black', 'black', 'black', 'black']
