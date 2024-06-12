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

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
            print("Task added successfully!")
        elif choice == "2":
            tasks = list_tasks()
            if tasks:
                for task in tasks:
                    print(f"{task[0]}. {task[1]} - Due: {task[3]} - {'Completed' if task[4] else 'Incomplete'}")
            else:
                print("No tasks to display.")

