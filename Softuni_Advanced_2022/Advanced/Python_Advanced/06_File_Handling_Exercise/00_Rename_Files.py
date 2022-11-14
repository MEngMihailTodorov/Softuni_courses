import os

directory = input()
replace_what = input()
replace_with = input()

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    print(file)

    if os.path.isfile(file):
        new_name = filename.replace(replace_what, replace_with)
        