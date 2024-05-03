import os

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager

from Helpers.AppInfo import AppInfo
from Helpers.PageEnum import PageEnum

Builder.load_file("View/SettingsPage.kv")


class SettingsPage(Screen):
    folder_path = StringProperty()

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = PageEnum.SettingsPage
        self.folder_path = f"[u][ref={AppInfo.folder_path}]{AppInfo.folder_path} [/ref][u]"


    # endregion

    def navigate_to_main_screen(self):
        self.parent.screen = PageEnum.MainPage

    def select_path(self, path: str):
        self.folder_path = path
        AppInfo.folder_path = path
        self.exit_manager()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
        pass

    def open_file_manager(self):
        path = os.path.expanduser(AppInfo.folder_path)  # path to the directory that will be opened in the file manager

        self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path, )
        self.file_manager.selector = "folder"
        self.file_manager.use_access = True
        self.file_manager.sort_by = 'date'
        self.file_manager.ext = [""]

        self.file_manager.show(path)

    # endregion
