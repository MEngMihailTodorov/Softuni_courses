from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget - price < 0:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return f"Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return f"Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda u: u.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker.name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary

        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_price = 0
        for animal in self.animals:
            total_price += animal.money_for_care

        if total_price <= self.__budget:
            self.__budget -= total_price
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):

        lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return '\n'.join(str(r) for r in result)

    def workers_status(self):

        keepers = list(filter(lambda a: a.__class__.__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda a: a.__class__.__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda a: a.__class__.__name__ == "Vet", self.workers))

        result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        result.extend(keepers)

        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)

        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return '\n'.join(str(r) for r in result)


from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
