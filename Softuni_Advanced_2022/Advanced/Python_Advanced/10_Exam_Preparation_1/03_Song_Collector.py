def add_songs(*args: tuple):
    songs_dict = {}
    output = ''
    for arg in args:
        if arg[0] not in songs_dict.keys():
            d = {arg[0]: arg[1]}
            songs_dict.update(d)
        else:
            for i in arg[1]:
                songs_dict[arg[0]].append(i)

    for key in songs_dict.keys():
        output += f"- {key}" + '\n'
        if songs_dict[key]:
            output += '\n'.join(f"{str(line)}" for line in songs_dict[key])
            output += '\n'
        else:
            pass

    return output


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
    ["Just in time, I found you just in time",
    "Before you came, my time was running low",
    "I was lost, the losing dice were tossed",
    "My bridges all were crossed, nowhere to go"])
))

print()
print()

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

print()
print()

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
