from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from Control.Dao import Dao

Builder.load_file("View/MainPage.kv")


class MainPage(Screen):

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # endregion
