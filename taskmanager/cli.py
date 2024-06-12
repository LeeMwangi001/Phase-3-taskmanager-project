import click
from taskmanager.controllers import TaskManagerController

@click.group()
def main():
    """Task Manager CLI"""
    pass

@main.command()
@click.argument('title')
@click.argument('description')
@click.argument('due_date')
def add_task(title, description, due_date):
    """Add a new task"""
    TaskManagerController.add_task(title, description, due_date)

@main.command()
def list_tasks():
    """List all tasks"""
    tasks = TaskManagerController.list_tasks()
    if tasks:
        for task in tasks:
            print(f"{task['id']}. {task['title']} - Due: {task['due_date']} - {'Completed' if task['completed'] else 'Incomplete'}")
    else:
        print("No tasks to display.")

@main.command()
@click.argument('task_id')
@click.argument('title')
@click.argument('description')
@click.argument('due_date')
def update_task(task_id, title, description, due_date):
    """Update an existing task"""
    TaskManagerController.update_task(task_id, title, description, due_date)

@main.command()
@click.argument('task_id')
def delete_task(task_id):
    """Delete a task"""
    TaskManagerController.delete_task(task_id)

@main.command()
@click.argument('task_id')
def mark_task_complete(task_id):
    """Mark a task as complete"""
    TaskManagerController.mark_task_complete(task_id)

@main.command()
def init_db():
    """Initialize the database"""
    TaskManagerController.init_db()

if __name__ == "__main__":
    main()
