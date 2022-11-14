def grocery_store(**kwargs):
    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = ''
    for key, val in sorted_kwargs.items():
        result += f"{key}: {val}" + "\n"

    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggss=12,
))
