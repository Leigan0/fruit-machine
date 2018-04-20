import random

class Reel:
    DEFAULT_SLOTS = ["black", "white", "green", "yellow"]

    def __init__(self, reel_size):
        self.slots = Reel.DEFAULT_SLOTS
        self._reel = []
        self.build_reel(reel_size)

    def reel(self):
        return self._reel

    def spin_reel(self):
        for i in range(0, len(self._reel)):
            self._reel[i] = random.choice(self.slots)

    def build_reel(self, reel_size):
        for i in range(0, reel_size):
            self._reel.append(None)
