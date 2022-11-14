class Customer:
    def __init__(self, name: str, age: int, number_id: int):
        self.name = name
        self.age = age
        self.id = number_id
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join(d.name for d in self.rented_dvds)})"

    @classmethod
    def get_next_id(cls):
        return cls.id

