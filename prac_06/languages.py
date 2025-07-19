"""
CP1404/CP5632 Practical - Client code for ProgrammingLanguage class
Estimate: 30 minutes
Actual: 1hr
"""

from programming_language import ProgrammingLanguage


def main():
    """Demonstrate use of ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Check if __str__ works
    print(python)

    # Create a list of languages
    languages = [python, ruby, visual_basic]

    # Print dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
