import datetime
import os
import shutil
import pathlib

from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager

from Control.ExcelService import ExcelService

Builder.load_file("View/GeneratorPage.kv")


class GeneratorPage(Screen):
    # region Properties and variables

    filePath = StringProperty()
    folderPath = StringProperty()
    copyPath = StringProperty()
    generateDisabled = BooleanProperty(True)

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
        self.copyPath = f"{self.folderPath}{self.create_file_name()}"
        shutil.copyfile(self.filePath, self.copyPath)

    def generate_file(self):
        excel = ExcelService(self.copyPath)
        excel.create_spreadsheet()

    @staticmethod
    def create_file_name():
        time = datetime.datetime.now()
        year = time.strftime("%Y")
        month = time.strftime("%m")
        day = time.strftime("%d")
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S")

        return f"Cashflow_{year}-{month}-{day}_{hour}{minute}{second}.xlsx"

    # endregion

    # region Handlers

    def get_file_action(self):
        self._open_file_manager()

        if self.copyPath is not None:
            self.generateDisabled = False

    def generate_excel_action(self):
        self.copy_file()
        self.generate_file()

    def select_path(self, path: str):
        self.filePath = path
        parentPath = pathlib.Path(self.filePath).parent
        self.folderPath = f"{parentPath}\\"
        self.exit_manager()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    # endregion
