class Car: # Car is the entity
    def __init__(self, brand, model, year, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Engine: {self.engine}")

# initialize object for class Car
car1 = Car("Toyota", "Fortuner", 2025, "Hybrid")
car2 = Car("Mitsubishi", "Montero Sport", 2025, "Diesel")
car3 = Car("BMW", "X5", 2025, "Hybrid")
car4 = Car("Chery", "Tiggo 8 Pro Max", 2025, "Hybrid")

# call the methods display_info()
car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()