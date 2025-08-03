"""
CP1404/CP5632 Practical
UnreliableCar class
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable version of a Car that may randomly not drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is less than the car's reliability."""
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
