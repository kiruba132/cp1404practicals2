from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """A Kivy App that dynamically creates Labels for a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Build the GUI layout and dynamically add Label widgets."""
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            self.add_label(name)
        return self.root

    def add_label(self, name):
        """Create and add a Label to the layout (SRP: isolated label creation logic)."""
        label = Label(text=name)
        self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
