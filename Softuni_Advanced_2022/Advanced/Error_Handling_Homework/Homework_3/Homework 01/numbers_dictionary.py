class NonInteger(Exception):
    """The variable number must be an integer"""
    pass


class NonExistent(Exception):
    """Number does not exist in dictionary"""
    pass


numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(NonInteger.__doc__)
    line = input()

line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print(NonExistent.__doc__)
    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print(NonExistent.__doc__)
    line = input()

print(numbers_dictionary)
