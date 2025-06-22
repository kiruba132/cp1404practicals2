"""
wimbledon.py
Estimate: 30 minutes
Actual: 1 hour
"""

import csv

def main():
    """Main function to coordinate Wimbledon data processing."""
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_to_wins, countries = process_wimbledon_data(data)
    display_wimbledon_stats(champion_to_wins, countries)

def read_wimbledon_data(filename):
    """Read Wimbledon data from a CSV file and return a list of rows."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        return list(reader)

def process_wimbledon_data(data):
    """Process data to extract champion win counts and countries."""
    champion_to_wins = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins, countries

def display_wimbledon_stats(champion_to_wins, countries):
    """Display champion stats and sorted list of countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == '__main__':
    main()
