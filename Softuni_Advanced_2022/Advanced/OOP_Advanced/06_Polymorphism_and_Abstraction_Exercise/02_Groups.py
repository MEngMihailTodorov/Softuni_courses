class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        name = self.name
        surname = other.surname
        new_account = Person(name, surname)
        return new_account


class Group:
    def __init__(self, name: str, people: list):
        self.people = people
        self.name = name

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        name = f"{self.name} {other.name}"
        people = self.people + other.people
        new_instance = Group(name, people)

        return new_instance

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(f'{p.name} {p.surname}' for p in self.people)}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item].name} {self.people[item].surname}"


import unittest


class TestGroups(unittest.TestCase):
    def setUp(self):
        self.p0 = Person('Aliko', 'Dangote')
        self.p1 = Person('Bill', 'Gates')
        self.p2 = Person('Warren', 'Buffet')
        self.p3 = Person('Elon', 'Musk')

    def test_person_init(self):
        self.assertEqual(self.p0.name, 'Aliko')
        self.assertEqual(self.p0.surname, 'Dangote')

    def test_person_str(self):
        self.assertEqual(str(self.p1), 'Bill Gates')

    def test_person_add(self):
        self.assertEqual(str(self.p2 + self.p3), 'Warren Musk')

    def test_group_init(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(first_group.name, '__VIP__')
        self.assertEqual(first_group.people, [self.p0, self.p1, self.p2])

    def test_group_str(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(str(first_group), "Group __VIP__ with members Aliko Dangote, Bill Gates, Warren Buffet")

    def test_group_len(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(len(first_group), 3)


if __name__ == "__main__":
    unittest.main()