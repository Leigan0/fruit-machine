import random

class Reel:
    DEFAULT_SLOTS = ["black", "white", "green", "yellow"]

    def __init__(self):
        self.slots = Reel.DEFAULT_SLOTS
        self.reel = [None, None, None, None]

    def show_reel(self):
        return self.reel

    def spin_reel(self):
        for i in range(0, len(self.reel)):
            self.reel[i] = random.choice(self.slots)
