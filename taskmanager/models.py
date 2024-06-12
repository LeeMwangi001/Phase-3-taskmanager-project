from .database import connect

def add_task(title, description, due_date):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tasks (title, description, due_date, completed)
        VALUES (?, ?, ?, 0)
        """, (title, description, due_date))
        conn.commit()

def list_tasks():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()

def update_task(task_id, title, description, due_date):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE tasks
        SET title = ?, description = ?, due_date = ?
        WHERE id = ?
        """, (title, description, due_date, task_id))
        conn.commit()

def delete_task(task_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

def mark_task_complete(task_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
