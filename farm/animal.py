# pylint: disable=too-few-public-methods
"""Animal module — shared parent class for all animals."""


class Animal:
    """Base class for all animals, storing energy level."""

    def __init__(self):
        self.energy = 0

    def feed(self):
        """Increase the animal's energy by 1."""
        self.energy += 1
