from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("View/MainWorkbookScreen.kv")


class MainWorkbookScreen(Screen):

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # endregion
