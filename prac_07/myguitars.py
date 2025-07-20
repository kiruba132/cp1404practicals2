"""
CP1404 Practical 07
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read and display guitars from a file, then sort and display them."""
    guitars = load_guitars(FILENAME)

    print("These are my guitars:")
    display_guitars(guitars)

    # Sort by year (oldest to newest)
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")


if __name__ == '__main__':
    main()
