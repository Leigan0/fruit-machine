from app.Reel import Reel

class Machine:
    MINIMUM_BET = 1
    def __init__(self, reel_object=Reel):
        self._prizefund = 0
        self.reel = reel_object()

    def prizefund(self):
        return self._prizefund

    def spin_reel(self):
        self._prizefund += Machine.MINIMUM_BET
        return self.reel.spin_reel()

    def release_funds(self):
        debit_amount = self._prizefund
        if self.prize_spin():
            self._prizefund = 0
            return debit_amount
        else:
            return 0

    def prize_spin(self):
        return self.reel.in_a_row()
