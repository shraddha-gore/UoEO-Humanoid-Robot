import unittest
from features.todo_list import ToDoList


class ToDoListTest(unittest.TestCase):

    todo = ToDoList()

    # -----------------------------------------------------------------------------

    # Test adding a task
    def test_1_add_task(self):
        name = "Test Task"

        self.todo.add_task(name)
        assert name in self.todo.get_tasks(), "A new task should be added."

    # -----------------------------------------------------------------------------

    # Test adding an empty task
    def test_2_add_empty_task(self):
        original_tasks_count = len(self.todo.get_tasks())

        self.todo.add_task("  ")
        assert len(
            self.todo.get_tasks()) == original_tasks_count, "An empty task should not be added."

    # -----------------------------------------------------------------------------

    # Test adding a duplicate task
    def test_3_add_duplicate_task(self):
        name = "Test Task"
        original_tasks_count = len(self.todo.get_tasks())

        self.todo.add_task(name)
        assert len(
            self.todo.get_tasks()) == original_tasks_count, "Duplicate task should not be added."

    # -----------------------------------------------------------------------------

    # Test removing a task
    def test_4_remove_task(self):
        name = "Test Task"

        self.todo.remove_task(name, "y")
        assert name not in self.todo.get_tasks(), "Task should be removed."

    # -----------------------------------------------------------------------------

    # Test removing a non-existent task
    def test_5_remove_non_existent_task(self):
        name = "Non-existent Task"
        original_tasks_count = len(self.todo.get_tasks())

        self.todo.remove_task(name, "y")
        assert len(
            self.todo.get_tasks()) == original_tasks_count, "Non-existent task should not affect To-Do list."

    # -----------------------------------------------------------------------------

    # Test clearing all tasks
    def test_6_clear(self):
        self.todo.clear("y")
        assert len(self.todo.get_tasks()) == 0, "To-Do list should be cleared."
