def forecast(*args):
    cloudy_dict = {}
    rainy_dict = {}
    sunny_dict = {}

    for arg in args:
        city = arg[0]
        weather = arg[1]

        d = {city: weather}

        if weather == "Sunny":
            sunny_dict.update(d)
        elif weather == "Cloudy":
            cloudy_dict.update(d)
        elif weather == "Rainy":
            rainy_dict.update(d)

    cloudy_dict = dict(sorted(cloudy_dict.items(), key=lambda x: (x[0])))
    rainy_dict = dict(sorted(rainy_dict.items(), key=lambda x: (x[0])))
    sunny_dict = dict(sorted(sunny_dict.items(), key=lambda x: (x[0])))

    output = ''

    for k, v in sunny_dict.items():
        output += f"{k} - {v}"
        output += '\n'
    for k, v in cloudy_dict.items():
        output += f"{k} - {v}"
        output += '\n'
    for k, v in rainy_dict.items():
        output += f"{k} - {v}"
        output += '\n'

    return output


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
