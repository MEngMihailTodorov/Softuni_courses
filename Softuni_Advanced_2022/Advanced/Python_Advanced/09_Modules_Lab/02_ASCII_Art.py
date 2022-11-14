import pyfiglet as pfg


def print_figlet_art(msg: str):
    ascii_art = pfg.figlet_format(msg)

    print(ascii_art)


print(print_figlet_art(input()))