# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"

# Polymorphism in action
vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    print(v.move())
