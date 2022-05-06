from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("Greet")
        your_name = self.root.ids.input_name.text       #get the user input and assign to your_name
        self.root.ids.output_label.text = "Hello, " + your_name   #change the label to greet the user

    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"



if __name__ == '__main__':
    BoxLayoutDemo().run()
