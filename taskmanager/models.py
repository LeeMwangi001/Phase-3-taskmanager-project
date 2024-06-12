from datetime import datetime
from .database import get_db_connection

class Task:
    def __init__(self, title, description, due_date, completed=False, task_id=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

class TaskManager:
    @staticmethod
    def add_task(title, description, due_date):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO tasks (title, description, due_date, completed)
            VALUES (?, ?, ?, 0)
            """, (title, description, due_date))
            conn.commit()

    @staticmethod
    def list_tasks():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            rows = cursor.fetchall()
            tasks = [Task(row['title'], row['description'], row['due_date'], row['completed'], row['id']) for row in rows]
            return tasks

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
