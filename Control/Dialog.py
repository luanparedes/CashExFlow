from kivy.properties import NumericProperty, Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar


class Dialog:
    dialog = None
    progress_bar = None
    progress_value = 0
    radius_value = 18

    def __init__(self, dialog_type, **kwargs):
        super().__init__(**kwargs)

        self.dialog_type = dialog_type
        self.call_dialog_type()

    def call_dialog_type(self):
        if self.dialog_type == TypeDialog.ProgressDialog:
            self.create_progress_dialog()
        if self.dialog_type == TypeDialog.FinishDialog:
            self.create_finished_dialog()

    def create_progress_dialog(self):
        self.progress_bar = MDProgressBar(value=self.progress_value)

        self.dialog = MDDialog(
            title="Criando nova planilha...",
            type="custom",
            content_cls=MDBoxLayout(
                self.progress_bar,
                orientation="vertical",
                spacing="12dp",
                size_hint_y=None,
                height="15dp",
            ),
            buttons=[MDFlatButton()],
            radius=[self.radius_value, self.radius_value, self.radius_value, self.radius_value]
        )

        Clock.schedule_interval(self.run_timer, 0.05)

    def create_finished_dialog(self):
        pass

    def run_timer(self, dt):
        self.progress_bar.value += 1
        if self.progress_bar.value >= 100:
            self.close()

    def open(self):
        self.dialog.open()

    def close(self):
        self.dialog.dismiss()


class TypeDialog:
    ProgressDialog = "progress"
    FinishDialog = "finish"
