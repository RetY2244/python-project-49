import random
import math


def get_nums_pair_and_gcd():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    nums_pair = f'{num1} {num2}'
    gcd = math.gcd(num1, num2)

    return nums_pair, str(gcd)
