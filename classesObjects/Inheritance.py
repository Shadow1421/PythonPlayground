# Base class: Car
class Car:
    def __init__(self, engine, model):
        self.engine = engine
        self.model = model

    def apply_break(self):
        print("Car: Applying brakes.")

    def accelerate(self):
        print("Car: Accelerating.")


# Derived class: BMW (inherits from Car)
class BMW(Car):
    def __init__(self, engine, model, seats):
        super().__init__(engine, model)
        self.seats = seats

    def display_car_properties(self):
        print("BMW Details:")
        print("Engine:", self.engine)
        print("Model:", self.model)
        print("Number of Seats:", self.seats)


# Creating instances of the classes
car1 = Car("V6", "XYZ")
bmw1 = BMW("V8", "X5", 5)

# Accessing base class methods and attributes
car1.apply_break()
car1.accelerate()

# Accessing derived class methods and attributes
bmw1.apply_break()
bmw1.accelerate()
bmw1.display_car_properties()
