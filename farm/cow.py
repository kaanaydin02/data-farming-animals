"""Cow module."""
from farm.animal import Animal


class Cow(Animal):
    """A cow that produces milk when fed."""

    def __init__(self):
        super().__init__()
        self.milk = 0

    def talk(self):
        """Return the sound a cow makes."""
        return "moo"

    def feed(self):
        """Increase energy and produce 2 liters of milk."""
        super().feed()
        self.milk += 2
