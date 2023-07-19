# call base class function in drive class function
# Base class: Car 
class Car:
    def __init__(self, engine, model):
        self.engine = engine
        self.model = model

    def apply_brake(self):
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

    def apply_brake(self):
        super().apply_brake()  # Calling the base class function
        print("BMW: Applying brakes with additional features.")


# Creating instances of the classes
bmw1 = BMW("V8", "X5", 5)

# Accessing derived class methods and base class function
bmw1.apply_brake()
