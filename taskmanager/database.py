import sqlite3

DATABASE_FILE = "taskmanager.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
        owner_id INTEGER,
        FOREIGN KEY (owner_id) REFERENCES users (id)
    )
    """)

    conn.commit()
    conn.close()
