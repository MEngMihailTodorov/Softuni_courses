# super() methods
# Inheritance - code reusability, add features without modification, transitive in nature
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name)
        self.age = age
        self.new_arg = []




s = Student('Peter', 'Ivanov')
print(s.last_name)
print(s.get_full_name())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old.'


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id
