# coding: utf8
class Player:
    DEFAULT_FUNDS = 10  # type: int
    def __init__(self):
        self.funds = Player.DEFAULT_FUNDS

    def debit(self, stake):
        self._insufficient_funds_check(stake)
        self.funds -= stake

    def credit(self, stake):
        self.funds += stake


    def wallet(self):
        return self.funds

    def _insufficient_funds_check(self,stake):
        if self.funds < stake:
            raise Exception("Insufficient Funds Available")
