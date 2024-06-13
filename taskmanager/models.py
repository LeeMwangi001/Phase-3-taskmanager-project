# taskmanager/models.py

from taskmanager.database import get_db_connection

class User:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def add_user(name):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
            conn.commit()

    @staticmethod
    def get_user_id(name):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE name = ?", (name,))
            user = cursor.fetchone()
            return user['id'] if user else None

    @staticmethod
    def list_users():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()


class Task:
    def __init__(self, title, description, due_date, owner_id):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.owner_id = owner_id

    @staticmethod
    def add_task(title, description, due_date, owner_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tasks (title, description, due_date, owner_id, completed)
                VALUES (?, ?, ?, ?, 0)
            """, (title, description, due_date, owner_id))
            conn.commit()

    @staticmethod
    def list_tasks():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            return cursor.fetchall()

    @staticmethod
    def update_task(task_id, title, description, due_date):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tasks
                SET title = ?, description = ?, due_date = ?
                WHERE id = ?
            """, (title, description, due_date, task_id))
            conn.commit()

    @staticmethod
    def delete_task(task_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()

    @staticmethod
    def mark_task_complete(task_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
            conn.commit()


class TaskAssignment:
    @staticmethod
    def assign_task(task_id, user_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO task_assignments (task_id, user_id)
                VALUES (?, ?)
            """, (task_id, user_id))
            conn.commit()
