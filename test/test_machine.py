import unittest
import mock
from app.Machine import Machine

class MachineTestSpec(unittest.TestCase):
    def setUp(self):
        self.reel = mock.MagicMock()
        self.machine = Machine()

    def test_machine_knows_its_own_prizefund_balance(self):
        self.assertEqual(self.machine.prizefund(), 0)
