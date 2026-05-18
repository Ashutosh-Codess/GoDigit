from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

    @abstractmethod
    def calculate_trip_cost(self, value):
        pass

    def display_vehicle(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Model:", self.model)
        print("Battery Percentage:", self.battery_percentage)


class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return distance * 10


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, minutes):
        return minutes * 2


print("Welcome to Eco-Ride Urban Mobility System")

choice = input("Enter vehicle type (car/scooter): ").lower()

vehicle_id = input("Enter Vehicle ID: ")
model = input("Enter Model: ")
battery_percentage = float(input("Enter Battery Percentage: "))

if choice == "car":
    seating_capacity = int(input("Enter Seating Capacity: "))
    distance = float(input("Enter Distance in KM: "))

    vehicle = ElectricCar(
        vehicle_id,
        model,
        battery_percentage,
        seating_capacity
    )

    print("\nTrip Cost:", vehicle.calculate_trip_cost(distance))

elif choice == "scooter":
    max_speed_limit = int(input("Enter Max Speed Limit: "))
    minutes = float(input("Enter Trip Time in Minutes: "))

    vehicle = ElectricScooter(
        vehicle_id,
        model,
        battery_percentage,
        max_speed_limit
    )

    print("\nTrip Cost:", vehicle.calculate_trip_cost(minutes))

else:
    print("Invalid Vehicle Type")