import datetime
import os
import shutil
import pathlib

from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar.snackbar import MDSnackbar

from Control.Dialog import Dialog, TypeDialog
from Control.ExcelService import ExcelService
from Helpers.AppInfo import AppInfo
from Helpers.Dao import Dao

AppInfo.GetDebugOrRelease(AppInfo.is_debug, 'View\\GeneratorPage.kv')


class GeneratorPage(Screen):
    # region Properties and variables

    filePath = StringProperty()
    folderPath = StringProperty()
    copyPath = StringProperty()
    generateDisabled = BooleanProperty(True)

    dialog = None
    
    # endregion

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.user_folder = Dao.get_folder_path()

    # endregion

    # region Methods

    def _open_file_manager(self):
        path = os.path.expanduser(self.user_folder)  # path to the directory that will be opened in the file manager

        self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path, )
        self.file_manager.use_access = True
        self.file_manager.sort_by = 'date'
        self.file_manager.ext = [".xlsx"]
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

        self.dialog = Dialog(dialog_type=TypeDialog.ProgressDialog)

        # When dismiss dialog, it calls this callback
        self.dialog.dialog.on_dismiss = self.dialog_close_callback
        self.dialog.open()

        self.generate_file()

    def dialog_close_callback(self, *args):
        self.filePath = ""
        self.generateDisabled = True

        snackbar = MDSnackbar()
        snackbar.md_bg_color = (.0, .255, .128, 1)
        snackbar.add_widget(MDLabel(text=f"Arquivo criado com sucesso em {self.copyPath}"))
        snackbar.open()

    def select_path(self, path: str):
        self.filePath = path
        parentPath = pathlib.Path(self.filePath).parent
        self.folderPath = f"{parentPath}\\"
        self.exit_manager()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    # endregion
