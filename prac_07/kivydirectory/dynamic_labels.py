from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

name_list = []


class DynamicLabels(App):

    def __init__(self):
        name_list = []

    def build(self):
        self.title = "Labels dynamic"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()

    def create_widgets(self):
        for name in self.name_list:
            temp_button = Button(Text=name)
            temp_button.bind(on_release=self.temp_button)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicLabels().run()

 #   temp_button = Button(Text=name)
 #   self.root.ids.entries_box.add_widget(temp_button)
 #   temp_button.bind(on_release=self.press_entry)




