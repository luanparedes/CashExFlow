import sqlite3


class Dao:

    sql = ""
    connection = None
    cursor = None

    def ConnectDatabase(self):
        self.connection = sqlite3.connect("CashExflow_database.db")
        self.cursor = self.connection.cursor()

    def DisconnectDatabase(self):
        self.connection.close()

    def AddNewClient(self, client):
        self.ConnectDatabase()

        self.sql = f'INSERT INTO Clients (Client) VALUES ("{client}")'
        self.cursor.execute(self.sql)
        self.connection.commit()

        self.DisconnectDatabase()
