import unittest
import mock
from app.Reel import Reel

class ReelTestSpec(unittest.TestCase):
    def setUp(self):
        self.reel = Reel(4)

    def test_reel_has_default_slots_at_initalization(self):
        self.assertEqual(self.reel.slots, Reel.DEFAULT_SLOTS)

    def test_reel_returns_array_with_correct_number_of_slots(self):
        self.assertEqual(self.reel.reel(), [None, None, None, None])

    def test_spin_reel_updates_reel_attribute(self):
        self.reel.spin_reel()
        self.assertNotEqual(self.reel.reel(), [None, None, None, None])

    def test_spin_reel_updates_reel_attributes_with_items_from_default_slots(self):
        self.reel.spin_reel()
        self.assertTrue(set(self.reel.reel()).issubset(Reel.DEFAULT_SLOTS))

    @mock.patch('random.choice')
    def test_spin_reel_selects_each_slot_using_random_choice(self, choice_mock):
        choice_mock.return_value = "black"
        self.reel.spin_reel()
        self.assertEqual(self.reel.reel(), ["black", "black", "black", "black"])

    @mock.patch('random.choice')
    def test_spin_reel_selects_each_slot_using_random_choice(self, choice_mock):
        choice_mock.return_value = "white"
        self.reel.spin_reel()
        self.assertEqual(self.reel.reel(), ["white", "white", "white", "white"])

    @mock.patch('random.choice')
    def test_all_items_match_method_returns_true_if_matching_slots(self, choice_mock):
        choice_mock.return_value = "white"
        self.reel.spin_reel()
        self.assertTrue(self.reel.in_a_row())

    @mock.patch('random.choice', side_effect=["Black", "Yellow", "Blue", "Green"])
    def test_all_items_match_method_returns_false_if_not_all_slots_matching_slots(self, choice_mock):
        self.reel.spin_reel()
        self.assertFalse(self.reel.in_a_row())
