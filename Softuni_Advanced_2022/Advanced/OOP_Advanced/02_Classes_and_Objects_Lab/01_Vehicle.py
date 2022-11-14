class Vehicle:
    def __init__(self,  mileage: int, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []

    def __str__(self):
        return f"{self.max_speed}"


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)


print(car)