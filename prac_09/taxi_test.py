from taxi import Taxi

def main():
    # Create a new taxi object, my_taxi, with name "Prius 1" and 100 units of fuel
    my_taxi = Taxi("Prius 1", 100)

    # Start the fare before driving
    my_taxi.start_fare()
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter (start a new fare)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()
