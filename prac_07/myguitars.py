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

    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)

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


def get_new_guitars():
    """Ask the user to input new guitars and return them as a list."""
    print("\nAdd new guitars:")
    new_guitars = []
    name = input("Name: ")
    while name:
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input! Please enter numbers for year and cost.")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Save the list of guitars to the CSV file."""
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == '__main__':
    main()
