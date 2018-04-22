import unittest
from app.Player import Player

class PlayerTestSpec(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.minimum_bet = 1

    def test_player_has_initial_wallet_of_10(self):
        self.assertEqual(self.player.wallet(), Player.DEFAULT_FUNDS)

    def test_debit_method_reduces_balance_by_debit_amount(self):
        self.player.debit(1)
        self.assertEqual(self.player.wallet(), Player.DEFAULT_FUNDS-self.minimum_bet)

    def test_debit_method_reduces_balance_by_correct_debit_amount(self):
        stake = 4
        self.player.debit(stake)
        self.assertNotEqual(self.player.wallet(), Player.DEFAULT_FUNDS)
        self.assertEqual(self.player.wallet(), Player.DEFAULT_FUNDS-stake)

    def test_player_debit_will_throw_error_if_insufficient_funds(self):
        with self.assertRaises(Exception): self.player.debit(Player.DEFAULT_FUNDS+self.minimum_bet)
        self.assertEqual(self.player.wallet(), Player.DEFAULT_FUNDS)

    def test_credit_method_increases_balance_by_correct_debit_amount(self):
        stake = 4
        self.player.credit(stake)
        self.assertNotEqual(self.player.wallet(), Player.DEFAULT_FUNDS)
        self.assertEqual(self.player.wallet(), Player.DEFAULT_FUNDS+stake)
