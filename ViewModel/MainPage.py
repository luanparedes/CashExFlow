from kivy.app import App as kivyApp
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu

from Helpers.AppInfo import AppInfo
from ViewModel.AboutCard import AboutCard
from ViewModel.GeneratorPage import GeneratorPage

AppInfo.GetDebugOrRelease(AppInfo.is_debug, 'View\\MainPage.kv')


class MainPage(Screen):
    menu_items = []
    test = ObjectProperty()

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.card = None

    def open_menu(self, button):
        self.menu_items.clear()
        self.fill_menu()

        self.menu = MDDropdownMenu(
            items=self.menu_items,
            width_mult=4,
        )
        self.menu.caller = button
        self.menu.open()

    def fill_menu(self):
        """self.menu_items.append({
            "text": "Configurações",
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "on_release": self.open_settings
        })"""
        self.menu_items.append({
            "text": "Sobre...",
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "on_release": self.set_isOpen
        })
        self.menu_items.append({
            "text": "Sair",
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "on_release": self.exit_login
        })

    def open_settings(self):
        self.parent.screen = 'settings'
        self.menu.dismiss()

    def exit_login(self):
        kivyApp.get_running_app().stop()

    def set_isOpen(self):
        self.card = AboutCard()
        self.card.bind(isOpen=self.on_change_card)
        self.card.isOpen = True

    def on_change_card(self, obj, value):
        if self.card.isOpen:
            self.add_widget(self.card)
        else:
            self.remove_widget(self.card)
        self.menu.dismiss()

    def on_enter_page(self):
        #self.children(GeneratorPage())
        self.add_widget(GeneratorPage())

    # endregion
