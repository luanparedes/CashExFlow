import os
import sqlite3

from Helpers.AppInfo import AppInfo


class Dao:
   
    @staticmethod
    def create_database():
        app_data_local_path = f"{os. path. expanduser('~')}\\AppData\\Local"
        os.makedirs(f"{app_data_local_path}\\Sunnymoon\\CashExFlow", exist_ok=True)
        
        try:
            conn = sqlite3.connect(AppInfo.app_data)
            cursor = conn.cursor()
        
            sql = 'CREATE TABLE IF NOT EXISTS "Clients" ("Id" INTEGER NOT NULL UNIQUE, "Client" INTEGER NOT NULL, PRIMARY KEY("Id" AUTOINCREMENT))'
            cursor.execute(sql)

            sql = 'CREATE TABLE IF NOT EXISTS FolderPath ("id" INTEGER NOT NULL UNIQUE, "path" TEXT, PRIMARY KEY("id" AUTOINCREMENT))'
            cursor.execute(sql)
        
            sql = f"INSERT OR IGNORE INTO FolderPath (id, path) VALUES (1, '{AppInfo.default_folder_path}')"
            cursor.execute(sql)
        except:
            pass
        
        conn.commit()

    @staticmethod
    def save_folder_path(path):

        conn = sqlite3.connect(AppInfo.app_data)

        cursor = conn.cursor()

        sql = f'UPDATE FolderPath SET path = "{path}" WHERE id == 1'
        cursor.execute(sql)
        conn.commit()

    @staticmethod
    def get_folder_path():

        conn = sqlite3.connect(AppInfo.app_data)

        cursor = conn.cursor()

        sql = 'SELECT path FROM FolderPath WHERE id == 1'
        return cursor.execute(sql).fetchone()[0]
