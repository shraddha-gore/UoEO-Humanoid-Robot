from .feature import Feature


class ToDoList(Feature):
    """Class to manage a to-do list."""

    _tasks = None  # Stores tasks

    # -----------------------------------------------------------------------------

    def __init__(self):
        """Initialize an empty list to store tasks."""
        self._tasks = []

    # -----------------------------------------------------------------------------

    def get_tasks(self):
        """Return the current list of tasks."""
        return self._tasks

    # -----------------------------------------------------------------------------

    def add_task(self, task):
        """Add a new task to the To-Do list."""
        try:
            task = task.strip()

            if not task:
                print("Task cannot be empty.")
                return
            elif task in self._tasks:
                print(f"Task '{task}' already present.")
                return

            self._tasks.append(task)
            print(f"Task '{task}' added.")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def remove_task(self, task, confirm):
        """Remove a task from the To-Do list after confirmation."""
        try:
            task = task.strip()
            confirm = confirm.strip().lower()

            if confirm != "y":
                print("Cancelled task removal.")
                return

            if not task:
                print(f"Task '{task}' cannot be empty.")
                return

            if task not in self._tasks:
                print(f"Task '{task}' not found.")
                return

            self._tasks.remove(task)
            print("Task '{task}' removed.")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def clear(self, confirm):
        """Clear all tasks from the To-Do list after confirmation."""
        try:
            confirm = confirm.strip().lower()

            if confirm != "y":
                print("Cancelled To-Do list clearance.")
                return

            self._tasks.clear()
            print("To-Do list cleared.")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def display(self):
        """Display all tasks in the To-Do list."""
        try:
            if not self._tasks:
                print("To-Do list is empty.")
                return

            print("Tasks: ")
            for idx, task in enumerate(self._tasks, start=1):
                print(f"{idx}) {task}")
        except Exception as e:
            print(f"Error: {e}")
