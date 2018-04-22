# coding: utf8
class Printer:

    def print_display(self, data):
        print(self.display_data(data))

    def display_prizefund(self, data):
        print(_format_prizefund())

    def display_data(self,data):
        return self._header() + self._format_data(data)

    def _format_prizefund(self,data):
        return "Jackpot winner £%s !!!!!!" %data

    def _format_data(self,data):
        return ' '.join(data)

    def _header(self):
        return 'Reel Spin Results: '
