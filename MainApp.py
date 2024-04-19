import datetime

from kivymd.app import MDApp
from kivy.core.window import Window

from Control.Conditions import Conditions
from Control.ScreenManagement import ScreenManagement

Window.minimum_width, Window.minimum_height = (700, 500)

version = "v.1.0.0"

class MainApp(MDApp):
    def build(self):
        self.title = f"Cash ExFlow {version}"
        # self.icon = "Assets/logo.png"
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '300'
        self.theme_cls.theme_style = 'Dark'

        #print(Conditions.Pay10and25Condition(datetime.date(2024, 12, 25)))
        print(Conditions.Pay10and25Condition(datetime.date(2024, 5, 20)))
        print(Conditions.Pay02and15Condition(datetime.date(2024, 5, 20)))
        #print(Conditions.WeekendCondition(datetime.date(2024, 4, 20)))
        print(Conditions.AlwaysWednesdayCondition(datetime.date(2024, 4, 20)))
        print(Conditions.AlwaysThursdayCondition(datetime.date(2024, 4, 20)))
        print(Conditions.AlwaysFridayCondition(datetime.date(2024, 4, 20)))
        print(Conditions.EveryDay06Condition(datetime.date(2024, 4, 20)))
        print(Conditions.EveryDay06Condition(datetime.date(2024, 4, 2)))
        print(Conditions.EveryDay06Condition(datetime.date(2024, 4, 6)))
        print(Conditions.EveryDay06Condition(datetime.date(2024, 12, 1)))

        return ScreenManagement()


if __name__ == '__main__':
    MainApp().run()
