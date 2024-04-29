from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from ViewModel.MainPage import MainPage


class ScreenManagement(ScreenManager):
    screen = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.transition = FadeTransition()
        self.transition.duration = 0.7

        self.select_screen = MainPage()
        self.add_widget(self.select_screen)

    def on_screen(self, instance, value):
        self.current = value
