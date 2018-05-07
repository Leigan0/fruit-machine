# coding: utf8
import unittest
import mock
import sys
from io import StringIO
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
    @mock.patch('app.Machine.Machine.prize_spin')
    def test_player_cannot_play_if_no_available_funds(self, jackpot_mock):
        jackpot_mock.return_value = False
        for i in range(0, Player.DEFAULT_FUNDS):
            self.gamerunner.spin_reel()

        with self.assertRaises(Exception): self.gamerunner.spin_reel()
        self.assertEqual(self.gamerunner.player.wallet(), 0)
        self.assertEqual(self.gamerunner.machine.prizefund(), (Player.DEFAULT_FUNDS))


    @mock.patch('random.choice', side_effect=["Black", "Black", "Black", "Blue"])
    def test_printer_prints_reel_to_std_out(self, reel_mock):
        out = StringIO()
        sys.stdout = out
        self.gamerunner.spin_reel()
        output = out.getvalue().strip()
        self.assertEqual(output, "Reel Spin Results: Black Black Black Blue")

    @mock.patch('random.choice', side_effect=["Black", "Black", "Black", "Black"])
    def test_printer_prints_reel_to_std_out_with_Jackpot(self, reel_mock):
        out = StringIO()
        sys.stdout = out
        self.gamerunner.spin_reel()
        output = out.getvalue().strip()
        self.assertEqual(output, "Reel Spin Results: Black Black Black Black\nJackpot winner £1 !!!!!!")
