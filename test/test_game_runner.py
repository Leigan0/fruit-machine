import unittest
from mock import MagicMock
from app.Game_Runner import GameRunner


class GameRunnerTestSpec(unittest.TestCase):
    def setUp(self):
        self.mock_machine = MagicMock()
        self.mock_player = MagicMock()
        self.GameRunner = GameRunner(self.mock_machine, self.mock_player)

    def test_game_can_return_player(self):
        self.assertEqual(self.GameRunner.player, self.mock_player)
