from project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name: str, quantity: int, milliliters: float):
        super().__init__(name, quantity, milliliters)
