import os

from kivy.lang import Builder
from kivy.resources import resource_find


class AppInfo:
    app_name = "Cash ExFlow"
    app_version = "1.1.0"
    app_icon = "Assets/icon.ico"
    app_data = f"{os. path. expanduser('~')}\\AppData\\Local\\Sunnymoon\\CashExFlow\\CashExFlow_database.db"
    default_folder_path = f"{os. path. expanduser('~')}\\Downloads"
    is_debug = True

    @staticmethod
    def GetDebugOrRelease(self, path):
        if self:
            Builder.load_file(path)
        else:
            main = resource_find(f'..\\{path}')
            Builder.load_file(main)
