class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        fuel_needed = kilometers * self.fuel_consumption
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
        else:
            raise Exception("Not enough fuel to drive the distance.")

class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

class FamilyCar(Car):
    pass

class Motorcycle(Vehicle):
    pass

class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

class CrossMotorcycle(Motorcycle):
    pass

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
