"""
CP1404/CP5632 - Practical
Function implementation for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsius_to_fahrenheit(celsius):
    """ Function to convert Celsius to Fahrenheit """
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """ Function to convert Fahrenheit to Celsius """
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()