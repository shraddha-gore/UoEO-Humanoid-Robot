from abc import ABC, abstractmethod


class Feature(ABC):
    """Abstract base class for common feature methods."""

    @abstractmethod
    def clear(self):
        """Clear all data in the feature.
        Must be implemented by all subclasses."""
        pass

    # -----------------------------------------------------------------------------

    @abstractmethod
    def display(self):
        """Display the current state of the feature.
        Must be implemented by all subclasses."""
        pass
