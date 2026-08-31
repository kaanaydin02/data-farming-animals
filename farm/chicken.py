"""Chicken module."""
from farm.animal import Animal


class Chicken(Animal):
    """A chicken that produces eggs (if female) when fed."""

    def __init__(self, gender):
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def talk(self):
        """Return the sound a chicken makes, based on gender."""
        if self.gender == "male":
            return "cock-a-doodle-doo"
        return "cluck cluck"

    def feed(self):
        """Increase energy and, if female, produce 2 eggs."""
        super().feed()
        if self.gender == "female":
            self.eggs += 2
