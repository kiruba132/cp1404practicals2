"""
CP1404/CP5632 Practical
Test UnreliableCar
"""
from unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Reliable", 100, 100.0)
    unreliable_car = UnreliableCar("Unreliable", 100, 10.0)

    print("Testing ReliableCar (should always drive):")
    for i in range(5):
        distance = reliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance}km (Fuel left: {reliable_car.fuel})")

    print("\nTesting UnreliableCar (may not always drive):")
    for i in range(10):
        distance = unreliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance}km (Fuel left: {unreliable_car.fuel})")


if __name__ == "__main__":
    main()
