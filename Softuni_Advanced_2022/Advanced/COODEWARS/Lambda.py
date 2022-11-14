my_dict = {
    "name": "misho",
    "age": 23,
    "gender": "male",
    "edu": "engineer",
    "city": "sofia",
}

my_dict["name"] = "Margarita"


print(sorted(my_dict.items(), key=lambda x: (-len(x[0]), x[0])))


def funct(a):
    return "mama"


print(funct(my_dict))
