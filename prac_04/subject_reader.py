"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)



def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []  # Create empty list to hold all records
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Split the line into a list
        parts[2] = int(parts[2])  # Convert the student count to an integer
        data.append(parts)  # Add the processed line to the list
    input_file.close()
    return data

def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()