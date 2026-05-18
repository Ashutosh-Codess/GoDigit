class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

    def display_details(self):
        print("\n----- Vehicle Details -----")
        print("Vehicle ID:", self.vehicle_id)
        print("Model:", self.model)
        print("Battery Percentage:", self.battery_percentage, "%")


print("Welcome to Eco-Ride Urban Mobility System")


vehicle_id = input("Enter Vehicle ID: ")
model = input("Enter Vehicle Model: ")
battery_percentage = float(input("Enter Battery Percentage: "))


vehicle1 = Vehicle(vehicle_id, model, battery_percentage)


vehicle1.display_details()