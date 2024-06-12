from taskmanager.database import get_db_connection, init_db as init_db_function
from taskmanager.models import Task, User
from datetime import datetime

class TaskManagerController:
    @staticmethod
    def init_db():
        init_db_function()

    @staticmethod
    def add_task(title, description, due_date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tasks (title, description, due_date, completed)
        VALUES (?, ?, ?, 0)
        """, (title, description, due_date))
        conn.commit()
        conn.close()

    @staticmethod
    def list_tasks():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        conn.close()
        tasks = [Task(row["id"], row["title"], row["description"], row["due_date"], row["completed"], row["owner_id"]) for row in rows]
        return [task.__dict__ for task in tasks]

    @staticmethod
    def update_task(task_id, title, description, due_date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE tasks
        SET title = ?, description = ?, due_date = ?
        WHERE id = ?
        """, (title, description, due_date, task_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_task(task_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def mark_task_complete(task_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
