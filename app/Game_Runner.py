from app.Printer import Printer

class GameRunner:

    def __init__(self, machine, player, printer=Printer()):
        self.player = player
        self.machine = machine
        self.printer = printer

    def spin_reel(self):
        self.player.debit(self.machine.MINIMUM_BET)
        self.printer.print_display(self.machine.spin_reel())
        if (self.machine.prize_spin()) == True:
            prize = self.machine.release_funds()
            self.printer.display_prizefund(prize)
            self.player.credit(prize)
