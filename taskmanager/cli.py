from .models import TaskManager

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
            TaskManager.add_task(title, description, due_date)
            print("Task added successfully!")
        elif choice == "2":
            tasks = TaskManager.list_tasks()
            if tasks:
                for task in tasks:
                    print(f"{task.id}. {task.title} - Due: {task.due_date} - {'Completed' if task.completed else 'Incomplete'}")
            else:
                print("No tasks to display.")
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            due_date = input("Enter new due date (YYYY-MM-DD): ")
            TaskManager.update_task(task_id, title, description, due_date)
            print("Task updated successfully!")
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            TaskManager.delete_task(task_id)
            print("Task deleted successfully!")
        elif choice == "5":
            task_id = int(input("Enter task ID to mark as complete: "))
            TaskManager.mark_task_complete(task_id)
            print("Task marked as complete!")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
