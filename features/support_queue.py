from collections import deque
from .feature import Feature


class SupportQueue(Feature):
    """Class to manage support ticket queue."""

    _queue = None  # Deque for storing support tickets

    # -----------------------------------------------------------------------------

    def __init__(self):
        """Initialize the support queue with an empty deque."""
        self._queue = deque()

    # -----------------------------------------------------------------------------

    def get_tickets(self):
        """Return the current state of the queue."""
        return self._queue

    # -----------------------------------------------------------------------------

    def add_ticket(self, ticket):
        """Add a ticket to the queue."""
        try:
            ticket = ticket.strip()

            if not ticket:
                print("Ticket description cannot be empty.")
                return
            elif ticket in self._queue:
                print(f"Ticket '{ticket}' already present.")
                return

            self._queue.append(ticket)
            return f"Ticket '{ticket}' added."
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def resolve_ticket(self):
        """Resolve (remove) the first ticket in the queue."""
        try:
            if not self._queue:
                print("Queue is empty.")
                return

            first_ticket = self._queue.popleft()
            print(f"Ticket '{first_ticket}' resolved.")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def clear(self):
        """Clear all tickets from the queue."""
        try:
            self._queue.clear()
            print("Cleared queue.")
        except Exception as e:
            print(f"Error: {e}")

    # -----------------------------------------------------------------------------

    def display(self):
        """Display all tickets currently in the queue."""
        try:
            if not self._queue:
                print("Queue is empty.")
                return

            print("Tickets: ")
            for idx, ticket in enumerate(self._queue, start=1):
                print(f"{idx}) {ticket}")
        except Exception as e:
            print(f"Error: {e}")
