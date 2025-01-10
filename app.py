from features.todo_list import ToDoList
from features.stack_calculator import StackCalculator
from features.support_queue import SupportQueue


class App:
    """Main CLI Application integrating all features."""

    _features = None  # Dictionary for storing feature objects

    # -----------------------------------------------------------------------------

    def __init__(self):
        """Initialize features."""
        self._features = {
            "1": ToDoList(),
            "2": StackCalculator(),
            "3": SupportQueue(),
        }

    # -----------------------------------------------------------------------------

    def start(self):
        """Main menu for the application."""
        while True:
            try:
                print("\n--- CLI Application ---")
                print("1. To-Do List")
                print("2. Stack Calculator")
                print("3. Support Queue")
                print("4. Exit")
                choice = input("Choose an option: ")

                if choice in self._features:
                    self._manage_feature(choice)
                elif choice == "4":
                    print("Exiting application.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def _manage_feature(self, feature_key):
        """Feature management method."""
        feature = self._features[feature_key]

        if isinstance(feature, ToDoList):
            self._manage_todo_list(feature)
        elif isinstance(feature, StackCalculator):
            self._manage_stack_calculator(feature)
        elif isinstance(feature, SupportQueue):
            self._manage_support_queue(feature)

    # -----------------------------------------------------------------------------

    def _manage_todo_list(self, feature):
        """Menu and operations for To-Do List."""
        while True:
            try:
                print("\n--- To-Do List ---")
                print("1. Add Task")
                print("2. Remove Task")
                print("3. Clear Tasks")
                print("4. Display Tasks")
                print("5. Back")
                choice = input("Choose an option: ")

                if choice == "1":
                    task = input("Enter task: ")
                    feature.add_task(task)
                elif choice == "2":
                    task = input("Enter task to remove: ").strip()
                    confirm = input(
                        f"Are you sure you want to clear task '{task}'? (y/n): ")
                    feature.remove_task(task, confirm)
                elif choice == "3":
                    confirm = input(
                        "Are you sure you want to clear all tasks? (y/n): ")
                    feature.clear(confirm)
                elif choice == "4":
                    feature.display()
                elif choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def _manage_stack_calculator(self, feature):
        """Menu and operations for Stack Calculator."""
        while True:
            try:
                print("\n--- Stack Calculator ---")
                print("1. Add")
                print("2. Subtract")
                print("3. Multiply")
                print("4. Divide")
                print("5. Mod")
                print("6. Undo")
                print("7. Clear History")
                print("8. Display Current Value")
                print("9. Back")
                choice = input("Choose an option: ")

                if choice == "1":
                    number = input("Enter number to add: ")
                    feature.add(number)
                elif choice == "2":
                    number = input("Enter number to subtract: ")
                    feature.subtract(number)
                elif choice == "3":
                    number = input("Enter number to multiply: ")
                    feature.multiply(number)
                elif choice == "4":
                    number = input("Enter number to divide: ")
                    feature.divide(number)
                elif choice == "5":
                    number = input("Enter number to mod: ")
                    feature.mod(number)
                elif choice == "6":
                    feature.undo()
                elif choice == "7":
                    feature.clear()
                elif choice == "8":
                    feature.display()
                elif choice == "9":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def _manage_support_queue(self, feature):
        """Menu and operations for Support Queue."""
        while True:
            try:
                print("\n--- Support Queue ---")
                print("1. Add Ticket")
                print("2. Resolve First Ticket")
                print("3. Clear Queue")
                print("4. Display Tickets")
                print("5. Back")
                choice = input("Choose an option: ")

                if choice == "1":
                    ticket = input("Enter ticket description: ")
                    feature.add_ticket(ticket)
                elif choice == "2":
                    feature.resolve_ticket()
                elif choice == "3":
                    feature.clear()
                elif choice == "4":
                    "Tickets:", feature.display()
                elif choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")
