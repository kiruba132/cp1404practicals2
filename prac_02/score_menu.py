MENU = "G - Get a valid score\nP - Print result\nS - Show stars\nQ - Quit"

def main():
    score = ""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            print(show_stars(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def get_valid_score():
    """Prompt user until a valid score (0-100) is entered."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


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

def show_stars(score):
    """return stars matching to the score (as an integer)."""
    return '*' * int(score)

main()


