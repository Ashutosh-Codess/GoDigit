class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage,
                 maintenance_status, rental_price):

        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = 0
        self.__maintenance_status = maintenance_status
        self.__rental_price = rental_price

        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):
        return self.__battery_percentage

    def set_battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Invalid Battery Percentage")

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def get_rental_price(self):
        return self.__rental_price

    def set_rental_price(self, price):
        if price > 0:
            self.__rental_price = price
        else:
            print("Invalid Rental Price")

    def display_details(self):
        print("\nVehicle Details")
        print("Vehicle ID:", self.vehicle_id)
        print("Model:", self.model)
        print("Battery Percentage:", self.__battery_percentage)
        print("Maintenance Status:", self.__maintenance_status)
        print("Rental Price:", self.__rental_price)


print("Welcome to Eco-Ride Urban Mobility System")

vehicle_id = input("Enter Vehicle ID: ")
model = input("Enter Model: ")
battery_percentage = float(input("Enter Battery Percentage: "))
maintenance_status = input("Enter Maintenance Status: ")
rental_price = float(input("Enter Rental Price: "))

vehicle = Vehicle(
    vehicle_id,
    model,
    battery_percentage,
    maintenance_status,
    rental_price
)

vehicle.display_details()