"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    category = "Invalid score"
elif score >= 90:
    category = "Excellent"
elif score >= 50:
    category = "Pass"
else:
    category = "Bad"
print(f"Your score of {score} is considered {category}")
