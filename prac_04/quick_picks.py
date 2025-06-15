import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_pick = int(input("No of picks? "))
    while quick_pick <= 0:
        print("Incorrect number of picks!")
        quick_pick = int(input("No of picks? "))

    for i in range(quick_pick):
        quick_picks = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


main()