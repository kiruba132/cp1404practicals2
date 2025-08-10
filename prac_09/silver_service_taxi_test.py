# silver_service_taxi_test.py
from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a new SilverServiceTaxi object with name "Hummer", 200 units of fuel and 2x fanciness
    hummer = SilverServiceTaxi("Hummer", 200, 2)

    # Start the fare (important to reset fare distance)
    hummer.start_fare()

    # Drive the taxi 18 km
    distance_driven = hummer.drive(18)

    # Print the taxi's details and the current fare
    print(hummer)
    print(f"Current fare: ${hummer.get_fare():.2f}")

    # Assert the fare is as expected (18km * 2 * 1.23 + 4.50 = 48.78, rounded to 48.8)
    assert hummer.get_fare() == 48.8, f"Expected fare of $48.8, but got {hummer.get_fare()}"

if __name__ == "__main__":
    main()
