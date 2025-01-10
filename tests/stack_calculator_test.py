import unittest
from features.stack_calculator import StackCalculator


class StackCalculatorTest(unittest.TestCase):

    calc = StackCalculator()

    # -----------------------------------------------------------------------------

    # Test initial value
    def test_1_initial_value(self):
        assert self.calc.get_current_value() == 0, "Initial value should be 0"

    # -----------------------------------------------------------------------------

    # Test addition
    def test_2_addition(self):
        self.calc.add(5)
        assert self.calc.get_current_value() == 5, "Addition should work."

    # -----------------------------------------------------------------------------

    # Test subtraction
    def test_3_subtraction(self):
        self.calc.subtract(2)
        assert self.calc.get_current_value() == 3, "Subtraction should work."

    # -----------------------------------------------------------------------------

    # Test multiplication
    def test_4_multiplication(self):
        self.calc.multiply(4)
        assert self.calc.get_current_value() == 12, "Multiplication should work."

    # -----------------------------------------------------------------------------

    # Test division
    def test_5_division(self):
        self.calc.divide(3)
        assert self.calc.get_current_value() == 4, "Division should work."

    # -----------------------------------------------------------------------------

    # Test invalid division
    def test_6_invalid_division(self):
        current_value = self.calc.get_current_value()

        self.calc.divide(0)
        assert self.calc.get_current_value(
        ) == current_value, "Division by 0 should be handled."

    # -----------------------------------------------------------------------------

    # Test modulo
    def test_7_modulo(self):
        self.calc.mod(2)
        assert self.calc.get_current_value() == 0, "Modulo should work."

    # -----------------------------------------------------------------------------

    # Test invalid modulo
    def test_8_invalid_modulo(self):
        current_value = self.calc.get_current_value()

        self.calc.mod(0)
        assert self.calc.get_current_value(
        ) == current_value, "Modulo by 0 should be handled."

    # -----------------------------------------------------------------------------

     # Test undo
    def test_9_undo(self):
        self.calc.undo()
        assert self.calc.get_current_value() == 4, "Undo should work."

    # -----------------------------------------------------------------------------

    # Test clear
    def test_10_clear(self):
        self.calc.clear()
        assert self.calc.get_current_value() == 0, "Clear should work."
