from kivy.properties import BooleanProperty, NumericProperty, ListProperty, StringProperty
from kivymd.uix.card import MDCard

from Helpers.AppInfo import AppInfo

AppInfo.GetDebugOrRelease(AppInfo.is_debug, 'View\\AboutCard.kv')


class AboutCard(MDCard):
    app_version = StringProperty(f'Versão {AppInfo.app_version}')
    isOpen = BooleanProperty(False)
    card_size = ListProperty([0, 0])
    button_size = ListProperty([0, 0])
    text_button_size = NumericProperty()

    def __init__(self, **kwargs):
        super(AboutCard, self).__init__(**kwargs)

        self.set_card_size()
        self.set_button_size()
        self.set_text_button_size()

    def isOpen_check(self):
        self.isOpen = False

    # Properties setters
    def set_card_size(self):
        self.card_size = [.7, .7]

    def set_button_size(self):
        self.button_size = [.1, .1]

    def set_text_button_size(self):
        self.text_button_size = 16

    # on_<property_name> vai fazer o que precisa quando for alterado
    def on_isOpen(self, obj, value):
        print('Entrando no menu "Sobre"!')
