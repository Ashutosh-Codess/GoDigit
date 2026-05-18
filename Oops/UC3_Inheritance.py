class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

    def display_vehicle(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Model:", self.model)
        print("Battery Percentage:", self.battery_percentage)


class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def display_car(self):
        self.display_vehicle()
        print("Seating Capacity:", self.seating_capacity)


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def display_scooter(self):
        self.display_vehicle()
        print("Max Speed Limit:", self.max_speed_limit)


print("Welcome to Eco-Ride Urban Mobility System")

choice = input("Enter vehicle type (car/scooter): ").lower()

vehicle_id = input("Enter Vehicle ID: ")
model = input("Enter Model: ")
battery_percentage = float(input("Enter Battery Percentage: "))

if choice == "car":
    seating_capacity = int(input("Enter Seating Capacity: "))
    vehicle = ElectricCar(
        vehicle_id,
        model,
        battery_percentage,
        seating_capacity
    )
    print("\nCar Details")
    vehicle.display_car()

elif choice == "scooter":
    max_speed_limit = int(input("Enter Max Speed Limit: "))
    vehicle = ElectricScooter(
        vehicle_id,
        model,
        battery_percentage,
        max_speed_limit
    )
    print("\nScooter Details")
    vehicle.display_scooter()

else:
    print("Invalid Vehicle Type")