def start_spring(**kwargs):
    dictionary = {}

    result = []

    for v, k in kwargs.items():
        if k not in dictionary.keys():
            dictionary[k] = []

        dictionary[k].append(v)

    dictionary = sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, val in dictionary:
        result.append(f"{key}:")
        for v in sorted(val):
            result.append(f"-{v}")

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
