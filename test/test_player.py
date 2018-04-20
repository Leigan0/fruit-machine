import unittest
from app.Player import Player

class PlayerTestSpec(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_player_has_initial_wallet_of_10(self):
        self.assertEqual(self.player.wallet, 10)

    def test_debit_method_reduces_balance_by_debit_amount(self):
        self.player.debit(1)
        self.assertEqual(self.player.wallet, 9)

    def test_debit_method_reduces_balance_by_correct_debit_amount(self):
        self.player.debit(4)
        self.assertNotEqual(self.player.wallet, 1)
        self.assertEqual(self.player.wallet, 6)
