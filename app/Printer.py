# coding: utf8
class Printer:

    def print_display(self, data):
        print(self.display_data(data))

    def display_prizefund(self, data):
        print(self._format_prizefund(data))

    def display_loss(self):
        print("Unlucky, try again?")

    def display_data(self,data):
        return self._header() + self._format_data(data)

    def _format_prizefund(self,data):
        return "Jackpot win £%s !!!!!!" %data

    def _format_data(self,data):
        return ' '.join(data)

    def _header(self):
        return 'Reel Spin Results: '
