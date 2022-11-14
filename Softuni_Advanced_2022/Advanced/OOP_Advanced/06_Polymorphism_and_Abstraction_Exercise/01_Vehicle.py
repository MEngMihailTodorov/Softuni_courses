from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    AIR_CONDITIONING_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = (self.fuel_consumption + Car.AIR_CONDITIONING_CONSUMPTION) * distance

        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONING_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Truck.AIR_CONDITIONING_CONSUMPTION) * distance

        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
