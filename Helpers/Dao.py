import sqlite3

from Helpers.AppInfo import AppInfo


class Dao:

    @staticmethod
    def save_folder_path(path):
        if AppInfo.is_debug:
            conn = sqlite3.connect('CashExFlow_database.db')
        else:
            conn = sqlite3.connect(AppInfo.app_data)

        cursor = conn.cursor()

        sql = f'UPDATE FolderPath SET path = "{path}" WHERE id == 1'
        cursor.execute(sql)
        conn.commit()

    @staticmethod
    def get_folder_path():
        if AppInfo.is_debug:
            conn = sqlite3.connect('CashExFlow_database.db')
        else:
            conn = sqlite3.connect(AppInfo.app_data)

        cursor = conn.cursor()

        sql = 'SELECT path FROM FolderPath WHERE id == 1'
        return cursor.execute(sql).fetchone()[0]
