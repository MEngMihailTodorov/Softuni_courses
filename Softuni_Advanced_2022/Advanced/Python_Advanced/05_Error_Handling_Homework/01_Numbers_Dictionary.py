numbers_dictionary = {}

while True:
    number_as_string = str(input())
    if number_as_string == "Search":
        break
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f"The variable must be an integer")


while True:
    searched = str(input())
    if searched == "Remove":
        break
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print(f"Number does not exist in the dictionary")

while True:
    searched = str(input())
    if searched == "End":
        break
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print(f"Number does not exist in the dictionary")


print(numbers_dictionary)
