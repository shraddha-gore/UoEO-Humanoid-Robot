import unittest
from features.support_queue import SupportQueue


class SupportQueueTest(unittest.TestCase):
    """
    Unit tests for the SupportQueue class.
    The tests run sequentially, and the state of the shared SupportQueue instance persists across tests.
    """

    queue = SupportQueue()  # Instance of SupportQueue

    # -----------------------------------------------------------------------------

    # Test adding a ticket
    def test_1_add_ticket(self):
        name = "Test Ticket"

        self.queue.add_ticket(name)
        assert name in self.queue.get_tickets(), "A new ticket should be added."

    # -----------------------------------------------------------------------------

    # Test adding an empty ticket
    def test_2_add_empty_ticket(self):
        original_tickets_count = len(self.queue.get_tickets())

        self.queue.add_ticket("  ")
        assert len(
            self.queue.get_tickets()) == original_tickets_count, "An empty ticket should not be added."

    # -----------------------------------------------------------------------------

    # Test adding a duplicate ticket
    def test_3_add_duplicate_ticket(self):
        name = "Test Ticket"
        original_tickets_count = len(self.queue.get_tickets())

        self.queue.add_ticket(name)
        assert len(
            self.queue.get_tickets()) == original_tickets_count, "Duplicate ticket should not be added."

    # -----------------------------------------------------------------------------

    # Test resolving a ticket
    def test_4_resolve_ticket(self):
        name = "Test Ticket"

        self.queue.resolve_ticket()
        assert name not in self.queue.get_tickets(), "First ticket should be removed."

    # -----------------------------------------------------------------------------

    # Test clearing queue
    def test_5_clear(self):
        name = "Temp Ticket"

        self.queue.add_ticket(name)
        self.queue.clear()
        assert len(self.queue.get_tickets()) == 0, "Queue should be cleared."
