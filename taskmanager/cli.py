# cli.py

from taskmanager.models import User, Task, TaskAssignment

def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. Add User")
        print("2. List Users")
        print("3. Add Task")
        print("4. List Tasks")
        print("5. Update Task")
        print("6. Delete Task")
        print("7. Mark Task as Complete")
        print("8. Assign Task to User")
        print("9. Quit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            name = input("Enter user name: ")
            User.add_user(name)
        elif choice == "2":
            users = User.list_users()
            if users:
                for user in users:
                    print(f"ID: {user['id']}, Name: {user['name']}")
            else:
                print("No users to display.")
        elif choice == "3":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            owner_name = input("Enter owner name: ")
            owner_id = User.get_user_id(owner_name)
            if owner_id:
                Task.add_task(title, description, due_date, owner_id)
            else:
                print("User not found. Please add the user first.")
        elif choice == "4":
            tasks = Task.list_tasks()
            if tasks:
                for task in tasks:
                    print(f"ID: {task['id']}, Title: {task['title']}, Due Date: {task['due_date']}, "
                          f"Owner ID: {task['owner_id']}, Completed: {task['completed']}")
            else:
                print("No tasks to display.")
        elif choice == "5":
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            due_date = input("Enter new due date (YYYY-MM-DD): ")
            Task.update_task(task_id, title, description, due_date)
        elif choice == "6":
            task_id = int(input("Enter task ID to delete: "))
            Task.delete_task(task_id)
        elif choice == "7":
            task_id = int(input("Enter task ID to mark as complete: "))
            Task.mark_task_complete(task_id)
        elif choice == "8":
            task_id = int(input("Enter task ID to assign: "))
            user_name = input("Enter user name to assign to: ")
            user_id = User.get_user_id(user_name)
            if user_id:
                TaskAssignment.assign_task(task_id, user_id)
            else:
                print("User not found. Please add the user first.")
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
