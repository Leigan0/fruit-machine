class Player:
    def __init__(self):
        self.funds = 10

    def debit(self, stake):
        self.funds -= stake

    def credit(self, stake):
        self.funds += stake

    def wallet(self):
        return self.funds
