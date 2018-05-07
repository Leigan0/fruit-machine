import unittest
import mock
from app.Game_Runner import GameRunner
from app.Machine import Machine
from app.Player import Player
from app.Printer import Printer
from app.Reel import Reel

class GamePlayIntegrationTestSpec(unittest.TestCase):
    def setUp(self):
        self.printer = Printer()
        self.player = Player()
        self.machine = Machine(Reel)
        self.gamerunner = GameRunner(self.machine, self.player, self.printer)

    @mock.patch('random.choice', side_effect=["Black", "Yellow", "Blue", "Green"])
    def test_player_machine_credit_balance_reduces_on_nonprizereel_spin(self, jackpot_mock):
        self.gamerunner.spin_reel()
        self.assertEqual(self.gamerunner.player.wallet(), (Player.DEFAULT_FUNDS-Machine.MINIMUM_BET))
        self.assertEqual(self.gamerunner.machine.prizefund(), (Machine.MINIMUM_BET))

    @mock.patch('random.choice', side_effect=["Black", "Black", "Black", "Black"])
    def test_player_credit_balance_increases_on_prizereel_spin(self, slot_mock):
        self.gamerunner.spin_reel()
        # Wallet will be default as game jackpot funds spent
        self.assertEqual(self.gamerunner.player.wallet(), Player.DEFAULT_FUNDS)
        self.assertEqual(self.gamerunner.machine.prizefund(), 0)
    #
    # def test_player_cannot_play_if_no_available_funds(self):
