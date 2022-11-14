# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         return f"Person {self.name} says hello."
#
#     @staticmethod
#     def my_func():
#         return f"This is my funct"
#
#
# p = Person("Peter", 23)
#
# print(p.say_hi())
#
#
# class Class:
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def common_class(cls):
#         ingredients = ['tomato sauce', 'mozarela']
#
#         return cls(ingredients)
#
#
# p = Class('Misho')
# print(str(p.common_class()))


class Validator:
    @staticmethod
    def raise_if_str_null_or_empty(value):
        if not value.strip():
            raise ValueError('Invalid string value provided')


class Person:
    MIN_AGE = 0
    MAX_AGE = 140
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_str_null_or_empty(value)
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < self.MIN_AGE or value > self.MAX_AGE:
            raise ValueError(f'Age should be between {Person.MIN_AGE} and {Person.MAX_AGE}')
        self.__age = value


class Employee(Person):
    MIN_AGE = 16
    MAX_AGE = 100

    def __init__(self, name, age):
        super().__init__(name, age)


p = Person('Misho', 13)