import datetime

from kivymd.app import MDApp
from kivy.core.window import Window

from Control.ScreenManagement import ScreenManagement

Window.minimum_width, Window.minimum_height = (700, 500)

version = "v.1.0.0"


class App(MDApp):
    def build(self):
        self.title = f"Cash ExFlow {version}"
        self.icon = "Assets/Logo_36x36.png"
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '300'
        self.theme_cls.theme_style = 'Dark'

        return ScreenManagement()


if __name__ == '__main__':
    App().run()
