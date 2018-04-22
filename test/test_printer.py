import unittest
from app.Printer import Printer

class PrinterTestSpec(unittest.TestCase):
    def setUp(self):
        self.printer = Printer()

    def test_printer_can_format_list_to_output(self):
        input = ["red","green", "black", "blue"]
        self.assertEqual(self.printer.display_data(input),"Reel Spin Results: red green black blue")
