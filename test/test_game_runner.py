import unittest
from mock import MagicMock
from app.Game_Runner import GameRunner


class GameRunnerTestSpec(unittest.TestCase):
    def setUp(self):
        self.mock_printer = MagicMock()
        self.mock_machine = MagicMock()
        self.mock_player = MagicMock()
        self.gamerunner = GameRunner(self.mock_machine, self.mock_player, self.mock_printer)

    def test_game_can_return_player(self):
        self.assertEqual(self.gamerunner.player, self.mock_player)

    def test_game_can_return_machine(self):
        self.assertEqual(self.gamerunner.machine, self.mock_machine)

    def test_game_can_return_printer(self):
        self.assertEqual(self.gamerunner.printer, self.mock_printer)

    def test_game_calls_spin_reel_method_on_machine_object(self):
        self.gamerunner.spin_reel()
        self.assertTrue(self.gamerunner.machine.spin_reel.called)

    def test_game_calls_debit_method_on_player_object(self):
        self.gamerunner.spin_reel()
        self.assertTrue(self.gamerunner.player.debit.called)

    def test_game_calls_print_display_method_on_printer_object(self):
        self.gamerunner.spin_reel()
        self.assertTrue(self.gamerunner.printer.print_display.called)

    def test_game_calls_print_jackpot_display_if_prize_spin(self):
        self.gamerunner.machine.prize_spin.return_value = True
        self.gamerunner.spin_reel()
        self.assertTrue(self.gamerunner.printer.display_prizefund.called)
