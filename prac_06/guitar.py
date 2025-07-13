"""
CP1404 Practical - Guitar collection program
Estimate: 20 minutes
Actual: 1hr
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    """Class for storing information about a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= VINTAGE_AGE