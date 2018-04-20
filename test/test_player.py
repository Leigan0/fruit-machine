import unittest
from app.Player import Player

class PlayerTestSpec(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_player_has_initial_wallet_of_10(self):
        self.assertTrue(self.player.wallet, 10)
