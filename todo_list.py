import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')

    def list_tasks(self):
        """Lists all tasks with their completion status."""
        if not self.tasks:
            print("No tasks in the to-do list.")
            return

        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. [{status}] {task['task']}")

    def mark_completed(self, index):
        """Marks a task as completed."""
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print(f'Task "{self.tasks[index - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")

    def remove_task(self, index):
        """Removes a task from the list."""
        if 0 < index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f'Task "{removed_task["task"]}" removed.')
        else:
            print("Invalid task number.")
    
    def set_reminder(self, index, reminder):
        """Sets a reminder for a specific task."""
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["reminder"] = reminder
            print(f'Reminder set for task "{self.tasks[index - 1]["task"]}" to {reminder}.')
        else:
            print("Invalid task number.")


def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Remove a task")
        print("5. Set a reminder to a task")
        print("6. Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter the task: ")
            reminder = input("Enter a reminder date (YYYY-MM-DD) or press Enter to skip: ")
            if reminder:
                try:
                    # Validate date format
                    datetime.datetime.strptime(reminder, "%Y-%m-%d")
                    todo_list.add_task(task, reminder)
                except ValueError:
                    print("Invalid date format. Task added without reminder.")
                    todo_list.add_task(task)
            else:
                todo_list.add_task(task)

        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            try:
                task_num = int(input("Enter the task number to mark as completed: "))
                todo_list.mark_completed(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_num = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            try:
                task_num = int(input("Enter the task number to set a remindaer on: "))
                reminder = input("Enter a reminder date (YYYY-MM-DD): ")
                try:
                    # Validate date format
                    datetime.datetime.strptime(reminder, "%Y-%m-%d")
                    todo_list.set_reminder(task_num, reminder)
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                todo_list.set_reminder(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "6":
            print("Exiting the to-do list manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
