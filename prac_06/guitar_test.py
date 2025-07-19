"""
CP1404 Practical - Guitar collection program
Estimate: 20 minutes
Actual: 1hr
"""

from guitar import Guitar

def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1512.9)

    # Test get_age()
    print(f"{guitar.name} get_age() - Expected ~103. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected ~12. Got {other.get_age()}")

    # Test is_vintage()
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


if __name__ == "__main__":
    run_tests()
