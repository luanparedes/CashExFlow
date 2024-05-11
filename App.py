import os
import sys

from kivy.resources import resource_add_path
from kivymd.app import MDApp
from kivy.core.window import Window

from Control.ScreenManagement import ScreenManagement
from Helpers.AppInfo import AppInfo
from Helpers.Dao import Dao

Window.minimum_width, Window.minimum_height = (700, 500)


class App(MDApp):

    def build(self):
        self.title = f"{AppInfo.app_name} {AppInfo.app_version}"
        self.icon = AppInfo.app_icon
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '300'
        self.theme_cls.theme_style = 'Dark'

        Dao.create_database()
        
        return ScreenManagement()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    App().run()
