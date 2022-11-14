import math


def logarithm_calc(number: int, base):
    try:
        if base == "natural":
            return f'{math.log(number)}:.2f'
        else:
            return f'{math.log(number, float(base)):.2f}'
    except NameError:
        print(f"Enter a valid input")


number = int(input())
base = input()

print( logarithm_calc(number, base))