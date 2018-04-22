class Printer:

    def print_display(self, data):
        print(display_data(data))

    def display_data(self,data):
        return self._header() + self._format_data(data)

    def _format_data(self,data):
        return ' '.join(data)

    def _header(self):
        return 'Reel Spin Results: '
