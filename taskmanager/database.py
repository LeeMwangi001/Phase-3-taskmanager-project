import sqlite3

DATABASE_FILE = "taskmanager.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  
    return conn

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)

        # Tasks table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            owner_id INTEGER,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
            FOREIGN KEY (owner_id) REFERENCES users(id)
        )
        """)

        # Task_assignments table with composite key
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS task_assignments (
            task_id INTEGER,
            user_id INTEGER,
            PRIMARY KEY (task_id, user_id),
            FOREIGN KEY (task_id) REFERENCES tasks(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)

        conn.commit()
