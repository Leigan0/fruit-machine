# coding: utf8
from app.Reel import Reel

class Machine:
    MINIMUM_BET = 1

    def __init__(self, reel_object=Reel, float=0):
        self._prizefund = float
        self.reel = reel_object()

    def prizefund(self):
        return self._prizefund

    def spin_reel(self):
        self._prizefund += Machine.MINIMUM_BET
        return self.reel.spin_reel()

    def release_funds(self):
        debit_amount = self._prizefund
        if self.reel.in_a_row():
            self._prizefund = 0
            return debit_amount
        elif self.reel.no_match():
            self._prizefund = float(self._prizefund)/2
            return self._prizefund
        else:
            return 0

    def prize_spin(self):
        return(self.reel.in_a_row() or self.reel.no_match())
