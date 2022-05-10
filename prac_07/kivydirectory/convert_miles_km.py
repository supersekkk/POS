from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_CONVERSION = 1.609344

class ConvertMilestoKm(App):
    output_km = StringProperty()

    def build(self):
        """Set up the layout for the Kivy-file"""
        self.title = "Convert miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_to_km(self, value):
        """Handle the main calculation of conversion rate"""
        try:
            result = float(value) * MILES_CONVERSION
            self.root.ids.output_label.text = str(result)
        except ValueError:
            return 0.0

    def down_one(self, value):
        """Handle the down-button, update text input"""
        try:
            down_result = float(value) - 1
            self.root.ids.first_text.text = str(down_result)
        except ValueError:
            return 0.0

    def up_one(self, value):
        """Handle the up-button, update text input"""
        try:
            up_result = float(value) + 1
            self.root.ids.first_text.text = str(up_result)
        except ValueError:
            return 0.0

    def convert_to_number(self, text):
        try:
            return float(text)
        except ValueError:
            return '0.0'

ConvertMilestoKm().run()