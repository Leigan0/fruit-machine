import unittest
from app.Game import Game

class GameTestSpec(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_has_default_slots_at_initalization(self):
        self.assertEqual(self.game.slots, Game.DEFAULT_SLOTS)

    def test_game_reel_returns_array_with_four_colours(self):
        self.assertEqual(self.game.reel(), ['black', 'black', 'black', 'black'])
