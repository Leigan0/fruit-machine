import unittest
from mock import MagicMock
from app.Machine import Machine

class MachineTestSpec(unittest.TestCase):
    def setUp(self):
        self.mock_reel = MagicMock()
        self.machine = Machine(self.mock_reel)

    def test_machine_knows_its_own_default_prizefund_balance(self):
        self.assertEqual(self.machine.prizefund(), 0)

    def test_machine_can_have_float_value_set_at_creation(self):
        machine = Machine(self.mock_reel, 50)
        self.assertEqual(machine.prizefund(), 50)

    def test_machine_calls_spin_reel_method_on_reel_object(self):
        self.machine.spin_reel()
        self.assertTrue(self.machine.reel.spin_reel.called)

    def test_machine_calls_on_reel_object_to_confirm_if_prize_winning_reel(self):
        self.machine.release_funds()
        self.assertTrue(self.machine.reel.in_a_row.called)

    def test_machine_release_funds_method_returns_prize_fund_amount_if_win(self):
        self.machine.spin_reel()
        self.machine.spin_reel()
        self.machine.reel.in_a_row.return_value = True
        self.assertEqual(self.machine.release_funds(), (Machine.MINIMUM_BET*2))

    def test_machine_release_funds_method_returns_0_prize_fund_if_no_win(self):
        self.machine.spin_reel()
        self.machine.reel.in_a_row.return_value = False
        self.machine.reel.no_match.return_value = False
        self.assertEqual(self.machine.release_funds(), 0)

    def test_machine_releases_funds_with_confirmation_of_matching_row_row(self):
        self.machine.spin_reel()
        self.machine.reel.in_a_row.return_value = True
        self.assertEqual(self.machine.prizefund(), Machine.MINIMUM_BET)
        self.machine.release_funds()
        self.assertEqual(self.machine.prizefund(), 0)

    def test_machine_releases_half_funds_with_confirmation_of_no_match_row(self):
        self.machine.spin_reel()
        self.machine.reel.in_a_row.return_value = False
        self.machine.reel.no_match.return_value = True
        self.assertEqual(self.machine.prizefund(), Machine.MINIMUM_BET)
        # self.machine.reel.no_match.return_value = True
        self.machine.release_funds()
        self.assertEqual(self.machine.prizefund(), 0.5)

    def test_machine_does_not_releases_funds_with_confirmation_of_prize_row(self):
        self.machine.spin_reel()
        self.machine.reel.in_a_row.return_value = False
        self.machine.reel.no_match.return_value = False
        self.assertEqual(self.machine.prizefund(), Machine.MINIMUM_BET)
        self.machine.release_funds()
        self.assertEqual(self.machine.prizefund(), Machine.MINIMUM_BET)
