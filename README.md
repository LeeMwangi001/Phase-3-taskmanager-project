# TaskManager

TaskManager is a simple command-line application for managing tasks. It allows users to add, list, update, delete, and mark tasks as complete. This project is created by Lee Mwangi.

## Features
- Add a new task with a title, description, and due date.
- List all tasks with their details.
- Update an existing task.
- Delete a task.
- Mark a task as complete.
- Quit the application.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/LeeMwangi001/TaskManager.git
    ```

2. Navigate to the project directory:
    ```sh
    cd TaskManager
    ```

3. Install the required dependencies (if any).

## Usage

Run the main script to start the TaskManager application:
```sh
python main.py
```
## Menu Options

1. Add Task: Prompts the user to enter the task title, description, and due date. The task is then added to the task list.

2. List Tasks: Displays all the tasks with their details, including the task ID, title, due date, and completion status.

3. Update Task: Prompts the user to enter the task ID and the new details (title, description, due date) to update the task.

4. Delete Task: Prompts the user to enter the task ID to delete the task from the list.

5. Mark Task as Complete: Prompts the user to enter the task ID to mark the task as complete.

6. Quit: Exits the TaskManager application.

## Example

Here is an example of how the TaskManager application works:

Task Manager Menu:
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Quit

Enter your choice (1-6): 1
Enter task title: Finish project
Enter task description: Complete the project by the end of the week
Enter due date (YYYY-MM-DD): 2024-06-15
Task added successfully!

Task Manager Menu:
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Quit

Enter your choice (1-6): 2
1. Finish project - Due: 2024-06-15 - Incomplete

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Lee Mwangi (GitHub: LeeMwangi001)