import sqlite3

class Database:
    def __init__(self, db_name="tarefas.db"):
        self.db_name = db_name

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def init_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                concluido BOOLEAN NOT NULL DEFAULT 0
            )
        """)
        conn.commit()
        conn.close()

database = Database()