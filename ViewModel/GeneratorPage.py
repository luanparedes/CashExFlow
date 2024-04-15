from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("View/GeneratorPage.kv")


class GeneratorPage(Screen):

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # endregion
