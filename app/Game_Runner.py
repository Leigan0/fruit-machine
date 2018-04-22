from app.Machine import Machine
from app.Player import Player
from app.Printer import Printer

class GameRunner:

    def __init__(self, machine=Machine, player=Player, printer=Printer):
        self.player = player
        self.machine = machine
        self.printer = printer

    def spin_reel(self):
        self.player.debit()
        self.machine.spin_reel()
