from app.Machine import Machine
from app.Player import Player

class GameRunner:

    def __init__(self, machine=Machine, player=Player):
        self.player = player
        self.machine = machine

    def spin_reel(self):
        self.player.debit()
        self.machine.spin_reel()
