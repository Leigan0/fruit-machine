class Player:
    def __init__(self):
        self.wallet = 10

    def debit(self, stake):
        self.wallet -= stake
