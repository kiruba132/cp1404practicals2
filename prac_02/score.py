"""
CP1404/CP5632 - Practical 2
Function implementation for determining score status program
"""
import random

def main():
    """Main function to get user score, print result, and test with a random score."""
    score = float(input("Enter score: "))
    print(determine_score_status(score))

    random_score = random.randint(0, 100)  # Generate a random score between 0 and 100
    print(f"Random score: {random_score:.2f}, Status: {determine_score_status(random_score)}")

def determine_score_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

main()

