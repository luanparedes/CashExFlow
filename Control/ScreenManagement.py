from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, FadeTransition


class ScreenManagement(ScreenManager):
    screen = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.transition = FadeTransition()
        self.transition.duration = 0.7

        #self.select_screen = SelectFilesScreen(name=ScreenEnum.SELECT_FILES)
        #self.workbook_screen = MainWorkbookScreen(name=ScreenEnum.MAIN_WORKBOOK)

        #self.add_widget(self.select_screen)
        #self.add_widget(self.workbook_screen)

        #self.current = self.select_screen.name

    def on_screen(self, instance, value):
        self.current = value
