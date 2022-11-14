def age_assignment(*args, **kwargs):
    my_dict = {}

    for arg in args:
        d = {arg: kwargs[arg[0]]}
        my_dict.update(d)

    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: ([x[0]])))
    result = ""

    for k, v in sorted_dict.items():
        result += f"{k} is {v} years old." + "\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))