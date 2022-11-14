from os import linesep
from os import remove


while True:
    current_command = str(input())

    if current_command == "End":
        break
    else:
        current_command = current_command.split("-")

        if current_command[0] == "Create":
            file_name = current_command[1]
            file_path = './resources/' + file_name
            print(file_path)

            with open(file_path, 'w+') as text_file:
                text_file.write('')
                text_file.close()

        elif current_command[0] == "Add":
            file_name = current_command[1]
            file_path = './resources/' + file_name
            content = current_command[2]

            with open(file_path, "a+") as text_file:
                text_file.write(f"{content}\n")

        elif current_command[0] == "Replace":
            try:
                file_name = current_command[1]
                file_path = './resources/' + file_name
                old_string = current_command[2]
                new_string = current_command[3]

                with open(file_path, "r+") as text_file:
                    lines = text_file.read()
                    lines = lines.replace(old_string, new_string)

                    text_file.close()

                with open(file_path, "w") as text_file:
                    text_file.write(lines)

            except FileNotFoundError:
                print(f"An error occurred")

        elif current_command[0] == "Delete":
            try:
                file_name = current_command[1]
                file_path = './resources/' + file_name
                remove(file_path)

            except FileNotFoundError:
                print(f"An error occurred")