import unittest
from mock import MagicMock
from app.Machine import Machine

class MachineTestSpec(unittest.TestCase):
    def setUp(self):
        self.mock_reel = MagicMock()
        self.machine = Machine(self.mock_reel)

    def test_machine_knows_its_own_prizefund_balance(self):
        self.assertEqual(self.machine.prizefund(), 0)

    def test_machine_prize_fund_increases_by_default_bet_with_reel_spin(self):
        self.machine.spin_reel()
        self.assertEqual(self.machine.prizefund(), Machine.MINIMUM_BET)

    def test_machine_calls_spin_reel_method_on_reel_object(self):
        self.machine.spin_reel()
        self.assertTrue(self.machine.reel.spin_reel.called)

    def test_machine_calls_on_reel_object_to_confirm_if_prize_winning_reel(self):
        self.machine.release_funds()
        self.assertTrue(self.machine.reel.in_a_row.called)

    def test_machine_releases_funds_with_confirmation_of_prize_row(self):
        self.machine.spin_reel()
        self.machine.reel.in_a_row.return_value = True
        self.assertEqual(self.machine.prizefund(), Machine.MINIMUM_BET)
        self.machine.release_funds()
        self.assertEqual(self.machine.prizefund(), 0)

    def test_machine_does_not_releases_funds_with_confirmation_of_prize_row(self):
        self.machine.spin_reel()
        self.machine.reel.in_a_row.return_value = False
        self.assertEqual(self.machine.prizefund(), Machine.MINIMUM_BET)
        self.machine.release_funds()
        self.assertEqual(self.machine.prizefund(), Machine.MINIMUM_BET)
