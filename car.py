# Car Rental System:
class Car:
    company = "Toyota"
    
    def __init__(self, model, year, licence_plate, availability_status, rental_rate):
        self.model = model
        self.year = year
        self.licence_plate = licence_plate
        self.availability_status = availability_status
        self.rental_rate = rental_rate
    
    @classmethod
    def set_company(cls, new_company):
        """Change the Class Variable"""
        cls.company = new_company
    
    def show_car(self):
        print(f"\nCar Model: {self.model}\nCar Company: {self.company}\nCar Year: {self.year}\nLicence Plate: {self.licence_plate}")
        
    def available(self):
        print(f"Car Model: {self.model}\nCar Company: {self.company}\nAvailability: {bool(self.availability_status)}\nRental Rent per Day: {self.rental_rate}\n")

# car1 = Car("Camry", 2022, "ABC123", 1, 50.0)
# car2 = Car("Civic", 2021, "XYT099", 0, 85.0)
# car3 = Car("Rav4", 2023, "PQR456", 0, 55.0)
# car3 = Car("Corolla", 2021, "XYZ789", 0, 45.0)


class Customer:
    def __init__(self, name, phone_num):
        self.name = name
        self.phone_num = phone_num
        self.rent = 0  # Initialize rent to zero for a new customer
        self.rent_history = []

    def customer_detail(self):
        print("Customer Details:")
        print(f"Name: {self.name}\nPhone Number: {self.phone_num}\nRent: {self.rent}\n")

    def adjust_rent(self, new_rent):
        self.rent = new_rent
        print(f"Rent adjusted to: {self.rent}")

    def add_rent(self, additional_rent):
        self.rent += additional_rent
        print(f"Additional rent added. Total rent now: {self.rent}")
        self.rent_history.append(self.rent)

    def total_rent(self):
        self.total_rent = sum(self.rent_history)
        print(f"Total rent now: {self.rent}")
    
    

# Example:
customer1 = Customer("John Doe", "123-456-7890")
customer2 = Customer("Alice Smith", "987-654-3210")
customer3 = Customer("Bob Johnson", "555-123-4567")
# Adjusting the rent
# customer1.adjust_rent(600.0)

# customer1.add_rent(500) # Adding rent 
# # Displaying details for each customer
# customer1.customer_detail()
# customer2.customer_detail()
# customer3.customer_detail()

class Connect:
    def __init__(self, car_vehicle, customer):
        self.vehicle = car_vehicle  # Car class Object
        self.customer = customer    # Customer class Object
        self.available_car = list()
        self.unavailable_car = list()

    def show_all_available_cars(self):
        print("\nAll Available Cars:")
        for index, car in enumerate(self.available_car, start=1):
            car.show_car()
            print()

    def show_all_unavailable_cars(self):
        print("\nAll Unavailable Cars:")
        for index, car in enumerate(self.unavailable_car, start=1):
            car.show_car()
            print()

    def connect(self, index_num):
        # Check if the selected car is available
        if 0 <= index_num < len(self.available_car):
            selected_car = self.available_car.pop(index_num)
            selected_car.availability_status = 0  # Mark as unavailable
            self.unavailable_car.append(selected_car)
            print("Car connected to customer successfully.")
        else:
            print("Invalid index. Please choose an available car.")


class RentalRecord:
    def __init__(self, customer, car, rental_days):
        self.customer = customer
        self.car = car
        self.rental_days = rental_days      # New
        self.total_rent = self.calculate_rent()   #

    def calculate_rent(self):
        return self.car.rental_rate * self.rental_days

    def display_record(self):
        print("\nRental Record:")
        print(f"Customer: {self.customer.name}")
        print(f"Car Model: {self.car.model}")
        print(f"Rental Days: {self.rental_days}")
        print(f"Total Rent: ${self.total_rent}")

# You can use this class to keep track of rental records in the CarRentalSystem class.


class CarRentalSystem:
    def __init__(self):
        self.car_lst = []  # List to store Car objects
        self.customer_lst = []  # List to store Customer objects
        self.rental_records = []  # List to store RentalRecord objects

    def menu(self):
        while True:
            print("Welcome to Car Rental Management System".center(95, " "))
            print("\n Menu:")
            print("1. Show All Cars")
            print("2. Show Available Cars")
            print("3. Show All Customers")
            print("4. Show All Customers Detail")
            print("5. Show Rent History of Every Person")
            print("6. Add New Car")
            print("7. Add New Customer and Connect with Car")
            print("8. Exit")

            choice = int(input("Enter the option: "))

            if choice == 1:
                self.show_all_cars()

            elif choice == 2:
                self.show_available_cars()

            elif choice == 3:
                self.show_all_customers()

            elif choice == 4:
                self.show_all_customers_detail()

            elif choice == 5:
                self.show_rent_history()

            elif choice == 6:
                self.add_new_car()

            elif choice == 7:
                self.add_new_customer_and_connect_car()

            elif choice == 8:
                print("Exiting the system.")
                break

            else:
                print("Invalid option. Please try again.")

    def show_all_cars(self):
        print("\nAll Cars:")
        for index, car in enumerate(self.car_lst, start=1):
            car.show_car()
            print()

    def show_available_cars(self):
        print("\nAll Available Cars:")
        for index, car in enumerate(self.car_lst, start=1):
            if car.availability_status == 1:
                car.show_car()
                print()

    def show_all_customers(self):
        print("\nAll Customers:")
        for index, customer in enumerate(self.customer_lst, start=1):
            customer.customer_detail()
            print()

    def show_all_customers_detail(self):
        print("\nAll Customers Detail:")
        for index, customer in enumerate(self.customer_lst, start=1):
            customer.customer_detail()
            print()

    def show_rent_history(self):
        print("\nRent History:")
        for record in self.rental_records:
            record.display_record()
            print()

    def add_new_car(self):
        model = input("Enter car model: ")
        year = int(input("Enter car year: "))
        licence_plate = input("Enter licence plate: ")
        availability_status = int(input("Enter availability status (0 or 1): "))
        rental_rate = float(input("Enter rental rate per day: "))

        new_car = Car(model, year, licence_plate, availability_status, rental_rate)
        self.car_lst.append(new_car)
        print("New car added successfully.")    

    def add_new_customer_and_connect_car(self):
        name = input("Enter customer name: ")
        phone_num = input("Enter customer phone number: ")

        new_customer = Customer(name, phone_num)
        self.customer_lst.append(new_customer)

        self.show_available_cars()
        index_num = int(input("Enter the index of the car to connect: "))

        if 0 <= index_num < len(self.car_lst):
            connect = Connect(self.car_lst[index_num], new_customer)
            connect.connect(0)  # Assuming the first available car is selected

            rental_days = int(input("Enter the number of rental days: "))
            rental_rate = self.car_lst[index_num].rental_rate
            rent_amount = rental_days * rental_rate

            new_customer.add_rent(rent_amount)

            rental_record = RentalRecord(new_customer, self.car_lst[index_num], rental_days)
            self.rental_records.append(rental_record)

            print("Customer added and connected with a car successfully.")

        else:
            print("Invalid car index. Customer not connected.")
            
            
car_system = CarRentalSystem()
car_system.menu()