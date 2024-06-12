import sqlite3

def connect():
    return sqlite3.connect("tasks.db")

def create_tables():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
        """)
        conn.commit()
