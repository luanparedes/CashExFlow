from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable

Builder.load_file("View/ClientsPage.kv")


class ClientsPage(Screen):

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data_tables = None

        self.initialize()

    # endregion

    # Private methods

    def initialize(self):
        self.data_tables = MDDataTable(
            use_pagination=False,
            check=False,
            background_color_cell="#155555",
            sorted_order="ASC",
            elevation=2,
            column_data=[
                ("Id", dp(8)),
                ("Cliente", dp(30)),
            ],
        )

        self.add_widget(self.data_tables)

    # endregion

    # Handlers

    def on_enter_clientsPage(self):
        pass

    # endregion