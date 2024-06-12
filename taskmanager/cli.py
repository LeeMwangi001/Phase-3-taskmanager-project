from .models import add_task, list_tasks, update_task, delete_task, mark_task_complete

def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        