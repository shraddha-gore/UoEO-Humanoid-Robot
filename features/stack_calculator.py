from collections import deque
from .feature import Feature


class StackCalculator(Feature):
    """Class for a stack-based calculator with undo functionality."""

    _stack = None  # Stores the history of values for undo functionality
    _current_value = None  # Tracks the current value of the calculator

    # -----------------------------------------------------------------------------

    def __init__(self):
        """Initialize the stack and set the current value to 0."""
        self._stack = deque()
        self._current_value = 0

    # -----------------------------------------------------------------------------

    def get_current_value(self):
        """Return the current value of the calculator."""
        return self._current_value

    # -----------------------------------------------------------------------------

    def _set_current_value(self, value):
        """Set the current value of the calculator."""
        self._current_value = value

    # -----------------------------------------------------------------------------

    def add(self, number):
        """Add a number to the current value and update the stack."""
        try:
            number = round(float(number), 2)
            current_value = self.get_current_value()

            self._stack.append(current_value)
            self._set_current_value(current_value + number)
            current_value = self.get_current_value()

            print(f"Addition successful. Current value: {current_value}")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def subtract(self, number):
        """Subtract a number from the current value and update the stack."""
        try:
            number = round(float(number), 2)
            current_value = self.get_current_value()

            self._stack.append(current_value)
            self._set_current_value(current_value - number)
            current_value = self.get_current_value()

            print(f"Subtraction successful. Current value: {current_value}")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def multiply(self, number):
        """Multiply the current value by a number and update the stack."""
        try:
            number = round(float(number), 2)
            current_value = self.get_current_value()

            self._stack.append(current_value)
            self._set_current_value(current_value * number)
            current_value = self.get_current_value()

            print(f"Multiplication successful. Current value: {current_value}")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def divide(self, number):
        """Divide the current value by a number and update the stack."""
        try:
            number = round(float(number), 2)

            if number == 0:
                raise ZeroDivisionError("Cannot divide by 0.")

            current_value = self.get_current_value()
            self._stack.append(current_value)
            self._set_current_value(current_value / number)
            current_value = self.get_current_value()

            print(f"Division successful. Current value: {current_value}")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def mod(self, number):
        """Calculate the remainder of the current value divided by a number and update the stack."""
        try:
            number = round(float(number), 2)

            if number == 0:
                raise ZeroDivisionError("Cannot mod by 0.")

            current_value = self.get_current_value()
            self._stack.append(current_value)
            self._set_current_value(current_value % number)
            current_value = self.get_current_value()

            print(f"Modulo successful. Current value: {current_value}")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def undo(self):
        """Undo the last operation by restoring the previous value from the stack."""
        try:
            if not self._stack:
                raise IndexError("No operations to undo.")

            self._set_current_value(self._stack.pop())
            current_value = self.get_current_value()

            print(f"Undid last operation. Current value: {current_value}")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def clear(self):
        """Reset the calculator to its initial state."""
        try:
            self._stack.clear()
            self._set_current_value(0)

            print("Calculator reset to initial state.")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def display(self):
        """Display the current value of the calculator."""
        try:
            current_value = self.get_current_value()

            print(f"Current value: {current_value}")
        except Exception as e:
            print(f"Error: {e}")
