from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from Helpers.PageEnum import PageEnum
from ViewModel.MainPage import MainPage
from ViewModel.SettingsPage import SettingsPage


class ScreenManagement(ScreenManager):
    screen = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.transition = FadeTransition()
        self.transition.duration = 0.7

        self.main_screen = MainPage()
        self.add_widget(self.main_screen)

        self.settings_screen = SettingsPage()
        self.add_widget(self.settings_screen)

    def on_screen(self, instance, value):
        if value == PageEnum.SettingsPage:
            self.current = self.settings_screen.name
        elif value == PageEnum.MainPage:
            self.current = self.main_screen.name
