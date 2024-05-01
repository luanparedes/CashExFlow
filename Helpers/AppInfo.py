from kivy.lang import Builder
from kivy.resources import resource_find


class AppInfo:
    app_name = "Cash ExFlow"
    app_version = "1.0.5"
    app_icon = "Assets/icon.ico"
    is_debug = True

    @staticmethod
    def GetDebugOrRelease(self, path):
        if self:
            Builder.load_file(path)
        else:
            main = resource_find(f'..\\{path}')
            Builder.load_file(main)
