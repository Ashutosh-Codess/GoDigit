class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

    def display(self):
        print(
            self.vehicle_id,
            self.model,
            self.battery_percentage
        )


fleet_hubs = {}

while True:
    print("\n1. Add Hub")
    print("2. Add Vehicle to Hub")
    print("3. Display Fleet")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        hub_name = input("Enter Hub Name: ")

        if hub_name not in fleet_hubs:
            fleet_hubs[hub_name] = []
            print("Hub Added Successfully")
        else:
            print("Hub Already Exists")

    elif choice == "2":
        hub_name = input("Enter Hub Name: ")

        if hub_name in fleet_hubs:
            vehicle_id = input("Enter Vehicle ID: ")
            model = input("Enter Model: ")
            battery_percentage = float(
                input("Enter Battery Percentage: ")
            )

            vehicle = Vehicle(
                vehicle_id,
                model,
                battery_percentage
            )

            fleet_hubs[hub_name].append(vehicle)

            print("Vehicle Added Successfully")

        else:
            print("Hub Not Found")

    elif choice == "3":
        for hub, vehicles in fleet_hubs.items():
            print("\nHub:", hub)

            for vehicle in vehicles:
                vehicle.display()

    elif choice == "4":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")