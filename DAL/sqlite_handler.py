import sqlite3
from sqlite3 import Error


class SqliteConnection:
    def __init__(self, db_file):
        self.db_file = db_file

    def __enter__(self):
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

        return conn

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        self.cursor.execute('SELECT * FROM parking_decision_logs')
        print(self.cursor.fetchall())
