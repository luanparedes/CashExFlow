import datetime
import os
import shutil

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager

from Control.ExcelService import ExcelService

Builder.load_file("View/GeneratorPage.kv")


class GeneratorPage(Screen):
    # region Properties and variables

    folderPath = ObjectProperty()
    copyPath = ObjectProperty()

    # endregion

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # endregion

    # region Methods

    def _open_file_manager(self, is_saving=False):
        path = os.path.expanduser("~")  # path to the directory that will be opened in the file manager
        self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path, )

        if is_saving:
            self.file_manager.selector = "folder"
        else:
            self.file_manager.selector = "file"

        self.file_manager.show(path)

    def copy_file(self):
        date = datetime.date.today()
        new_file_name = (f"Cashflow_{date.year}-{date.month}-{date.day}_"
                         f"014430.xlsx")

        self.copyPath = f"C:\\Users\\luans\\Downloads\\{new_file_name}"

        shutil.copyfile(self.folderPath, self.copyPath)

        ExcelService.create_row_realpay(self.copyPath)

    # endregion

    # region Handlers

    def try_button_click(self):
        self._open_file_manager()

    def select_path(self, path: str):
        self.folderPath = path
        self.exit_manager()
        self.copy_file()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    # endregion
