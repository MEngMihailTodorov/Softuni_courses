from project.food import Vegetable, Fruit, Seed, Meat
from project.animals.animal import Animal
from project.animals.animal import Bird
from abc import ABC, abstractmethod


class Hen(Bird):
    @property
    def gained_weight(self):
        return 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Seed, Meat]

    def make_sound(self):
        return "Cluck"


class Owl(Bird):
    @property
    def gained_weight(self):
        return 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self):
        return "Hoot Hoot"
