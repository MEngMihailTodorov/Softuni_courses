import math


def are_multiplicative_inverse(x: int, x_1: int, n: int):
    if math.gcd(x*x_1, n) == 1:
        return True
    return False


print(are_multiplicative_inverse(map(int, input().split())))