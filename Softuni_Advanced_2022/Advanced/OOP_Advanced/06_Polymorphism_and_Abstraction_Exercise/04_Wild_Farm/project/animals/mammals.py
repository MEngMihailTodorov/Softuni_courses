from project.food import Vegetable, Fruit, Seed, Meat
from project.animals.animal import Animal
from project.animals.animal import Mammal
from abc import ABC, abstractmethod


class Mouse(Mammal):
    @property
    def gained_weight(self):
        return 0.1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    @property
    def gained_weight(self):
        return 0.4

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    @property
    def gained_weight(self):
        return 0.3

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    @property
    def gained_weight(self):
        return 1.00

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self):
        return "ROAR!!!"

    