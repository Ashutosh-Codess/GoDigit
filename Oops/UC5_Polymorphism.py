from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

    @abstractmethod
    def calculate_trip_cost(self, value):
        pass


class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return 5 + (0.50 * distance)


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, minutes):
        return 1 + (0.15 * minutes)


vehicles = []

n = int(input("Enter number of vehicles: "))

for i in range(n):
    choice = input("\nEnter vehicle type (car/scooter): ").lower()

    vehicle_id = input("Enter Vehicle ID: ")
    model = input("Enter Model: ")
    battery_percentage = float(input("Enter Battery Percentage: "))

    if choice == "car":
        seating_capacity = int(input("Enter Seating Capacity: "))
        distance = float(input("Enter Distance in KM: "))

        car = ElectricCar(
            vehicle_id,
            model,
            battery_percentage,
            seating_capacity
        )

        vehicles.append((car, distance))

    elif choice == "scooter":
        max_speed_limit = int(input("Enter Max Speed Limit: "))
        minutes = float(input("Enter Trip Time in Minutes: "))

        scooter = ElectricScooter(
            vehicle_id,
            model,
            battery_percentage,
            max_speed_limit
        )

        vehicles.append((scooter, minutes))

print("\nTrip Cost Details")

for vehicle, value in vehicles:
    print(
        vehicle.vehicle_id,
        vehicle.model,
        "Trip Cost =",
        vehicle.calculate_trip_cost(value)
    )